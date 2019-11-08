# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:48:31 2019

@author: Cenk
"""

from datetime import datetime

from flask import render_template, request, redirect , url_for, session
from mysqlstatements import create_tables,get_customers,create_user,delete_user,create_customer

#from passlib.hash import pbkdf2_sha256 as hasher

def home_page():
    create_tables()
    today = datetime.today()
    day_name = today.strftime("%A")
    current_time = today.strftime("%X")
    current_date = today.strftime("%x")
    return render_template("home.html", day=day_name , time = current_time , date = current_date)

def create_user_page():
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





















