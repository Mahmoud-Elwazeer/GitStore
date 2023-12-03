from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField
from wtfform import TextAreaField, validators, SubmitField, FloatField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Products(Form):
    name = StringField('Name', validators=[DataRequired()])
    color = StringField('Colros', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    discount = IntegerField('Discount', validators=[DataRequired()])
    decription = TextAreaField('Description', validators=[DataRequired()])
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png', 'gif', 'jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png', 'gif', 'jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[FileAllowed(
        ['jpg', 'png', 'gif', 'jpeg']), 'Images only please'])
