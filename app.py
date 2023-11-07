from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        name = db.Column(db.String, nullable=False, unique=True)
        description = db.Column(db.String, nullable=False)
        price = db.Column(db.String, nullable=False)
        category = db.Column(db.String, nullable=False)
        image = db.Column(db.String, unique=True)
        
        def __init__(self, name, description, price, category, image):
            self.name = name
            self.description = description
            self.price = price
            self.category = category
            self.image = image

class ProductSchema(ma.Schema):
        class Meta:
            fields = ('id', 'name', 'description', 'price', 'category', 'image')

product_schema = ProductSchema()
multi_product_schema = ProductSchema(many=True)

@app.route('/')
def hello_world():
    return 'David s Devcamp Backend!'

# **** Add Product EndPoint ****
@app.route('/product/add', methods=["POST"])
def add_product():
    if request.content_type != 'application/json':
        return jsonify('Error: Data must be sent as JSON')
    
    post_data = request.get_json()
    name = post_data.get('name')
    description = post_data.get('description')
    price = post_data.get('price')
    category = post_data.get('category')
    image = post_data.get('image')

    if name == None:
        return jsonify("Error: Please, provide a product name.")
    if description == None:
        return jsonify("Error: Please, provide a description.")
    if price == None:
        return jsonify("Error: Please, provide the price.")
    if category == None:
        return jsonify("Error: Please, provide a category.")
    
    new_record = Product(name, description, price, category, image)
    db.session.add(new_record)
    db.session.commit()

    return jsonify(product_schema.dump(new_record))

# **** Get Product EndPoint ****
@app.route('/product/get', methods=["GET"])
def get_products():
    all_products = db.session.query(Product).all()
    return jsonify(multi_product_schema.dump(all_products))

# **** Get A Product EndPoint ****
@app.route('/product/get/<id>', methods=["GET"])
def get_product(id):
    get_product = db.session.query(Product).filter(Product.id == id).first()
    return jsonify(product_schema.dump(get_product))

# **** Edit Product EndPoint ****
@app.route('/product/edit/<id>', methods=["PUT"])
def edit_product_id(id):
    if request.content_type != 'application/json':
        return jsonify("Error: Data must be sent as JSON")
    
    put_data = request.get_json()
    name = put_data.get('name')
    description = put_data.get('description')
    price = put_data.get('price')
    category = put_data.get('category')
    image = put_data.get('image')

    edit_product_id = db.session.query(Product).filter(Product.id == id).first()

    if name != None:
        edit_product_id.name = name
    if description != None:
        edit_product_id.description = description
    if price != None:
        edit_product_id.price = price
    if category != None:
        edit_product_id.category = category
    if image != None:
        edit_product_id.image = image

    db.session.commit()
    return jsonify(product_schema.dump(edit_product_id))


# **** Delete Product EndPoint ****

@app.route('/product/delete/<id>', methods=["DELETE"])
def delete_product_id(id):
    delete_product = db.session.query(Product).filter(Product.id == id).first()
    db.session.delete(delete_product)
    db.session.commit()
    return jsonify("The product has been deleted!", product_schema.dump(delete_product))


#  **** Add Many Products EndPoint ****
@app.route('/product/add/many', methods=["POST"])
def add_many_products():
    if request.content_type != "application/json":
        return jsonify("Error: Your Data must be sent as JSON")
    
    post_data = request.get_json()
    products = post_data.get('products')

    new_products = []

    for product in products:
        name = product.get('name')
        description = product.get('description')
        price = product.get('price')
        category = product.get('category')
        image = product.get('image')

        existing_product_check = db.session.query(Product).filter(Product.name == name).first()
        if existing_product_check is None:
            new_record = Product(name, description, price, category, image)
            db.session.add(new_record)
            db.session.commit()
            new_products.append(product_schema.dump(new_record))

    return jsonify(multi_product_schema.dump(new_products))

if __name__ == "__main__":
    app.run(debug = True)