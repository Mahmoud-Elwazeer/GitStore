from storeOverflow import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
# from .forms import RegistrationForm
# from storeOverflow.admin.forms import RegistrationForm
from .forms import RegistrationForm, LoginForm
from .modules import User


@app.route("/")
@app.route("/home")
@app.route("/Home")
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('welcom {} Thanks for registering', 'success'.format(form.username.data))
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title='Regestration')


@app.route('/login', methods=['GET', 'POST'])
@app.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(form.data)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Welcom {} You are now logged in', 'success'.format(form.email.data))
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    # print(user)
    # return 'login form'
    return render_template('admin/login.html', form=form, title='Login')