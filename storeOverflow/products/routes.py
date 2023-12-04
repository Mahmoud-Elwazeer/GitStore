from flask import render_template, url_for, request, flash, redirect
from storeOverflow import app, db, photos
from .modules import Category, Product
from .forms import ProductForm
import secrets


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        flash(f'category {getcat} added', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addcat.html', title='Add Category')


@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    form = ProductForm(request.form)
    categories = Category.query.all()
    if request.method == 'POST' and 'image_1' in request.files and\
        'image_2' in request.files and 'image_3' in request.files:
        # print("I am In")
        name = form.name.data
        color = form.color.data
        size = form.size.data
        price = form.price.data

        get_category = request.form.get('category')

        stock = form.stock.data
        discount = form.discount.data
        decription = form.decription.data
        image_1 = photos.save(request.files.get(
            'image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get(
            'image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get(
            'image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Product(name=name, color=color, size=size, price=price,
                                category=Category(name=get_category), stock=stock, discount=discount,
                                description=decription, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addproduct)
        db.session.commit()
        return redirect(url_for('addproduct'))

    return render_template('products/addproduct.html', form=form, categories=categories)
