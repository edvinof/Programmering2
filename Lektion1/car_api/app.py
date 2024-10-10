from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'cars.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            license_plate TEXT PRIMARY KEY,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            kilometer INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return redirect(url_for('show_all_cars'))

@app.route('/cars', methods=['GET'])
def show_all_cars():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return render_template('cars.html', cars=cars)

@app.route('/api/cars', methods=['GET'])
def api_get_all_cars():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    car_list = [dict(car) for car in cars]
    return jsonify(car_list)

@app.route('/api/cars/<license_plate>', methods=['GET'])
def api_get_car(license_plate):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM cars WHERE license_plate = ?', (license_plate,)).fetchone()
    conn.close()
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    return jsonify(dict(car))

@app.route('/api/cars/brand/<brand_name>', methods=['GET'])
def api_get_cars_by_brand(brand_name):
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars WHERE brand = ?', (brand_name,)).fetchall()
    conn.close()
    car_list = [dict(car) for car in cars]
    return jsonify(car_list)

@app.route('/add_car', methods=['GET'])
def add_car_form():
    return render_template('add_car.html')

@app.route('/add_car', methods=['POST'])
def add_car():
    license_plate = request.form['license_plate']
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
    kilometer = request.form['kilometer']

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO cars (license_plate, brand, model, year, kilometer) VALUES (?, ?, ?, ?, ?)',
                     (license_plate, brand, model, year, kilometer))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return 'Error: License plate already exists', 400
    conn.close()
    return redirect(url_for('show_all_cars'))

if __name__ == '__main__':
    app.run(debug=True)