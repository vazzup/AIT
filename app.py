#!/usr/bin/env python
from flask import Flask, make_response, request
from flask import jsonify
from flask_cors import CORS
import sqlite3 as sql

app = Flask(__name__)
CORS(app)

@app.route('/booking_verify', methods=['GET'])
def booking_verify():
    name = request.args.get("name")
    booking_ref = request.args.get("booking_ref")
    flight_no = request.args.get("flight_no")
    connection = sql.connect('./.flights.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT count(*) FROM bookings WHERE name IS (?) AND booking_ref is (?) AND flight_no IS (?);""", (name, booking_ref, flight_no))
    count = 0
    for row in cursor:
        for item in row:
            count += int(item)
    if count is 0:
        return '<h3> No Booking of this kind exists </h3>'
    else:
        return '<h3> Booking exists!</h3>'

@app.route('/get_age_data', methods=['GET'])
def get_age_data():
    connection = sql.connect('./.flights.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT age FROM user;""")
    my_dict = {'1-25':0, '26-40':0, '41-60':0, '61+':0}
    for row in cursor:
        for item in row:
            if item <= 25:
                my_dict['1-25']+=1
            elif item <= 40:
                my_dict['26-40']+=1
            elif item <= 60:
                my_dict['41-60']+=1
            else:
                my_dict['61+']+=1
    data = []
    for key, item in my_dict.items():
        temp = [key, item]
        data.append(temp)
    return jsonify({"info": data})

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug = True)
