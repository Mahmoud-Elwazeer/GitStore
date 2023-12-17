from storeOverflow import app, db
from flask import redirect, render_template, url_for, session, request
from flask_login import current_user, login_required
import secrets
from .modules import Orders
import stripe



puplishable_key = ''
stripe.api_key = ''


@login_required
@app.route('/payment', methods=['POST'])
def payment():
    bill = request.form.get('bill')
    total_amount = request.form.get('total')

    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken'],
    )


    charge = stripe.Charge.create(
      customer=customer.id,
      description='GitStore',
      amount=total_amount,
      currency='gbp',
    )

    order = Orders.query.filter_by(user_id=current_user.id, bill=bill).first()
    order.status = 'paid'
    db.session.commit()
    if order.status == 'paid':
        return redirect(url_for('thanks'))
    else:
        return redirect(url_for('payment_fail'))


@app.route('/thanks')
def thanks():
    return '<h1>Thanks</h1>'


@app.route('/payment_fail')
def payment_fail():
    return '<h1>Failed</h1>'


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
    grand_total = 0
    for key, value in orders.orders.items():
        discount = (value['discount'] / 100.0) * value['price']
        price_qty = float(value['price']) - discount
        sub_total = price_qty * int(value['quantity'])
        total += sub_total
        grand_total = ("%0.2f" % float(total))
    
    return render_template('products/checkout.html', orders=orders, 
                           total=total, grand_total=grand_total)



