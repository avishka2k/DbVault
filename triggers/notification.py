from config import mysql

mysql = mysql
cursor = mysql.cursor(dictionary=True)


def notify_insert_trigger(file_name, table_name):
    trigger_name = f'{table_name}_after_insert'
    cursor.execute(f'''
        CREATE TRIGGER `{trigger_name}` AFTER INSERT ON `{table_name}` FOR EACH ROW BEGIN
        INSERT INTO recents(file_name, folder_name, date_time)
            VALUES('{file_name}', '{table_name}', CURRENT_TIMESTAMP());
        END
    ''')
    mysql.commit()


def notify_delete_trigger(file_name, table_name):
    trigger_name = f'{table_name}_after_delete'
    cursor.execute(f'''
        CREATE TRIGGER `{trigger_name}` AFTER DELETE ON `{table_name}` FOR EACH ROW BEGIN
        INSERT INTO recents(file_name, folder_name, date_time)
            VALUES('{file_name}', '{table_name}', CURRENT_TIMESTAMP());
        END
    ''')
    mysql.commit()