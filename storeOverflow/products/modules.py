from storeOverflow import app, db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    color = db.Column(db.String(200), nullable=False, unique=False)
    size = db.Column(db.String(30), nullable=False, unique=False)
    price = db.Column(db.Numeric(10, 2), nullable=False, unique=False)

    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)
    category = db.relationship(
        'Category', backref=db.backref('categories', lazy=True))

    stock = db.Column(db.Integer, nullable=False, unique=False)
    discount = db.Column(db.Integer, nullable=False, default=0, unique=False)
    description = db.Column(db.Text, nullable=False, unique=False)

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')


with app.app_context():
    db.create_all()
