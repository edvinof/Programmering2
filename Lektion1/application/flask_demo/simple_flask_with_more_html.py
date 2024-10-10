from flask import Flask, render_template_string
import random

# app = Flask("simple_flask_with_html")
app = Flask(__name__)

@app.route('/')
def home():
    html = """
<body>
    <div class="main-container">
        <div class="container">
            <h1>Programmering 2, Välkomna till Flask!</h1>
            <p>Här är en enkel HTML-sida med lite css. Läs mer om Flask på länken nedan:</p>
            <a href="https://flask.palletsprojects.com/" target="_blank" class="button">Flask Doc</a>
        </div>
        <div class="container">
            <h1>Här är dagens arbetsgrupper:</h1>
            <a href="/groups" class="button">Grupper</a>
        </div>
    </div>
</body>

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f5;
        margin: 0;
        padding: 20px;
        color: #333;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        flex-direction: column;
        min-height: 100vh;
    }
    .main-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
    }
    .container {
        background-color: #ffffff;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #45a049;
    }
</style>
    """
    return render_template_string(html)

@app.route('/groups')
def groups():
    # Read the names from klasslista.txt
    with open('klasslista.txt', 'r', encoding='utf-8') as file:
        names = [line.strip() for line in file.readlines()]

    # Shuffle names and create groups of 5
    random.shuffle(names)
    group_size = 5
    groups = [names[i:i + group_size] for i in range(0, len(names), group_size)]

    # HTML template to display the groups
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Groups</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f5;
                margin: 0;
                padding: 20px;
                color: #333;
            }
            .group-container {
                max-width: 800px;
                margin: 0 auto;
            }
            .group {
                background-color: #ffffff;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            h2 {
                color: #4CAF50;
                margin-bottom: 10px;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                padding: 5px 0;
            }
        </style>
    </head>
    <body>
        <div class="group-container">
            <h1>Randomly Generated Groups</h1>
            {% for group in groups %}
            <div class="group">
                <h2>Group {{ loop.index }}</h2>
                <ul>
                    {% for name in group %}
                    <li>{{ name }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """

    return render_template_string(html, groups=groups)

if __name__ == '__main__':
    app.run(debug=True)