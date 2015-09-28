import sqlite3 as sql
from flask import flash

def create_user_list():
    user_id = "shelan"
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO accounts(userid,lasttime) VALUES (?,?)", (user_id, "0"))
    connection.commit()
    connection.close()
    flash("users added")

def get_user_list():
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    users = cursor.execute("SELECT * from accounts")
    for user in users:
        flash(user)
    connection.commit()
    connection.close()
