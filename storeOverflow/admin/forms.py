from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    # firstname = StringField('First Name',
    #                        validators=[DataRequired(), Length(min=2, max=20)])
    # lastname = StringField('Last Name',
    #                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])




