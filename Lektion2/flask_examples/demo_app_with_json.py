from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" (just a list to store items)
items: list = []

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', '')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    item = {
        'id': len(items) + 1,  # Simulate auto-incrementing ID
        'name': name,
        'description': description
    }
    items.append(item)
    
    return jsonify(item), 201

# Route to update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    # Find item by ID
    for item in items:
        if item['id'] == item_id:
            item['name'] = name
            item['description'] = description
            return jsonify(item), 200

    return jsonify({'error': 'Item not found'}), 404

# Route to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]

    return jsonify({'message': 'Item deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')