from storeOverflow import app, db
from flask import redirect, render_template, url_for, session
from flask_login import current_user, login_required
import secrets
from .modules import Orders


@app.route('/orders')
@login_required
def get_orders():
    if current_user.is_authenticated:
        try:
            bill = secrets.token_hex(5)
            user_id = current_user.id
            order = Orders(user_id=user_id, bill=bill, orders=session['ShooppingCart'])
            db.session.add(order)
            db.session.commit()
            session.pop('ShooppingCart')
            return redirect(url_for('orders', bill=bill))
        except:
            return redirect(url_for('getcart'))

@app.route('/orders/<bill>')
def orders(bill):
    user_id = current_user.id
    orders = Orders.query.filter_by(bill=bill, user_id=user_id).first()
    total = 0
    for key, value in orders.orders.items():
        discount = (value['discount'] / 100.0) * value['price']
        price_qty = float(value['price']) - discount
        sub_total = price_qty * int(value['quantity'])
        total += sub_total
    
    return render_template('products/checkout.html', orders=orders, total=total)



