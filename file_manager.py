from config import mysql
from flask import render_template, request
from urllib.parse import parse_qs
from triggers import create_insert_trigger, create_delete_trigger, create_update_trigger, create_alter_trigger

mysql = mysql
cursor = mysql.cursor(dictionary=True)


# def file_manager():
#     cursor.execute("SHOW TABLES")
#     table_info = []
#
#     for info in cursor.fetchall():
#         table_name = info['Tables_in_adbms']
#         cursor.execute(
#             f"SELECT table_name, ROUND(data_length / (1024 * 1024), 4) AS data_length_mb, "
#             f"DATE_FORMAT(CREATE_TIME, '%d,%b %Y %h:%i %p') AS create_time_formatted "
#             f"FROM information_schema.tables "
#             f"WHERE table_schema = 'adbms' AND table_name = '{table_name}'"
#         )
#         result = cursor.fetchone()
#         if result:
#             table_info.append(result)
#         cursor.execute(f"SELECT COUNT(*) AS table_items FROM {table_name}")
#         result = cursor.fetchone()
#         if result:
#             table_info[-1]['table_items'] = result['table_items']
#
#     cursor.execute(f"SELECT * FROM recents")
#     recents_data = cursor.fetchall()
#
#     cursor.execute("CALL CountTables('adbms')")
#     # Fetch the result
#     count_tables = cursor.fetchone()
#     table_count = count_tables['COUNT(*)']
#
#     return render_template(
#         'file-manager.html',
#         table_info=table_info,
#         recents_data=recents_data,
#         resultcount=table_count - 1
#     )


def get_table_info(cur):
    cur.execute("SHOW TABLES")
    table_info = []

    for info in cur.fetchall():
        table_name = info['Tables_in_adbms']
        cur.execute(
            """
            SELECT table_name, ROUND(data_length / (1024 * 1024), 4) AS data_length_mb, 
            DATE_FORMAT(CREATE_TIME, %s) AS create_time_formatted 
            FROM information_schema.tables 
            WHERE table_schema = %s AND table_name = %s
            """,
            ('%d,%b %Y %h:%i %p', 'adbms', table_name)
        )
        result = cur.fetchone()
        if result:
            table_info.append(result)
        cur.execute(f"SELECT COUNT(*) AS table_items FROM {table_name}")
        result = cur.fetchone()
        if result:
            table_info[-1]['table_items'] = result['table_items']

    return table_info


def get_recents_data(cur):
    cur.execute(f"SELECT * FROM recents")
    return cur.fetchall()


def get_table_count():
    cur = mysql.cursor(dictionary=True)
    cur.execute("CALL CountTables('adbms')")
    count_tables = cur.fetchone()
    cur.close()
    return count_tables['COUNT(*)']


def file_manager():
    try:
        table_info = get_table_info(cursor)
        recents_data = get_recents_data(cursor)
        # table_count = get_table_count()
    except Exception as e:
        return render_template('error.html', error=str(e))
    return render_template(
        'file-manager.html',
        table_info=table_info,
        recents_data=recents_data,
        resultcount=''
    )


def add_new_table():
    table_name = request.form['table_name']
    column_name = request.form['initial_column']
    relationship = request.form['relationship']
    relationship_id = relationship + 'Id'

    try:
        if relationship == "":
            cursor.execute(f'''
                CREATE TABLE {table_name} (
                {table_name}Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                {column_name} varchar(255)
                )
            ''')
        else:
            cursor.execute(f'''
                CREATE TABLE {table_name} (
                {table_name}Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                {column_name} varchar(255),
                {relationship_id} int,
                FOREIGN KEY ({relationship_id}) REFERENCES {relationship}({relationship_id})
                )
            ''')
        mysql.commit()
        # create triggers
        create_insert_trigger('Created New Record', table_name)
        create_delete_trigger('Deleted Record', table_name)
        create_update_trigger('Updated Record', table_name)
        create_alter_trigger('Added New Column', table_name)

        return render_template('file-manager.html')
    except Exception as e:
        return f'Something went wrong: {e}'


def drop_table():
    table_name = request.form['table_name']
    try:
        cursor.execute(f'DROP TABLE {table_name}')
        mysql.commit()
        return "success"
    except Exception as e:
        return f'Something went wrong: {e}'


class FileManager:
    tableName = None

    def file_manager_table(self, table_name):
        self.tableName = table_name
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
            column_names = [column[0] for column in cursor.description]
            return render_template(
                'file-manager-table.html',
                data=data, column_names=column_names,
                table_name=table_name
            )
        except Exception as e:
            return f'Something went wrong: {e}'

    def edit_cell(self, cell_id):
        table_name = self.tableName
        try:
            name = request.form['field']
            value = request.form['value']
            cursor.execute(f"UPDATE {table_name} SET {name}=%s WHERE {table_name}Id=%s", (value, cell_id))
            mysql.commit()
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'

    def insert_row(self):
        table_name = self.tableName
        try:

            form_data_str = request.form['form_data']
            form_data_dict = parse_qs(form_data_str)
            print('--------------')
            print(table_name)
            columns = ', '.join(form_data_dict.keys())
            values_count = ', '.join(['%s'] * len(form_data_dict))
            values = [item[0] for item in form_data_dict.values()]
            cursor.execute(f'INSERT INTO {table_name} ({columns}) VALUES ({values_count})', tuple(values))
            mysql.commit()
            return "success"

        except Exception as e:
            return f'Something went wrong: {e}'

    def new_col(self):
        table_name = self.tableName
        try:
            new_column_name = request.form['new_column_name']
            new_column_type = request.form['new_column_type']
            cursor.execute(f"ALTER TABLE {table_name} ADD {new_column_name} {new_column_type}")
            mysql.commit()
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'

    def drop_col(self):
        table_name = self.tableName
        try:
            col_name = request.form['column_name']
            cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {col_name}")
            mysql.commit()
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'

    def drop_row(self):
        table_name = self.tableName
        try:
            rowid = request.form['rowid']
            cursor.execute(f"DELETE FROM {table_name} WHERE {table_name}Id={rowid}")
            mysql.commit()
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'

    # not done
    def edit_row(self, row_id):
        table_name = self.tableName
        try:
            name = request.form['field']
            value = request.form['value']
            cursor.execute(f"UPDATE {table_name} SET {name}=%s WHERE {table_name}Id=%s", (value, row_id))
            mysql.commit()
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'

    # not work
    def compare(self, value):
        table_name = self.tableName
        try:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
            cursor.fetchall()
            print('-----------')
            print(value)
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'

    def edit_col_name(self):
        table_name = self.tableName
        col_name = request.form['value']
        print(col_name)
        print(table_name)
        try:
            cursor.execute(f'ALTER TABLE {table_name} RENAME COLUMN {col_name} TO new_cname')
            mysql.commit()
            return "success"
        except Exception as e:
            return f'Something went wrong: {e}'


