from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_msearch import Search


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,  instance_relative_config=True)



app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://moharm:pass15420@localhost/gitstore_db'
# app.config["SQLALCHEMY_DATABASE_URI"] = \
#     "mysql+mysqldb://store_dev:store_dev_pwd@localhost/store_dev_db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://moharm:root@15420@localhost/gitstore_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

from storeOverflow.admin import routes
from storeOverflow.products import routes
from storeOverflow.carts import routes

