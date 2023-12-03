from storeOverflow import db , app
from .modules import AddCategory
from flask import render_template, url_for, request


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if (request.method = "POST"):
         
    return (render_template('products/addcat.html'))