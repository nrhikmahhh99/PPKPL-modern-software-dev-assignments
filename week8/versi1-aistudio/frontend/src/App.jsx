import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "http://localhost:5000/tasks";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    status: "todo",
  });
  const [error, setError] = useState("");

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    const res = await axios.get(API_URL);
    setTasks(res.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.title.trim()) {
      setError("Title cannot be empty");
      return;
    }
    setError("");
    await axios.post(API_URL, formData);
    setFormData({ title: "", description: "", status: "todo" });
    fetchTasks();
  };

  const updateStatus = async (id, newStatus) => {
    const task = tasks.find((t) => t.id === id);
    await axios.put(`${API_URL}/${id}`, { ...task, status: newStatus });
    fetchTasks();
  };

  const deleteTask = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
    fetchTasks();
  };

  const TaskColumn = ({ status, title, bgColor }) => (
    <div className="flex-1 min-w-[300px] bg-gray-50 p-4 rounded-xl shadow-inner">
      <h2
        className={`text-lg font-bold mb-4 uppercase tracking-wider ${bgColor}`}
      >
        {title}
      </h2>
      {tasks
        .filter((t) => t.status === status)
        .map((task) => (
          <div
            key={task.id}
            className="bg-white p-4 rounded-lg shadow-md mb-3 border-l-4 border-blue-500 hover:shadow-lg transition"
          >
            <h3 className="font-semibold text-gray-800">{task.title}</h3>
            <p className="text-sm text-gray-600 mb-3">{task.description}</p>
            <div className="flex justify-between items-center mt-2">
              <select
                value={task.status}
                onChange={(e) => updateStatus(task.id, e.target.value)}
                className="text-xs bg-gray-100 border rounded p-1"
              >
                <option value="todo">To Do</option>
                <option value="in progress">In Progress</option>
                <option value="done">Done</option>
              </select>
              <button
                onClick={() => deleteTask(task.id)}
                className="text-red-500 hover:text-red-700 text-sm font-medium"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-100 p-8 font-sans">
      <div className="max-w-6xl mx-auto">
        <header className="mb-10 text-center">
          <h1 className="text-4xl font-extrabold text-gray-900 mb-2">
            Task Management
          </h1>
          <p className="text-gray-500 text-lg">
            Organize your development workflow
          </p>
        </header>

        {/* Form Section */}
        <form
          onSubmit={handleSubmit}
          className="bg-white p-6 rounded-2xl shadow-sm mb-12 flex flex-col md:flex-row gap-4 items-end border border-gray-200"
        >
          <div className="flex-1 w-full text-left">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Task Title*
            </label>
            <input
              type="text"
              placeholder="Fix bug in API..."
              className={`w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none ${error ? "border-red-500" : "border-gray-300"}`}
              value={formData.title}
              onChange={(e) =>
                setFormData({ ...formData, title: e.target.value })
              }
            />
            {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
          </div>
          <div className="flex-[2] w-full text-left">
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <input
              type="text"
              placeholder="Add more details..."
              className="w-full p-2 border border-gray-300 rounded-lg outline-none"
              value={formData.description}
              onChange={(e) =>
                setFormData({ ...formData, description: e.target.value })
              }
            />
          </div>
          <button
            type="submit"
            className="bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-blue-700 transition w-full md:w-auto"
          >
            Add Task
          </button>
        </form>

        {/* Board Section */}
        <div className="flex flex-wrap gap-6">
          <TaskColumn status="todo" title="🎯 To Do" bgColor="text-gray-600" />
          <TaskColumn
            status="in progress"
            title="⚡ In Progress"
            bgColor="text-blue-600"
          />
          <TaskColumn status="done" title="✅ Done" bgColor="text-green-600" />
        </div>
      </div>
    </div>
  );
}
