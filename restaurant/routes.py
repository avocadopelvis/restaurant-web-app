from restaurant import app
from flask import render_template
from restaurant.models import Table

@app.route('/')
#HOME PAGE
@app.route('/home')
def home_page():
    return render_template('index.html')

#MENU PAGE
@app.route('/menu')
def menu_page():
    return render_template('menu.html')

#TABLE RESERVATION PAGE
@app.route('/table')
def table_page():
    tables = Table.query.all()
    return render_template('table.html', tables = tables)

#LOGIN AND REGISTER PAGE
@app.route('/login')
def login_page():
    return render_template('login.html')