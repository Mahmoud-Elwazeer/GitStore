from storeOverflow import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
# from .forms import RegistrationForm
# from storeOverflow.admin.forms import RegistrationForm
from .forms import RegistrationForm
from .modules import User


@app.route("/")
@app.route("/home")
@app.route("/Home")
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('admin/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    print(form.validate())
    print(form.errors)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form)
