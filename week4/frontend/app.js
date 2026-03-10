// Fungsi bantuan untuk fetch (bawaan dari starter code Anda)
async function fetchJSON(url, options = {}) {
  const res = await fetch(url, options);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// Fungsi loadNotes yang sudah digabungkan dengan logika pencarian
async function loadNotes(query = "") {
  const list = document.getElementById("notes");
  list.innerHTML = ""; // Kosongkan daftar sebelum mengisi yang baru

  // Tentukan URL: jika ada query, panggil endpoint search. Jika tidak, ambil semua.
  // Catatan: Menggunakan /search/ (dengan garis miring) agar sesuai dengan backend
  let url = "/notes/";
  if (query) {
    url = `/notes/search/?q=${encodeURIComponent(query)}`;
  }

  try {
    const res = await fetch(url);
    const notes = await res.json();

    for (const n of notes) {
      const li = document.createElement("li");
      li.textContent = `${n.title}: ${n.content}`;
      list.appendChild(li);
    }
  } catch (error) {
    console.error("Gagal mengambil catatan:", error);
  }
}

// Fungsi loadActions (tidak ada yang diubah)
async function loadActions() {
  const list = document.getElementById("actions");
  list.innerHTML = "";
  try {
    const items = await fetchJSON("/action-items/");
    for (const a of items) {
      const li = document.createElement("li");
      li.textContent = `${a.description} [${a.completed ? "done" : "open"}]`;
      if (!a.completed) {
        const btn = document.createElement("button");
        btn.textContent = "Complete";
        btn.onclick = async () => {
          await fetchJSON(`/action-items/${a.id}/complete`, { method: "PUT" });
          loadActions();
        };
        li.appendChild(btn);
      }
      list.appendChild(li);
    }
  } catch (error) {
    console.error("Gagal mengambil action items:", error);
  }
}

window.addEventListener("DOMContentLoaded", () => {
  // Event listener untuk form penambahan catatan baru
  document.getElementById("note-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const title = document.getElementById("note-title").value;
    const content = document.getElementById("note-content").value;
    await fetchJSON("/notes/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, content }),
    });
    e.target.reset();

    // Ambil ulang teks dari kotak pencarian (jika ada) saat memuat ulang notes
    const searchVal = document.getElementById("search-input")
      ? document.getElementById("search-input").value
      : "";
    loadNotes(searchVal);
  });

  // Event listener untuk form penambahan action item
  document
    .getElementById("action-form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();
      const description = document.getElementById("action-desc").value;
      await fetchJSON("/action-items/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description }),
      });
      e.target.reset();
      loadActions();
    });

  // Event listener untuk kolom pencarian! (Diletakkan di dalam DOMContentLoaded agar aman)
  const searchInput = document.getElementById("search-input");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      loadNotes(e.target.value);
    });
  }

  // Panggil saat halaman pertama kali dimuat
  loadNotes();
  loadActions();
});
