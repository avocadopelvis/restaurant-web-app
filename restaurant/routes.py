from restaurant import app
from flask import render_template, redirect, url_for, flash, request
from restaurant.models import Table, User
from restaurant.forms import RegisterForm, LoginForm, OrderIDForm, ReserveForm
from restaurant import db
from flask_login import login_user, logout_user, login_required, current_user

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
@app.route('/table', methods = ['GET', 'POST'])
# @login_required
def table_page():
    reserve_form = ReserveForm()
    #to get rid of 'confirm form resubmission' on refresh
    if request.method == 'POST':
        reserved_table = request.form.get('reserved_table')
        r_table_object = Table.query.filter_by(table = reserved_table).first()
        if r_table_object:
            # r_table_object.owner = current_user.id #set the owner of the table to the current logged in user
            # db.session.commit()
            r_table_object.assign_ownership(current_user) #set the owner of the table to the current logged in user
            # flash(f"Your table {{ r_table_object.table }} has been reserved successfully!")

        return redirect(url_for('table_page'))

    if request.method == 'GET':
        tables = Table.query.filter_by(owner = None)
        return render_template('table.html', tables = tables, reserve_form = reserve_form)

#LOGIN PAGE
@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    forml = LoginForm()
    form = RegisterForm()
    if forml.validate_on_submit():
        attempted_user = User.query.filter_by(username = forml.username.data).first() #get username data entered from sign in form
        if attempted_user and attempted_user.check_password_correction(attempted_password = forml.password.data): #to check if username & password entered is in user database
            login_user(attempted_user) #checks if user is registered 
            flash(f'Signed in successfully as: {attempted_user.username}', category = 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Username or password is incorrect! Please Try Again', category = 'danger') #displayed in case user is not registered
    return render_template('login.html', forml = forml, form = form)

#LOGOUT FUNCTIONALITY
@app.route('/logout')
def logout():
    logout_user() #used to log out
    flash('You have been logged out!', category = 'info')
    return redirect(url_for("home_page")) 

#REGISTER PAGE
@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    forml = LoginForm()
    form = RegisterForm() 
    #checks if form is valid
    if form.validate_on_submit():
         user_to_create = User(username = form.username.data,
                               email_address = form.email_address.data,
                               password = form.password1.data)
         db.session.add(user_to_create)
         db.session.commit()
         login_user(user_to_create) #login the user on registration 
         return redirect(url_for('home_page'))
    if form.errors != {}: #if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}')
    return render_template('login.html', form = form, forml = forml)

#DELIVERY TRACKING
@app.route('/track')
def track_page():
    orderid = OrderIDForm()
    return render_template('order-id.html', orderid = orderid)

