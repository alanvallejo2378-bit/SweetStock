* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background-color: #f4f7f6;
    color: #333;
    padding: 20px;
}

.container {
    max-width: 900px;
    margin: 0 auto;
}

header {
    text-align: center;
    margin-bottom: 30px;
}

header h1 {
    color: #2c3e50;
    font-size: 2.2rem;
}

.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

.card {
    background: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.card h2 {
    font-size: 1.3rem;
    margin-bottom: 15px;
    color: #34495e;
}

form {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

input, select {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 1rem;
}

.btn {
    background-color: #27ae60;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 6px;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s ease;
}

.btn:hover {
    background-color: #219150;
}

.inventory-list {
    list-style: none;
}

.inventory-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px;
    border-bottom: 1px solid #eee;
}

.inventory-item:last-child {
    border-bottom: none;
}

.badge {
    background-color: #e8f8f5;
    color: #16a085;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.9rem;
    font-weight: bold;
}