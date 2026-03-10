/**
 * Action Item Extractor - Frontend logic
 */

const $ = (sel) => document.querySelector(sel);

const itemsEl = $('#items');
const notesEl = $('#notes-list');
const textEl = $('#text');
const saveNoteEl = $('#save_note');

async function extract(endpoint) {
  const text = textEl.value;
  const save = saveNoteEl.checked;
  itemsEl.textContent = endpoint.includes('llm') ? 'Extracting with LLM...' : 'Extracting...';
  try {
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, save_note: save }),
    });
    if (!res.ok) throw new Error('Request failed');
    const data = await res.json();
    if (!data.items || data.items.length === 0) {
      itemsEl.innerHTML = '<p class="muted">No action items found.</p>';
      return;
    }
    itemsEl.innerHTML = data.items.map(it =>
      `<div class="item"><input type="checkbox" data-id="${it.id}" /> <span>${escapeHtml(it.text)}</span></div>`
    ).join('');
    itemsEl.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      cb.addEventListener('change', async (e) => {
        const id = e.target.getAttribute('data-id');
        await fetch(`/action-items/${id}/done`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ done: e.target.checked }),
        });
      });
    });
  } catch (err) {
    console.error(err);
    itemsEl.textContent = 'Error extracting items';
  }
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

async function listNotes() {
  notesEl.textContent = 'Loading...';
  try {
    const res = await fetch('/notes');
    if (!res.ok) throw new Error('Request failed');
    const notes = await res.json();
    if (!notes || notes.length === 0) {
      notesEl.innerHTML = '<p class="muted">No notes saved.</p>';
      return;
    }
    notesEl.innerHTML = notes.map(n =>
      `<div class="note-item"><strong>#${n.id}</strong> ${escapeHtml(n.content.substring(0, 100))}${n.content.length > 100 ? '...' : ''} <span class="muted">${n.created_at}</span></div>`
    ).join('');
  } catch (err) {
    console.error(err);
    notesEl.textContent = 'Error loading notes';
  }
}

function init() {
  $('#extract').addEventListener('click', () => extract('/action-items/extract'));
  $('#extract-llm').addEventListener('click', () => extract('/action-items/extract-llm'));
  $('#list-notes').addEventListener('click', listNotes);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
