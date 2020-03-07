from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# nothing but the secret key to encrypt the cookies
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abb9614f40e5f6521adb623714cdfc9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)

from blog import routes