from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    rows = cursor.fetchall()
    conn.close()

    items = []
    for row in rows:
        items.append({
            'id': row[0],
            'name': row[1],
            'description': row[2]
        })
    
    return jsonify(items), 200

# Route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', '')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()

    return jsonify({'id': item_id, 'name': name, 'description': description}), 201

# Route to update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE items SET name = ?, description = ? WHERE id = ?', (name, description, item_id))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({'error': 'Item not found'}), 404

    conn.close()
    return jsonify({'id': item_id, 'name': name, 'description': description}), 200

# Route to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({'error': 'Item not found'}), 404

    conn.close()
    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')