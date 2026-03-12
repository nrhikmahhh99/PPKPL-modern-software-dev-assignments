"""
Action item extraction service with pattern recognition for due dates and assignees.
"""

import re
from dataclasses import dataclass


@dataclass
class ExtractedActionItem:
    """A single extracted action item with optional metadata."""

    description: str
    due_date: str | None = None
    assignee: str | None = None


# --- Pattern definitions ---

# Bullet/numbered list prefixes: - * • 1. 2) etc.
BULLET_PREFIX = re.compile(r"^\s*([-*•]|\d+[.)]\s*)\s*", re.IGNORECASE)

# Action keywords (case-insensitive)
KEYWORD_PREFIXES = (
    "todo:",
    "action:",
    "next:",
    "task:",
    "must:",
    "should:",
    "need to:",
)

# Checkbox patterns
CHECKBOX_PATTERNS = ("[ ]", "[x]", "[todo]", "[ ] ")

# Due date patterns (order matters - more specific first)
DUE_PATTERNS = [
    # "due: 2024-01-15", "deadline: 12/31/2024", "by Monday"
    re.compile(
        r"\b(?:due\s*(?:date)?|deadline|by)\s*[:\s]+([A-Za-z0-9/\-]+(?:\s+[A-Za-z0-9/\-]+)*)\b",
        re.IGNORECASE,
    ),
    # "(due Jan 15)", "[by 2024-01-15]"
    re.compile(
        r"[([]\s*(?:due|by)\s+([^)\]}\]]+?)\s*[)\]]",
        re.IGNORECASE,
    ),
    # ISO or slash date standalone
    re.compile(r"\b(\d{4}-\d{2}-\d{2})\b"),
    re.compile(r"\b(\d{1,2}/\d{1,2}/\d{2,4})\b"),
]

# Assignee patterns
ASSIGNEE_PATTERNS = [
    # "assignee: John", "assigned to: @jane", "owner: team"
    re.compile(
        r"\b(?:assignee|assigned\s+to|owner|responsible)\s*[:\s]+[@]?([A-Za-z0-9_-]+(?:\s+[A-Za-z0-9_-]+)?)",
        re.IGNORECASE,
    ),
    # "@john" or "@john_doe"
    re.compile(r"@([A-Za-z0-9_-]+)"),
    # "(assignee: John)", "[assigned: Jane]"
    re.compile(
        r"[([]\s*(?:assignee|assigned)\s*[:\s]+([^)\]}\]]+)\s*[)\]]",
        re.IGNORECASE,
    ),
]

# Imperative verb starters for fallback sentence extraction
IMPERATIVE_STARTERS = {
    "add", "create", "implement", "fix", "update", "write", "check",
    "verify", "refactor", "document", "design", "investigate", "review",
    "ship", "deploy", "test", "build", "setup", "configure", "complete",
}


def _is_action_line(line: str) -> bool:
    """Check if a line looks like an action item."""
    stripped = line.strip()
    if not stripped:
        return False
    lower = stripped.lower()
    if BULLET_PREFIX.match(stripped):
        return True
    if any(lower.startswith(kw) for kw in KEYWORD_PREFIXES):
        return True
    if any(marker in lower for marker in CHECKBOX_PATTERNS):
        return True
    if stripped.endswith("!"):
        return True
    # Numbered list
    if re.match(r"^\d+[.)]\s+\S", stripped):
        return True
    return False


def _clean_description(raw: str) -> str:
    """Remove bullet prefix, checkbox markers, and trim."""
    s = BULLET_PREFIX.sub("", raw).strip()
    for marker in ("[ ]", "[x]", "[todo]"):
        s = s.replace(marker, "").strip()
    return s.strip()


def _parse_due_date(text: str) -> str | None:
    """Extract due date from text. Returns first match or None."""
    for pat in DUE_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(1).strip()
    return None


def _parse_assignee(text: str) -> str | None:
    """Extract assignee from text. Returns first match or None."""
    for pat in ASSIGNEE_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(1).strip()
    return None


def _remove_metadata_from_description(desc: str, due: str | None, assignee: str | None) -> str:
    """
    Remove parsed due_date and assignee patterns from description
    so the core task text stays clean.
    """
    result = desc
    if due:
        for pat in DUE_PATTERNS:
            result = pat.sub(" ", result)
    if assignee:
        for pat in ASSIGNEE_PATTERNS:
            result = pat.sub(" ", result)
    # Collapse whitespace and trim
    result = re.sub(r"\s+", " ", result).strip(" ,;-")
    return result


def _looks_imperative(sentence: str) -> bool:
    """Heuristic: does the sentence start with an imperative verb?"""
    words = re.findall(r"[A-Za-z']+", sentence)
    if not words:
        return False
    return words[0].lower() in IMPERATIVE_STARTERS


def _parse_single_item(raw: str) -> ExtractedActionItem:
    """Parse one raw line into ExtractedActionItem with due_date and assignee."""
    cleaned = _clean_description(raw)
    if not cleaned:
        return ExtractedActionItem(description=raw.strip())
    due = _parse_due_date(cleaned)
    assignee = _parse_assignee(cleaned)
    description = _remove_metadata_from_description(cleaned, due, assignee)
    if not description:
        description = cleaned
    return ExtractedActionItem(description=description, due_date=due, assignee=assignee)


def extract_action_items(text: str) -> list[ExtractedActionItem]:
    """
    Extract action items from free-form text using pattern recognition.

    Supports:
    - Bullet lists (-, *, •, 1., 2))
    - Keyword prefixes (TODO:, ACTION:, NEXT:, TASK:, etc.)
    - Checkbox markers ([ ], [x], [todo])
    - Lines ending with !
    - Due date patterns (due: X, by X, deadline X, @date, etc.)
    - Assignee patterns (assignee: X, @username, etc.)
    - Fallback: imperative sentences when no explicit patterns match
    """
    if not text or not text.strip():
        return []

    lines = text.splitlines()
    extracted: list[ExtractedActionItem] = []

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if _is_action_line(line):
            item = _parse_single_item(line)
            if item.description:
                extracted.append(item)

    # Fallback: split by sentences and pick imperative ones
    if not extracted:
        sentences = re.split(r"(?<=[.!?])\s+", text.strip())
        seen_lower: set[str] = set()
        for s in re.split(r"\n+", text):
            s = s.strip()
            if not s:
                continue
            # Try sentence-level split
            for sent in re.split(r"(?<=[.!?])\s+", s):
                sent = sent.strip()
                if not sent or len(sent) < 3:
                    continue
                if _looks_imperative(sent):
                    key = sent.lower()
                    if key not in seen_lower:
                        seen_lower.add(key)
                        extracted.append(_parse_single_item(sent))

    # Deduplicate by description (case-insensitive)
    seen: set[str] = set()
    unique: list[ExtractedActionItem] = []
    for item in extracted:
        key = item.description.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)

    return unique
