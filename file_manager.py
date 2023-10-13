from config import mysql
from flask import render_template

mysql = mysql
cursor = mysql.cursor(dictionary=True)


def file_manager():
    cursor.execute("SHOW TABLES")
    table_info = []

    for info in cursor.fetchall():
        table_name = info['Tables_in_adbms']
        cursor.execute(
            f"SELECT table_name, ROUND(data_length / (1024 * 1024), 4) AS data_length_mb FROM "
            f"information_schema.tables WHERE table_schema = 'adbms' AND table_name = '{table_name}'"
        )
        result = cursor.fetchone()
        if result:
            table_info.append(result)

        # Add SQL here (each table row count) issue #1

    return render_template('file-manager.html', table_info=table_info)


def file_manager_table():
    return render_template('file-manager-table.html')
