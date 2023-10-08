from config import mysql
from flask import render_template, request

mysql = mysql
cursor = mysql.cursor(dictionary=True)


def index():
    try:
        cursor.execute("SELECT * FROM sample_table")
        data = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        return render_template('index.html', data=data, column_names=column_names)
    except Exception as e:
        return f'Something went wrong: {e}'


def edit(cell_id):
    try:
        name = request.form['field']
        value = request.form['value']
        cursor.execute(f"UPDATE sample_table SET {name}=%s WHERE id=%s", (value, cell_id))
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


def insert():
    try:
        new_name = request.form['new_name']
        new_age = request.form['new_age']
        cursor.execute("INSERT INTO sample_table (name, age) VALUES (%s, %s)", (new_name, new_age))
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


def new_col():
    try:
        new_column_name = request.form['new_column_name']
        new_column_type = request.form['new_column_type']
        cursor.execute(f"ALTER TABLE sample_table ADD {new_column_name} {new_column_type}")
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


def drop_col():
    try:
        col_name = request.form['column_name']
        cursor.execute(f"ALTER TABLE sample_table DROP COLUMN {col_name}")
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


def drop_row():
    try:
        rowid = request.form['rowid']
        cursor.execute(f"DELETE FROM sample_table WHERE id={rowid}")
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


# not done
def edit_row(row_id):
    try:
        name = request.form['field']
        value = request.form['value']
        cursor.execute(f"UPDATE sample_table SET {name}=%s WHERE id=%s", (value, row_id))
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


# not work
def compare(value):
    try:
        cursor.execute(f"SELECT * FROM sample_table LIMIT 3")
        cursor.fetchall()
        print('-----------')
        print(value)
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'