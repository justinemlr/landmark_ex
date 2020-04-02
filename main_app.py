from app import app, db
from models import Product


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Product': Product}