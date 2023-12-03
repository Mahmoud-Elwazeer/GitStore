from storeOverflow import db, app, photos
from .modules import AddCategory, AddProduct
from flask import render_template, url_for, request, flash, redirect
from .forms import ProductForm
import secrets


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get('category')
        category = AddCategory(name=getcat)
        db.session.add(category)
        flash(f'category {getcat} added', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addcat.html', title='Add Category')


@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    form = ProductForm()
    categories = AddCategory.query.all()
    if request.form == 'POST':
        name = form.name.data
        color = form.color.data
        size = form.size.data
        price = form.price.data

        get_category = request.form.get('categories')

        stock = form.stock.data
        discount = form.discount.data
        decription = form.decription.data
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        addproduct = AddProduct(name=name, color=color, size=size, price=price,
                    category=get_category, stock=stock, discount=discount,
                    decription=decription, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addproduct)
        db.session.commit()
        return redirect(url_for('addproduct'))

    return render_template('products/addproduct.html')
