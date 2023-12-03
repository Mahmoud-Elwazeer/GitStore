from storeOverflow import app, db


class AddCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class AddProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    size = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('add_category.id'), nullable=False)
    category = db.relationship('AddCategory', backref=db.backref('categories', lazy=True))

    stock = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text, nullable=False)

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')


with app.app_context():
    db.create_all()
