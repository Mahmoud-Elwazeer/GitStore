#!/usr/bin/python3
""" import modules"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


# class RegistrationForm(FlaskForm):
#     name = StringField('Name',
#                         validators=[DataRequired(), Length(min=2, max=50)])
#     username = StringField('Username',
#                         validators=[DataRequired(), Length(min=2, max=50)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('New Password', [
#         DataRequired(),
#         EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     # photo = FileField('Photo')
#     # submit = SubmitField('Sign Up')



# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('Name',
                    validators=[DataRequired(), Length(min=2, max=50)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')