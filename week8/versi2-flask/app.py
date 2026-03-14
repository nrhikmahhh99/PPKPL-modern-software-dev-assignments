from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Fungsi untuk membuat database
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  title TEXT NOT NULL, 
                  description TEXT, 
                  status TEXT DEFAULT 'todo')''')
    conn.commit()
    conn.close()

# Rute untuk menampilkan halaman HTML utama
@app.route('/')
def index():
    return render_template('index.html')

# API: Mengambil semua task (Read)
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = [{'id': row[0], 'title': row[1], 'description': row[2], 'status': row[3]} for row in c.fetchall()]
    conn.close()
    return jsonify(tasks)

# API: Menambah task baru (Create)
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", 
              (data['title'], data.get('description', ''), 'todo'))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

# API: Menghapus task (Delete)
@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

# API: Memperbarui status task (Update)
@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET status=? WHERE id=?", (data['status'], id))
    conn.commit()
    conn.close()
    return jsonify({"status": "updated"})

if __name__ == '__main__':
    init_db()
    # Kita jalankan di port 5001 agar tidak bentrok dengan versi 1
    app.run(debug=True, port=5001)