# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:48:31 2019

@author: Cenk
"""

from datetime import datetime

from flask import render_template, request, redirect , url_for, session, flash
from mysqlstatements import create_tables,get_customers,create_user,delete_user,create_customer, get_user, drop_tables
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField#, BooleanField
from wtforms.validators import InputRequired#, Length , #Email if neccessary
#import user.py

#from passlib.hash import pbkdf2_sha256 as hasher


from flask_login import UserMixin,current_user, login_user

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
    create_tables()
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
        session['my_var'] = form_username
        return redirect(url_for("create_customer_page"))
    
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
                next_page = request.args.get("next", url_for("list_customers_page")) # list_customer_page for now
                return redirect(next_page)
    return render_template("login.html", form=form)

def drop_tables_page():
    drop_tables()
    return redirect(url_for("home_page"))

def current_user_page():
    currentuser = current_user
    return currentuser.username + "_" + currentuser.password + "_" + currentuser.usertype



















