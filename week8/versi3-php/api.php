<?php
header('Content-Type: application/json');
$file = 'tasks.json';

// Buat file JSON jika belum ada
if (!file_exists($file)) {
    file_put_contents($file, json_encode([]));
}

// Ambil data yang ada
$tasks = json_decode(file_get_contents($file), true);
$method = $_SERVER['REQUEST_METHOD'];

// READ (GET)
if ($method === 'GET') {
    echo json_encode($tasks);
    exit;
}

// Ambil data dari Frontend
$input = json_decode(file_get_contents('php://input'), true);

// CREATE (POST)
if ($method === 'POST') {
    $newTask = [
        'id' => time(), // Gunakan waktu sebagai ID unik
        'title' => $input['title'],
        'description' => $input['description'] ?? '',
        'status' => 'todo'
    ];
    $tasks[] = $newTask;
    file_put_contents($file, json_encode($tasks));
    echo json_encode(['status' => 'success']);
    exit;
}

// UPDATE (PUT)
if ($method === 'PUT') {
    $id = $_GET['id'];
    foreach ($tasks as &$task) {
        if ($task['id'] == $id) {
            $task['status'] = $input['status'];
            break;
        }
    }
    file_put_contents($file, json_encode(array_values($tasks)));
    echo json_encode(['status' => 'updated']);
    exit;
}

// DELETE (DELETE)
if ($method === 'DELETE') {
    $id = $_GET['id'];
    $tasks = array_filter($tasks, function($task) use ($id) {
        return $task['id'] != $id;
    });
    file_put_contents($file, json_encode(array_values($tasks)));
    echo json_encode(['status' => 'deleted']);
    exit;
}
?>