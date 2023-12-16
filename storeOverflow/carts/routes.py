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
        quantity = int(request.form.get("quantity"))
        size = request.form.get("size")
        product  = Product.query.filter_by(id=product_id).first_or_404()

        if request.method == "POST":
            productsDict = {product_id: {
                'name': product.name,
                'price': float(product.price),
                'size': size,
                'quantity': quantity,
                'color': color,
                'discount': product.discount,
                'image': product.image_1,
                'colors': product.color,
                'sizes': product.size
            }}
            if 'ShooppingCart' in session:
                if product_id in session['ShooppingCart']:
                    print('here11')
                    for key, value in session['ShooppingCart'].items():
                        print('here222')
                        if int(key) == int(product_id):
                            print('here222')
                            print(type(quantity), type(key), type(product_id))
                            session.modified = True
                            value['quantity'] += 1
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
    total = float(0)
    for key, value in session['ShooppingCart'].items():
        new_price = float( value['price']) - float((value['discount'] / 100.0 )) * float(value['price'])
        sub_total = float(new_price) * int(value['quantity'])
        total += float(sub_total)

    return render_template('products/cart.html', total=total)



@app.route('/clearcart')
def clearcart():
    try:
        session.pop('ShooppingCart', None)
        return redirect(url_for('home'))
    except Exception as e:
        flash (e, 'danger')


@app.route('/updatecart/<int:id>', methods=["POST"])
def updatecart(id):
    if 'ShooppingCart' not in session:
        return redirect(url_for('home'))

    color = request.form.get("colors")
    quantity = int(request.form.get("quantity"))
    size = request.form.get("size")
    try:
        session.modified = True
        session['ShooppingCart'].get(str(id))['quantity'] = quantity
        session['ShooppingCart'].get(str(id))['color'] = color
        session['ShooppingCart'].get(str(id))['size'] = size
        # print(type(session['ShooppingCart'].get(str(id))['color']))
        # print(type(session['ShooppingCart'].get(str(id))['quantity']))
        
    except Exception as e:
        flash(e, 'danger')
    return redirect(url_for('getcart'))


@app.route('/removecart/<int:id>', methods=["POST"])
def removecart(id):
    if 'ShooppingCart' not in session:
        return redirect(url_for('home'))
    try:
        session.modified = True
        session['ShooppingCart'].pop(str(id), None)
    
    except Exception as e:
        flash(e, 'danger')
    return redirect(url_for('getcart'))