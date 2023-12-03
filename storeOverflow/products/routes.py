from storeOverflow import db, app
from .modules import AddCategory
from flask import render_template, url_for, request, flash, redirect


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
    return render_template('products/addproduct.html')
