from storeOverflow import app, db
from datetime import datetime
import json

class JsonEncodeDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)
        
    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)



class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=False)
    status = db.Column(db.String(20), default='Pending', nullable=False)

    bill = db.Column(db.String(50), nullable=False, unique=True)

    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    orders = db.Column(JsonEncodeDict)


with app.app_context():
    db.create_all()



