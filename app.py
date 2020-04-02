from flask import Flask, jsonify, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from parser import Parser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Product
import models


app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = 'mysql//root:password@localhost/landmarkDB'
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/get_products', methods=['GET'])
def get_products():
    """
    shows all the products
    :return: all the products
    """
    products = db.select([Product]).order_by(db.desc(Product.columns.updated))
    return render_template("get_product.html", products=products)


@app.route('/get_products', methods=['GET', 'POST'])
def search():
    """
    TODO -
    Haven't had time to finish this one but the plan was to have a small form (text area + submit button), once
    submit button is pressed, the following query is sent
    :return: the search page
    """
    Product.query.filter_by(name="user input")
    return render_template("get_product.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    the file must be named "product.json and replace the previous one.
    :return: the upload page
    """
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
    models.Product.query.delete()
    p = Parser()
    product_list = p.parse(p, filename="product.json")
    for prod in p.add_product(p, product_list):
        db.session.add(prod)
    return render_template('upload.html', title='Upload a file')


if __name__ == '__main__':
    app.run()
