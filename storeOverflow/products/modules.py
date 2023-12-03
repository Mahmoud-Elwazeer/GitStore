from storeOverflow import app, db


class AddCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)


with app.app_context():
    db.create_all()