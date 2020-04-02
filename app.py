from flask import Flask, jsonify, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from parser import Parser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from models import Product
import models


app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql//root:password@localhost/landmark'
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


"""
shows all the products
"""
@app.route('/get_products', methods=['GET'])
def get_products():
    products = db.select([Product]).order_by(db.desc(Product.columns.updated))
    return render_template("get_product.html", products=products)


@app.route('/get_products', methods=['GET', 'POST'])
def search():
    return


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    models.Product.query.delete()
    p = Parser()
    product_list = p.parse(p, filename="product.json")
    for prod in p.add_product(p, product_list):
        db.session.add(prod)
    return render_template('upload.html', title='Home')


if __name__ == '__main__':
    app.run()
