from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
app.config['SECRET_KEY'] = '1b1bdc96eb8dba64b0fc5ae1'
db = SQLAlchemy(app)

from restaurant import routes 
