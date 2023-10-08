from flask import Flask
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__, static_folder='static')

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')


app.config['MYSQL_HOST'] = host
app.config["MYSQL_USER"] = user
app.config["MYSQL_PASSWORD"] = password
app.config["MYSQL_DB"] = database


mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)
