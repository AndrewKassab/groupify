import os
import json
import datetime
import psycopg2
from flask import Flask, request, flash, url_for, redirect, render_template

from .models import db
from db import config
import yaml

app = Flask(__name__)

user = os.environ('DB_USER')
password = os.environ('DB_PASS')
host = os.environ('DB_HOST')
port = os.environ('DB_PORT')
database = f'groupify_{os.environ('FLASK_ENV')}'

DATABASE_URI = f'postgres+psychpg2://{user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

con = psycopg2.connect(
    dbname="Database name",
    user=user,
    password=password,
)

# cursor
cur = con.cursor()

cur.close()

# close the connection
con.close()
