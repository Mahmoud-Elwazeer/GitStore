from flask import render_template, url_for, request, flash, redirect, current_app
from storeOverflow import app, db, photos, search
from .modules import Category, Product
from .forms import ProductForm
import secrets
import os



@app.route('/hoodies')
def hoodies():
    page = request.args.get('page', 1, type=int)
    get_cat_hoodies = Category.query.filter_by(name='Hoodies').first_or_404()
    hoodies = Product.query.filter(Product.stock > 0, Product.category_id==get_cat_hoodies.id).order_by(Product.id.desc()).paginate(page=page, per_page=4)
    return (render_template('products/hoodies.html', hoodies=hoodies))



@app.route('/mugs')
def mugs():
    page = request.args.get('page', 1, type=int)
    get_cat_mugs = Category.query.filter_by(name='Mugs').first_or_404()
    mugs = Product.query.filter(Product.stock > 0, Product.category_id==get_cat_mugs.id).order_by(Product.id.desc()).paginate(page=page, per_page=4)
    return (render_template('products/mugs.html', mugs=mugs))


@app.route('/tshirts')
def tshirts():
    # tshirts = Category.query.filter_by(name=name).first_or_404()
    page = request.args.get('page', 1, type=int)
    products = Category.query.filter_by(name='T-shirts').first_or_404()
    tshirts = Product.query.filter(Product.stock > 0, Product.category_id == products.id).paginate(page=page, per_page=4)
    # print(product)
    return render_template('products/tshirts.html', tshirts=tshirts)

@app.route('/product/<int:id>')
def single_page(id):
    product = Product.query.get_or_404(id)
    related_products = Product.query.filter(Product.stock > 0, Product.category_id == product.category_id).order_by(Product.id.desc())

    return render_template('products/product.html', product=product, related_products=related_products[:4])


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

@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    category = Category.query.get_or_404(id)
    newcat = request.form.get('category')
    if request.method == 'POST':
        category.name = newcat
        db.session.commit()
        return (redirect(url_for('categories')))
    return render_template('products/updatecat.html', title='Add Category', category=category)

@app.route('/deletecat/<int:id>', methods=['POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        if category:
            db.session.query(Product).\
                filter_by(category=category).\
                delete(synchronize_session=False)
        db.session.delete(category)
        flash(f"The brand {category.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('categories'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('categories'))

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
        description = form.description.data
        image_1 = photos.save(request.files.get(
            'image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get(
            'image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get(
            'image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Product(name=name, color=color, size=size, price=price,
                             category_id=get_category, stock=stock, discount=discount,
                             description=description, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addproduct)
        db.session.commit()
        return redirect(url_for('products_list'))

    return render_template('products/addproduct.html', form=form, categories=categories)


@app.route('/updateproduct/<int:product_id>', methods=['GET', 'POST'])
def updateproduct(product_id):
    form = ProductForm(request.form)
    product = Product.query.get_or_404(product_id)
    categories = Category.query.all()
    category = request.form.get('category')

    if request.method == "POST":
        product.name = form.name.data
        product.color = form.color.data
        product.size = form.size.data
        product.price = form.price.data
        product.category_id = category
        product.stock = form.stock.data
        product.discount = form.discount.data
        product.description = form.description.data

        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path,
                          "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'),
                                              name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'),
                                              name=secrets.token_hex(10) + ".")
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path,
                          "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'),
                                              name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'),
                                              name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path,
                          "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'),
                                              name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'),
                                              name=secrets.token_hex(10) + ".")

        flash(f'product {form.name.data} updated successfuly', 'success')
        db.session.commit()
        return redirect(url_for('products_list'))

    form.name.data = product.name
    form.color.data = product.color
    form.size.data = product.size
    form.price.data = product.price
    category = product.category.name
    form.stock.data = product.stock
    form.discount.data = product.discount
    form.description.data = product.description

    return render_template('products/addproduct.html', form=form,
                           product=product, categories=categories)


@app.route('/deleteproduct/<int:product_id>', methods=['GET', 'POST'])
def deleteproduct(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        try:
            os.unlink(os.path.join(current_app.root_path,
                                   "static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path,
                                   "static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path,
                                   "static/images/" + product.image_3))
        except Exception as e:
            flash(e, 'danger')
        db.session.delete(product)
        db.session.commit()
        flash(f'the product {product.name} deleted successfuly', 'success')
        return redirect(url_for('products_list'))
    flash(f"the product {product.name} can't be deleted", 'success')

    return redirect(url_for('products_list'))


@app.route('/result')
def result():
    search_word = request.args.get('q')
    result = Product.query.msearch(search_word, fields=['name', 'description'], limit=3)
    return render_template ('products/result.html', result=result)