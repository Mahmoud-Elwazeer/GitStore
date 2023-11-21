## Filenname: app.py

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"



class DataForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    gender = SelectField("Gender", validators=None, choices=[(1, 'M'), (2, "F")])
    submit = SubmitField("Submit", validators=None)



@app.route('/index', methods=["GET", "POST"])
def index():
    form = DataForm(request.form)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.validate())
        print(form.name)
        flash("THIS IS FLASH")
        title="hello"
        return redirect(url_for('output'))
    return render_template('index.html', form=form)



@app.route('/output', methods=["GET", "POST"])
def output():
    title = "hello"
    form = DataForm()
    print(form.validate())
    return render_template('output.html', title=title)


app.run(debug=False)