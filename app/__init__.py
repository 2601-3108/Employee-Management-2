# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 

app = Flask(__name__ , static_url_path='/static')
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace 'your_secret_key_here' with a long and random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
# db.init_app(app)

db = SQLAlchemy(app)

from app import routes