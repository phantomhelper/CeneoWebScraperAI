from app import app
from flask import render_template

@app.route('/')
def index():
    name = "Danylo Kolisnichenko"
    return render_template("index.html.jinja", name=name)

@app.route('/author')
def author():
    name = "Danylo Kolisnichenko"
    field = "Applied Informatics"
    group = "ZZIAS1-1211"
    return render_template("author.html.jinja", name=name, field=field, group=group)