from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://moharm:pass15420@localhost/gitstore_db'
# app.config["SQLALCHEMY_DATABASE_URI"] = \
#     "mysql+mysqldb://store_dev:store_dev_pwd@localhost/store_dev_db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://moharm:root@15420@localhost/gitstore_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from storeOverflow.admin import routes
from storeOverflow.products import routes
