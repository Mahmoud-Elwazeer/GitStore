from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .modules import User

class RegistrationForm(Form):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    firstname = StringField('First Name',
                            validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last Name')
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                            validators.EqualTo('confirm_password', message='Passwords must match'
                            )])
    confirm_password = PasswordField('Confirm Password')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    

class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me')
    # submit = SubmitField('Login')