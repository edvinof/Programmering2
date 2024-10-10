import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask API!")

@app.route('/groups')
def groups():
    # Read the names from 'klasslista.txt'
    try:
        with open('klasslista.txt', 'r', encoding='utf-8') as file:
            names = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return jsonify(error="The file 'klasslista.txt' was not found."), 404

    # Shuffle names and create groups of up to 5
    random.shuffle(names)
    group_size = 5
    groups = [names[i:i + group_size] for i in range(0, len(names), group_size)]

    # Prepare the data to be returned as JSON
    groups_data = [
        {
            'group_number': idx + 1,
            'members': group
        } for idx, group in enumerate(groups)
    ]

    return jsonify(groups=groups_data)

if __name__ == '__main__':
    app.run(debug=True)