from array import array
from click import open_file
from app import app
import os
from flask import render_template, request
from tools.CeneoScraper.scraper import scraper

@app.route('/', methods=['POST', 'GET'])
def index():
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    # The reloader has already run - do what you want to do here

        if request.method == 'GET':
            dirs = []
            for filename in os.listdir("./opinions/"):
                dirs.append(filename.split(".")[0])
            return render_template("index.html.jinja", products=dirs)
        else:
            scraper(str(request.form.get('id')))
            # print(request.form.get('id'))
            dirs = []
            for filename in os.listdir("./opinions/"):
                dirs.append(filename.split(".")[0])
            return render_template("index.html.jinja", products=dirs, addinfo = "OK")

@app.route('/author')
def author():
    name = "Danylo Kolisnichenko"
    field = "Applied Informatics"
    group = "ZZIAS1-1211"
    return render_template("author.html.jinja", name=name, field=field, group=group)

@app.route('/opinions/<name>')
def opinions(name):
    with open(f"./opinions/{name}", "r") as f :
        content = f.read()
        f.close()
    return render_template("base.html.jinja", content = content, name = name.split(".")[0])