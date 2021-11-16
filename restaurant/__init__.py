from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
app.config['SECRET_KEY'] = '1b1bdc96eb8dba64b0fc5ae1'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from restaurant import routes 
