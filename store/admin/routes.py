#!/usr/bin/python3
""" import modules"""
from store import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, session
from .forms import RegistrationForm
from .models import User
import os


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    print(request.method)
    print(request.form)
    print(form.validate())
    print(form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit():
        print("Form submitted successfully")
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,
                    username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registeration Page")

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     print(form.validate())
#     print(form.validate_on_submit())
#     if form.validate_on_submit():
#         print(request.form)
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         with app.app_context():
#             db.create_all()
#             user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#             db.session.add(user)
#             db.session.commit()
#         flash('Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('home'))
#     return render_template('admin/register.html', title='Register', form=form)