import os
import jwt
import datetime
from sqlalchemy import exc
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from werkzeug.security import check_password_hash, generate_password_hash

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "appsecret"

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# PORT
# port = int(os.environ.get('PORT', 5000))

# Product Class/Model


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# User Schema


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    isAdmin = db.Column('version', db.Boolean, default=False)

    def __init__(self, name, username, email, password, isAdmin):
        self.name = name
        self.username = username
        self.email = email
        self.isAdmin = isAdmin
        self.password = generate_password_hash(password, method='sha256')
# User Schema


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'username', 'email', 'password', 'isAdmin')


# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Token Middleware


def requires_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({
                'success': False,
                'message': 'Unauthorized'
            }), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(
                id=data['user']['id']).first()
        except:
            return jsonify({
                'success': False,
                'message': 'Invalid Token'
            }), 401

        if current_user:
            if current_user.isAdmin:
                return f(current_user, *args, **kwargs)
            else:
                return jsonify({
                    'success': False,
                    'message': 'Unauthorized'
                }), 401
        else:
            return jsonify({
                'success': False,
                'message': 'User not found.'
            }), 401

    return decorated

# Index Route


@app.route('/', methods=['GET'])
def index():
    return '<h1>Vue Heroku Application</h1>'

# Register User


@app.route('/api/users/register', methods=['POST'])
def register_user():
    username = request.json['username']
    if check_unique_username_email(username, 'username'):
        email = request.json['email']
        if check_unique_username_email(email, 'email'):
            name = request.json['name']
            password = request.json['password']
            isAdmin = request.json['isAdmin']
            new_user = User(name, username, email, password, isAdmin)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"success": True, "message": "You are Registred Successfully"})
        else:
            return jsonify({"success": False, "message": "Email is already registered. Did you forget your password."})
    else:
        return jsonify({"success": False, "message": "Username taken please try with another one."})

# Login User


@app.route('/api/users/login', methods=['POST'])
def login_user():
    username = request.json['username']
    password = request.json['password']
    print(username, password)
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'success': False, "message": "Username not found."})
    else:
        if check_password_hash(user.password, password):
            token = jwt.encode({
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=60),
                'iat': datetime.datetime.utcnow()
            }, app.config['SECRET_KEY'])
            return jsonify({'success': True, "token": token.decode('UTF-8'), 'message': "Hurray login is successful"})
        else:
            return jsonify({'success': False, 'message': "Incorrect password."})

# User Functions


def check_unique_username_email(value, field):
    if field == 'username':
        user = User.query.filter_by(username=value).first()
    elif field == 'email':
        user = User.query.filter_by(email=value).first()
    if user:
        return False
    else:
        return True


def get_user_by_email_or_username(value):
    user = User.query.filter_by(username=value).first()
    if user:
        return user
    else:
        return None

# Product Functions


def check_if_product_exists(name):
    product = Product.query.filter_by(name=name).first()
    if product:
        return False
    else:
        return True


@app.route('/api/product', methods=['POST'])
@requires_admin
def add_product(current_user):
    name = request.json['name']
    if check_if_product_exists(name):
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']

        new_product = Product(name, description, price, qty)
        db.session.add(new_product)
        db.session.commit()
        product = {
            "description": new_product.description,
            "id": new_product.id,
            "name": new_product.name,
            "price": new_product.price,
            "qty": new_product.qty
        }
        return jsonify({'success': True, 'message': "Product added successfully", 'product': product})
    else:
        return jsonify({'success': False, 'message': "Product with this name already exists. Try with other name."})


# Get All Products


@app.route('/api/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Get Single Products


@app.route('/api/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return jsonify(product)
    else:
        return jsonify({
            'success': False,
            'message': "Product not found",
        })


# Update a Product


@app.route('/api/product/<id>', methods=['PUT'])
@requires_admin
def update_product(current_user, id):
    product = Product.query.get(id)
    if product:
        product.name = request.json['name']
        product.description = request.json['description']
        product.price = request.json['price']
        product.qty = request.json['qty']
        db.session.commit()
        return jsonify({
            'success': True,
            'message': "Product updated successfully",
            'product': product
        })
    else:
        return products_schema.jsonify({
            'success': False,
            'message': "Product does not exist."
        })


# Delete Product


@app.route('/api/product/<id>', methods=['DELETE'])
@requires_admin
def delete_product(current_user, id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': "Product deleted successfully.",
            'product': product
        })
    else:
        return jsonify({
            'success': False,
            'message': "Product does not exist."
        })


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
