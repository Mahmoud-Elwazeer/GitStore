#!/usr/bin/python3
""" import modules"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# create the app
app = Flask(__name__)
# configure the MySql database
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "mysql+mysqldb://store_dev:store_dev_pwd@localhost/store_dev_db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "dnvkdd5f51ds5c1d5sc12d1s"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from store import routes
from store.admin import routes
