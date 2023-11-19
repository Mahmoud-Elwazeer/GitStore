#!/usr/bin/python3
""" import modules"""

from store import app

@app.route('/')
def home():
    return "Home Page"

