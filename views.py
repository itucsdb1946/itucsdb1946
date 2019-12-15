# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:48:31 2019

@author: Cenk
"""

from datetime import datetime

from flask import render_template, request, redirect , url_for, session, flash
from mysqlstatements import create_tables,get_customers,create_user,delete_user,create_customer, get_user, drop_tables, get_orders, delete_order, create_company, get_companies,create_order,get_info,update , update_order
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField#, BooleanField
from wtforms.validators import InputRequired#, Length , #Email if neccessary

#import user.py

#from passlib.hash import pbkdf2_sha256 as hasher


from flask_login import UserMixin,current_user, login_user, login_required, logout_user

class User(UserMixin):
    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.active = True

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

def home_page():
    #create_tables()
    today = datetime.today()
    day_name = today.strftime("%A")
    current_time = today.strftime("%X")
    current_date = today.strftime("%x")
    return render_template("home.html", day=day_name , time = current_time , date = current_date)

def signup_page():
    if request.method == "GET":
        return render_template("movie_edit.html")
    else:
        form_username = request.form["username"]
        form_account_type = request.form["account_type"]
        form_password = request.form["password"]
        create_user(form_username,form_password,form_account_type)
        if(request.form["account_type"] == "Customer"):
            form_name = request.form["Customer name"]
            form_surname = request.form["Customer surname"]
            form_address = request.form["Customer address"]
            form_birth = request.form["Customer born"]
            create_customer(form_username,form_name,form_surname,form_address,form_birth)
            redirect(url_for("list_customers_page"))
        elif(request.form["account_type"] == "Company"):
            form_name = request.form["Company name"]
            form_founded = request.form["Founded year"]
            form_avgday = request.form["Avarage Day"]
            form_city = request.form["City"]
            create_company(form_username, form_name, form_founded,form_avgday,form_city)
        return redirect(url_for("login_page"))
    
@login_required 
def dashboard():
    if request.method == "GET":
        companies = get_companies()
        orders = get_orders(current_user.username,"CUSTOMER")
        customerinfo = get_info(current_user.username,"CUSTOMER")
        return render_template("dashboard.html", companies = sorted(companies) , orders= orders, customerinfo=customerinfo) 
    else:
        if 'CreateOrder' in request.form:
            currentuser = current_user
            company_id = request.form["which_company"]
            item = request.form["item"]
            howmany = request.form["Howmany"]
            create_order(currentuser.username,company_id,item,howmany)
            return redirect(url_for("dashboard"))
        elif 'DeleteOrder' in request.form:
            orders = get_orders(current_user.username,"CUSTOMER")
            orders_todelete = request.form.getlist("order")
            for order_id in orders_todelete:
                delete_order(order_id)
            return redirect(url_for("dashboard"))
        elif 'UpdateOrder' in request.form:
            orders = get_orders(current_user.username,"CUSTOMER")
            order_toupdate = request.form.getlist("order")
            newvalue = request.form["Updateitem"]
            update_order(order_toupdate[0],newvalue)
            return redirect(url_for("dashboard"))
        elif 'Logout' in request.form:
            logout_user()
            return redirect(url_for("login_page"))
        elif 'Updateprofile' in request.form:
            newvalue = request.form["Updatevalue"]
            whichupdate = request.form["Whichupdate"]
            update(current_user.username,whichupdate,newvalue,"CUSTOMER")
            return redirect(url_for("dashboard"))
        
@login_required 
def company_dashboard():
    if request.method == "GET":
        companies = get_companies()
        orders = get_orders(current_user.username,"COMPANY")
        #for i,j,k,l,m in orders:
        #    return m
        info = get_info(current_user.username ,"COMPANY")
        return render_template("companydashboard.html", companies = sorted(companies) , orders= orders, customerinfo=info) 
    else:
        if 'DeleteOrder' in request.form:
            orders_todelete = request.form.getlist("order")
            for order_id in orders_todelete:
                delete_order(order_id)
            return redirect(url_for("company_dashboard"))
        elif 'Logout' in request.form:
            logout_user()
            return redirect(url_for("login_page"))
        elif 'Updateprofile' in request.form:
            newvalue = request.form["Updatevalue"]
            whichupdate = request.form["Whichupdate"]
            update(current_user.username,whichupdate,newvalue ,"COMPANY")
            return redirect(url_for("company_dashboard"))

def list_customers_page():
    if request.method == "GET":
        customers = get_customers()
        return render_template("customers.html", customers = sorted(customers))
    else:
        customers_todelete = request.form.getlist("person")
        for customer_id in customers_todelete:
            delete_user(customer_id)
        
    return redirect(url_for("list_customers_page"))

def create_customer_page():
    if request.method == "GET":
        return render_template("add_customer.html" )
    else:
        username = session.get('my_var' , None)
        form_name = request.form["name"]
        form_surname = request.form["surname"]
        form_address = request.form["address"]
        create_customer(username,form_name,form_surname,form_address)
        return redirect(url_for("list_customers_page"))

def login_page():
    logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        temp = get_user(username)
        if temp is not None:
            realpassword, usertype = temp
            user = User(username, realpassword, usertype)
            password = form.data["password"]
            if password == realpassword: ##burayı sonra hashli yaparsın
                login_user(user)
                flash("You have logged in.")
                if usertype == 'Customer':
                    next_page = request.args.get("next", url_for("dashboard"))
                elif usertype == 'Company':
                    next_page = request.args.get("next", url_for("company_dashboard"))
                return redirect(next_page)
            else:
                return ("No such user")
    return render_template("login.html", form=form)

def customer_page():
    if request.method == "GET":
        orders = get_orders()
        return render_template("customerpage.html", orders = sorted(orders))
    else:
        orders_todelete = request.form.getlist("person")
        
        for order_id in orders_todelete:
            delete_order(order_id)
        
    return redirect(url_for("list_customers_page"))

def drop_tables_page():
    drop_tables()
    return redirect(url_for("home_page"))

def current_user_page():
    currentuser = current_user
    return currentuser.username + "_" + currentuser.password + "_" + currentuser.usertype



















