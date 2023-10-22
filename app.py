from config import mysql, app
from route import route


cursor = mysql.cursor(dictionary=True)

route()


if __name__ == '__main__':
    app.run(debug=True, port=5001)
