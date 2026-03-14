const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());
app.get("/", (req, res) => {
  res.send("Backend Task Manager sudah berjalan dengan baik!");
});

// Initialize SQLite Database
const db = new sqlite3.Database("./tasks.db", (err) => {
  if (err) console.error(err.message);
  console.log("Connected to the tasks database.");
});

// Create tasks table if it doesn't exist
db.run(`CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'todo'
)`);

// --- API Endpoints ---

// READ all tasks
app.get("/tasks", (req, res) => {
  db.all("SELECT * FROM tasks", [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

// CREATE a task
app.post("/tasks", (req, res) => {
  const { title, description, status } = req.body;
  if (!title) return res.status(400).json({ error: "Title is required" });

  const sql = `INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)`;
  db.run(sql, [title, description, status || "todo"], function (err) {
    if (err) return res.status(500).json({ error: err.message });
    res
      .status(201)
      .json({ id: this.lastID, title, description, status: status || "todo" });
  });
});

// UPDATE a task
app.put("/tasks/:id", (req, res) => {
  const { title, description, status } = req.body;
  const sql = `UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?`;
  db.run(sql, [title, description, status, req.params.id], function (err) {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ updated: this.changes });
  });
});

// DELETE a task
app.delete("/tasks/:id", (req, res) => {
  db.run(`DELETE FROM tasks WHERE id = ?`, req.params.id, function (err) {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ deleted: this.changes });
  });
});

const PORT = 5000;
app.listen(PORT, () =>
  console.log(`Backend running on http://localhost:${PORT}`),
);
