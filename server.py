import os
import time

from flask import Flask, render_template, request, redirect, url_for, flash, make_response, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, FloatField, IntegerField, PasswordField, RadioField, \
    BooleanField, SelectMultipleField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from datetime import date
from datetime import datetime, timedelta
import pdfkit
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

###########################################################################################################

##############################       DATABASE SETUP

########################################################################################################

# Global Variables
# gproduct_items = []

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost:3306/store'
db = SQLAlchemy(app)

############################################################################################

#####################    LOGIN  CONFIG

#############################################################################################


login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'


############################################################################

##########################     MODELS SETUP

############################################################################


@login_manager.user_loader
def load_user(user_id):
    return RegisterModel.query.get(user_id)


class RegisterModel(db.Model, UserMixin):
    __tablename__ = 'register'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))
    shop_name = db.Column(db.String(60))
    shop_type = db.Column(db.String(60))
    shop_owner_name = db.Column(db.String(60))
    shop_address = db.Column(db.String(60))
    shop_start_date = db.Column(db.String(60))

    def __init__(self, username, password, shop_name, shop_type, shop_owner_name, shop_address, shop_start_date):

        self.username = username
        self.password = password
        self.shop_name = shop_name
        self.shop_type = shop_type
        self.shop_owner_name = shop_owner_name
        self.shop_address = shop_address
        self.shop_start_date = shop_start_date

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def __repr__(self):
        return f"Username  {self.username}"


class AddProduct(db.Model, UserMixin):
    __tablename__ = 'store_data'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    product_quantity = db.Column(db.String)
    product_price = db.Column(db.String)
    product_arrival_date = db.Column(db.String)
    product_manufacture_date = db.Column(db.String)
    product_expiry_date = db.Column(db.String)

    def __init__(self, product_name, product_quantity, product_price, product_arrival_date, product_manufacture_date,
                 product_expiry_date):
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_arrival_date = product_arrival_date
        self.product_manufacture_date = product_manufacture_date
        self.product_expiry_date = product_expiry_date


#################################################################

#################        FORM SETUP

#################################################################


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={
        "placeholder": "Username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
        "placeholder": "Password"})
    shop_name = StringField("Enter Shop Name", validators=[
        DataRequired()], render_kw={"placeholder": "ENTER SHOP NAME"})
    shop_type = StringField("Enter Shop Type", validators=[
        DataRequired()], render_kw={"placeholder": "ENTER SHOP TYPE"})
    shop_owner = StringField("Enter Owner Name", validators=[
        DataRequired()], render_kw={"placeholder": "ENTER OWNER NAME"})

    shop_address = StringField("Enter Address", validators=[
        DataRequired()], render_kw={"placeholder": "ENTER SHOP ADDRESS"})
    shop_start_date = DateField(" Enter Shop startup Date", validators=[
        DataRequired()], render_kw={"placeholder": "ENTER SHOP STARTUP DATE"})

    submit = SubmitField("submit")


class LoginForm(FlaskForm):
    username = StringField("USERNAME", validators=[DataRequired()], render_kw={
        "placeholder": "ENTER YOUR USERNAME"})
    password = PasswordField("PASSWORD", validators=[DataRequired()], render_kw={
        "placeholder": "ENTER YOUR PASSWORD"})
    login = SubmitField("Login")


class update_profile(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter new username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Enter new password"})
    shop_name = StringField("Shop Name", validators=[DataRequired()], render_kw={"placeholder": "Enter new shop name"})
    shop_type = StringField("Shop Type", validators=[DataRequired()], render_kw={"placeholder": "Enter new shop type"})
    shop_owner_name = StringField("Shop Owner Name", validators=[DataRequired()],
                                  render_kw={"placeholder": "Enter new owner name"})
    shop_address = StringField("Shop Address", validators=[DataRequired()],
                               render_kw={"placeholder": "Enter new shop address"})
    shop_start_date = DateField("Shop Start Date", validators=[DataRequired()],
                                render_kw={"placeholder": "Enter shop start date"})

    submit = SubmitField("Update Profile")


#########################################################################################

#######################         ROUTE

########################################################################################


@app.route('/')
def index():
    return render_template('Index.html')


@app.route("/registration", methods=["POST", "GET"])
def registration():
    username = None
    password = None
    shop_name = None
    shop_type = None
    shop_owner = None
    shop_address = None
    shop_start_date = None

    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''

        password = form.password.data
        form.password.data = ''

        shop_name = form.shop_name.data
        form.shop_name.data = ''

        shop_type = form.shop_type.data
        form.shop_type.data = ''

        shop_owner = form.shop_owner.data
        form.shop_owner.data = ''

        shop_address = form.shop_address.data
        form.shop_address.data = ''

        shop_start_date = form.shop_start_date.data
        form.shop_start_date.data = ''


        entry = RegisterModel(username=username, password=password, shop_name=shop_name,
                              shop_type=shop_type, shop_owner_name=shop_owner, shop_address=shop_address,
                              shop_start_date=shop_start_date)

        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('registration.html', form=form, username=username, password=password, shop_name=shop_name,
                           shop_type=shop_type, shop_owner=shop_owner, shop_address=shop_address,
                           shop_start_date=shop_start_date)


@app.route('/login', methods=["POST", "GET"])
def login():
    username = None
    password = None
    form = LoginForm()

    if form.validate_on_submit():

        user = RegisterModel.query.filter_by(username=form.username.data).first()
        passw = RegisterModel.query.filter_by(password=form.password.data).first()
        print(user)
        print(passw)
        print(db.session.query(RegisterModel.password).first())
        print(form.password.data)
        a = user.check_password(form.password.data)
        print(a)

        if user.check_password(form.password.data) and user is not None:
            print("User is :")
            login_user(user)
            next = request.args.get('next')  # grab a reuest @login_required
            print(next)

            if next == None or not next[0] == "/":
                return redirect(url_for('search', posts=AddProduct.query.all()))
            else:
                return render_template('login.html', form=form, error='Invalid username or password')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def tostr(tup):
    str = ''
    for item in tup:
        str = str + item
    return str


@app.route('/profile', methods=["POST", "GET"])
@login_required
def profile():
    shop_name = db.session.query(RegisterModel.shop_name).all()
    shop_type = db.session.query(RegisterModel.shop_type).all()
    shop_owner_name = db.session.query(RegisterModel.shop_owner_name).all()
    shop_address = db.session.query(RegisterModel.shop_address).all()
    shop_start_date = db.session.query(RegisterModel.shop_start_date).all()

    return render_template('profile.html', shopn=tostr(shop_name[0]), shopt=tostr(shop_type[0]),
                           shopon=tostr(shop_owner_name[0]), shopa=tostr(shop_address[0]), shopsd=shop_start_date[0])


@app.route('/profile_update', methods=["POST", "GET"])
@login_required
def profile_update():
    form = update_profile()

    if request.method == 'POST':
        shopusername = form.username.data
        shoppassword = form.password.data
        shopname = form.shop_name.data
        shoptype = form.shop_type.data
        shopowner_name = form.shop_owner_name.data
        shopaddress = form.shop_address.data
        shopstartdate = form.shop_start_date.data

        entry = db.session.query(RegisterModel).filter(RegisterModel.id == '1').first()

        entry.username = shopusername
        entry.password = shoppassword
        entry.shop_name = shopname
        entry.shop_type = shoptype
        entry.shop_owner_name = shopowner_name
        entry.shop_address = shopaddress
        entry.shop_start_date = shopstartdate

        print("Data updated...")
        flash("Data Updated...")

        db.session.commit()

    return render_template('profile update.html', form=form)


@app.route('/add_product', methods=["POST", "GET"])
@login_required
def add_product():
    '''
      id, username, password, shop_name, shop_type, shop_owner_name,
      shop_address, shop_start_date, product_name, product_quantity,
      product_price, product_arrival_date, product_manufacture_date,
      product_expiry_date
      '''

    if request.method == 'POST':
        product_name = request.form.get('product_name')
        product_quantity = request.form.get('product_quantity')
        product_price = request.form.get('product_prize')
        product_arrival_date = request.form.get('product_arrival_date')
        product_manufacture_date = request.form.get('product_manufacture_date')
        product_expiry_date = request.form.get('product_expiry_date')

        entry = AddProduct(product_name=product_name, product_quantity=product_quantity, product_price=product_price,
                           product_arrival_date=product_arrival_date, product_manufacture_date=product_manufacture_date,
                           product_expiry_date=product_expiry_date)
        db.session.add(entry)
        db.session.commit()

        flash("Product successfully added...")
    return render_template('add product.html')


@app.route('/dls', methods=["POST", "GET"])
@login_required
def dls():
    return render_template('dls.html', posts=AddProduct.query.all())


@app.route("/generate_bill", methods=["POST"])
@login_required
def generate_bill():
    pro_name = db.session.query(AddProduct.product_name).all()

    values = []
    values = request.form.getlist('values[]')
    print(values)

    combined = zip(pro_name, values)

    # Convert the list of tuples into a dictionary
    my_dict = dict(combined)

    print(my_dict)

    filtered_dict = {key: value for key, value in my_dict.items() if value > '0'}

    print(("filtered_dict"))
    print(filtered_dict)

    productq = 0
    productn = 0
    product_q = 0
    pro_item = []
    global product_items
    product_items = []

    for pro in filtered_dict:
        print("pro is : ")
        print(pro)

        productq = int(my_dict[pro])
        productn = str(pro[0])
        print(productn)
        print(productq)

        product_data = db.session.query(AddProduct.product_quantity).filter(AddProduct.product_name == productn).first()
        productc = db.session.query(AddProduct.product_price).filter(AddProduct.product_name == productn).first()
        product_c = int(productc[0])
        product_q = int(product_data[0])

        print("Values: ")
        print(product_data)
        print(product_q)
        if productq <= product_q and productq != 0:
            print("You can purchase....")
            pro_item = [[productn, product_c, productq, productq * product_c]]
            print(pro_item)

            product_items.extend(pro_item)
            print(product_items)

            entry = db.session.query(AddProduct).filter(AddProduct.product_name == productn).first()
            print("actual quantity of a product : " + productn + "is :")
            print(entry.product_quantity)
            entry.product_quantity = int(entry.product_quantity - productq)
            db.session.commit()

        else:
            print("Insufficient product: ")
            return render_template("dls.html")

    i = 0

    total = 0
    for t in product_items:
        total += product_items[i][3]
        i = i + 1

    global gproduct_items
    gproduct_items = []
    gproduct_items.extend(product_items)

    global total_price
    total_price = total

    print("your products and total: ")
    print(gproduct_items)
    print(total_price)

    sp_name = "Shree patil oil traders, Jaysingpur"
    global today_date
    today_date = date.today()
    global now_time
    now = datetime.now()
    now_time = now.strftime("%H:%M:%S")

    global num
    num = random.randint(1000000000, 9999999999)
    print(num)

    return render_template("bill.html", sp_name=sp_name, num=num, today_date=today_date, now_time=now_time,
                           items=product_items, total=total)


@app.route('/pdf')
@login_required
def pdf():
    print("your products and total: ")
    # print(gproduct_items)
    print(total_price)
    html = render_template("pdf.html", items=gproduct_items, num=num, today_date=today_date, now_time=now_time,
                           total=total_price)
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html, configuration=config, options={"enable-local-file-access": ""})
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response


@app.route('/search')
@login_required
def search():
    check_product_quant = db.session.query(AddProduct.product_name).filter(AddProduct.product_quantity <= 5).all()
    check_expiry_date = db.session.query(AddProduct.product_name).filter(
        AddProduct.product_expiry_date <= datetime.now() + timedelta(3)).all()
    check_expired = db.session.query(AddProduct.product_name).filter(
        AddProduct.product_expiry_date < date.today()).all()

    print(check_expiry_date)
    print(check_expired)
    print("Notification : ")
    print(check_product_quant)

    if check_product_quant:
        flash(str(convert(check_product_quant)) + ' are less than 6 products')
    if check_expiry_date:
        flash(str(convert(check_expiry_date)) + ' this products are due to expire...!')
    if check_expired:
        flash(str(convert(check_expired)) + ' this products are expired...')

    return render_template('search.html', posts=AddProduct.query.all())


def convert(lst):
    result_list = [str(row) for row in lst]
    string = " ".join(result_list)
    return string.replace('(', '').replace(')', '')
    # return ', '.join(string)


if __name__ == '__main__':
    app.run(debug=True)
