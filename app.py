from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "user_list"

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'], 
    user=app.config['MYSQL_USER'], 
    password=app.config['MYSQL_PASSWORD'], 
    database=app.config['MYSQL_DB']
)
cursor = mysql.cursor(dictionary=True)

# Create a sample table
cursor.execute("CREATE TABLE IF NOT EXISTS sample_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
mysql.commit()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM sample_table")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    name = request.form['field']
    value = request.form['value']
    cursor.execute(f"UPDATE sample_table SET {name}=%s WHERE id=%s", (value, id))
    mysql.commit()
    return "success"

@app.route('/insert', methods=['POST'])
def insert():
    new_name = request.form['new_name']
    new_age = request.form['new_age']
    cursor.execute("INSERT INTO sample_table (name, age) VALUES (%s, %s)", (new_name, new_age))
    mysql.commit()
    return "success"

@app.route('/newCol', methods=['POST'])
def newCol():
    new_column_name = request.form['new_column_name']
    new_column_type = request.form['new_column_type']
    cursor.execute(f"ALTER TABLE sample_table ADD {new_column_name} {new_column_type}")
    mysql.commit()
    return "success"

@app.route('/dropCol', methods=['POST'])
def dropCol():
    col_name = request.form['column_name']
    cursor.execute(f"ALTER TABLE sample_table DROP COLUMN {col_name}")
    mysql.commit()
    return "success"

@app.route('/dropRow', methods=['POST'])
def dropRow():
    rowid = request.form['rowid']
    cursor.execute(f"DELETE FROM sample_table WHERE id={rowid}")
    mysql.commit()
    return "success"

# not done
@app.route('/editRow/<int:id>', methods=['POST'])
def editRow(id):
    name = request.form['field']
    value = request.form['value']
    cursor.execute(f"UPDATE sample_table SET {name}=%s WHERE id=%s", (value, id))
    mysql.commit()
    return "success"

# not work
@app.route('/filter/<int:value>',  methods=['GET'])
def compire(value):

    cursor.execute(f"SELECT * FROM sample_table LIMIT 3")
    cursor.fetchall()
    
    print('-----------')
    print(value)
    return "success"

if __name__ == '__main__':
    app.run(debug=True)
