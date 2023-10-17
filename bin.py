from config import mysql
from flask import render_template, request

mysql = mysql
cursor = mysql.cursor(dictionary=True)

