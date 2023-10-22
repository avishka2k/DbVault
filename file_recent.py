from config import mysql
from flask import render_template, request

mysql = mysql
cursor = mysql.cursor(dictionary=True)


def file_recent():
    cursor.execute(f"SELECT * FROM recents")
    recents_data = cursor.fetchall()
    return render_template('recents.html', recents_data=recents_data)


def file_recent_delete_all():
    try:
        cursor.execute("TRUNCATE TABLE recents")
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'

