from storeOverflow import app, db, bcrypt, login_manager
from flask import render_template, url_for, flash, redirect, request, session
# from .forms import RegistrationForm
# from storeOverflow.admin.forms import RegistrationForm
from .forms import RegistrationForm, LoginForm
from .modules import User
from storeOverflow.products.modules import Product, Category
from flask_login import login_user, current_user, login_required, logout_user, LoginManager


@app.route("/")
@app.route("/home")
@app.route("/Home")
def home():
    products = Product.query.order_by(Product.id.desc())
    return render_template('home.html', products=products)


@app.route('/admin')
def admin():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    # if (session['email'] == 'admin@admin.com'):
    #         return redirect(url_for('admin'))
    # else:
    #         return redirect(url_for('home'))
    products = Product.query.all()
    return render_template('admin/products.html', products=products)


@app.route('/categories')
def categories():
    categories = Category.query.order_by(Category.id).all()
    return render_template('admin/categories.html', title='Categories', categories=categories)


@app.route('/products')
def products_list():
    products = Product.query.all()
    return render_template('admin/products.html', products=products)


@login_manager.user_loader
def get_user(id):
    return User.query.get(int(id))


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
        flash(f'welcom {current_user.username} Thanks for registering',
              'success'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Regestration')


@app.route('/login', methods=['GET', 'POST'])
@app.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(form.data)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            login_user(user)
            # flash(f'Welcome {current_user.username} You are now logged in',
            #       'success'.format(form.email.data))
            if (session['email'] == 'admin@admin.com'):
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('home'))
        else:
            # flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('admin/login.html', form=form, title='Login')


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))