from storeOverflow import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
# from .forms import RegistrationForm
# from storeOverflow.admin.forms import RegistrationForm
from .forms import RegistrationForm



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
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form)