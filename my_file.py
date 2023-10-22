from config import mysql
from flask import render_template, request

mysql = mysql
cursor = mysql.cursor(dictionary=True)


def my_file():
    cursor.execute("SHOW TABLES")
    table_info = []

    for info in cursor.fetchall():
        table_name = info['Tables_in_adbms']
        cursor.execute(
            f"SELECT table_name, ROUND(data_length / (1024 * 1024), 4) AS data_length_mb, "
            f"DATE_FORMAT(CREATE_TIME, '%d,%b %Y %h:%i %p') AS create_time_formatted "
            f"FROM information_schema.tables "
            f"WHERE table_schema = 'adbms' AND table_name = '{table_name}'"
        )
        result = cursor.fetchone()
        if result:
            table_info.append(result)
        cursor.execute(f"SELECT COUNT(*) AS table_items FROM {table_name}")
        result = cursor.fetchone()
        if result:
            table_info[-1]['table_items'] = result['table_items']

    cursor.execute(f"SELECT * FROM recents")
    recents_data = cursor.fetchall()
    return render_template(
        'my-files.html',
        table_info=table_info,
        recents_data=recents_data
    )