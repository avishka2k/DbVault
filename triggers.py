from config import mysql

mysql = mysql
cursor = mysql.cursor(dictionary=True)


def create_insert_trigger(file_name, table_name):
    trigger_name = f'{table_name}_after_insert'
    cursor.execute(f'''
        CREATE TRIGGER `{trigger_name}` AFTER INSERT ON `{table_name}` FOR EACH ROW BEGIN
        INSERT INTO recents(file_name, folder_name, date_time)
            VALUES('{file_name}', '{table_name}', CURRENT_TIMESTAMP());
        END
    ''')
    mysql.commit()


def create_delete_trigger(file_name, table_name):
    trigger_name = f'{table_name}_after_delete'
    cursor.execute(f'''
        CREATE TRIGGER `{trigger_name}` AFTER DELETE ON `{table_name}` FOR EACH ROW BEGIN
        INSERT INTO recents(file_name, folder_name, date_time)
            VALUES('{file_name}', '{table_name}', CURRENT_TIMESTAMP());
        END
    ''')
    mysql.commit()


def create_update_trigger(file_name, table_name):
    trigger_name = f'{table_name}_after_update'
    cursor.execute(f'''
        CREATE TRIGGER `{trigger_name}` AFTER UPDATE ON `{table_name}` FOR EACH ROW BEGIN
        INSERT INTO recents(file_name, folder_name, date_time)
            VALUES('{file_name}', '{table_name}', CURRENT_TIMESTAMP());
        END
    ''')
    mysql.commit()


def create_alter_trigger(file_name, table_name):
    trigger_name = f'{table_name}_after_alter'
    cursor.execute(f'''
        CREATE TRIGGER `{trigger_name}` AFTER ALTER ON `{table_name}` FOR EACH ROW BEGIN
        INSERT INTO recents(file_name, folder_name, date_time)
            VALUES('{file_name}', '{table_name}', CURRENT_TIMESTAMP());
        END
    ''')
    mysql.commit()
