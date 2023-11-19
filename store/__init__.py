#!/usr/bin/python3
""" import modules"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)
# configure the MySql database
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "mysql+mysqldb://store_dev:store_dev_pwd@localhost/store_dev_db"

db = SQLAlchemy(app)


from store.admin import routes
