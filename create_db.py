#!/usr/bin/env python3
import sqlite3 as sql
import random

def main():
    print("Creating databases...")
    connection = sql.connect("./.flights.db")
    cursor = connection.cursor()
    print("Creating table...")
    cursor.execute("""CREATE TABLE IF NOT EXISTS bookings(name varchar(40) not NULL, booking_ref int primary key not NULL, flight_no int not NULL);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(name varchar(40) not NULL, age int not NULL, user_id int primary key not NULL);""")
    for i in range(25):
        name = "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for j in range(10)])
        age = random.randint(1, 100)
        user_id = i
        row = [name, age, user_id]
        sql_statement = "INSERT INTO user VALUES(\'{0}\',{1}, {2});".format(*row)
        print(sql_statement)
        cursor.execute(sql_statement)
    connection.commit()
    return

if __name__ == '__main__':
    main()
