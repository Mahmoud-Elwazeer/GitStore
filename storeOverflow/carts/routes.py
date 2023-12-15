from flask import render_template, url_for, request, flash, redirect, current_app, session
from storeOverflow import app, db, photos
from storeOverflow.products.modules import Product


def mergeDict(dict_1, dict_2):
    if isinstance(dict_1, list) and isinstance(dict_2, list):
        return dict_1 + dict_2
    elif isinstance(dict_1, dict) and isinstance(dict_2, dict):
        return dict(list(dict_1.items()) + list(dict_2.items()))
    else:
        return None

@app.route('/addtocart', methods=['POST'])
def addtocart():
    try:
        product_id = request.form.get("product_id")
        color = request.form.get("colors")
        quantity = request.form.get("quantity")
        size = request.form.get("size")
        product  = Product.query.filter_by(id=product_id).first_or_404()

        if request.method == "POST":
            productsDict = {product_id: {
                'name': product.name,
                'price': float(product.price),
                'size': size, 'quantity': int(quantity), 'color': color,
                'discount': product.discount,
                'image': product.image_1,
                'colors': product.color,
                'sizes': product.size
            }}
            if 'ShooppingCart' in session:
                if product_id in session['ShooppingCart']:
                    print('here')
                    for key, value in session['ShooppingCart'].items():
                        if key == product_id:
                            session.modified = True
                            value['quantity'] =  int(value['quantity']) + 1
                else:
                    session['ShooppingCart'] = mergeDict(session['ShooppingCart'], productsDict)
                    return redirect(request.referrer)
            else:
                session['ShooppingCart'] = productsDict
                return redirect(request.referrer)
    except Exception as e:
        flash (e, 'danger')
    finally:
        return redirect(request.referrer)


@app.route('/getcart', methods=['GET', 'POST'])
def getcart():
    if 'ShooppingCart' not in session:
        return redirect(url_for('home'))
    total = 0
    for key, value in session['ShooppingCart'].items():
        new_price = value['price'] - (value['discount'] / 100.0 )* value['price']
        sub_total = new_price * int(value['quantity'])
        total += sub_total

    return render_template('products/cart.html', total=total)



@app.route('/clearcart')
def clearcart():
    try:
        session.pop('ShooppingCart', None)
        return redirect(url_for('home'))
    except Exception as e:
        flash (e, 'danger')