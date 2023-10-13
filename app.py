from config import mysql, app
from route import route


cursor = mysql.cursor(dictionary=True)

# Create a sample table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS sample_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
mysql.commit()

route()


if __name__ == '__main__':
    app.run(debug=True, port=5001)
