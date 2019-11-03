# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:48:31 2019

@author: Cenk
"""

from datetime import datetime

from flask import render_template, request, redirect , url_for

import psycopg2 as dbapi2


dsn = """user='vagrant' password='vagrant'
         host='0.0.0.0' port=8080 dbname='itucsdb'"""

from mysqlstatements import create_tables,get_customers,create_customer,delete_customer


#from server import app
print("deneme1")
#@app.route("/")
def home_page():
    create_tables()
    today = datetime.today()
    day_name = today.strftime("%A")
    current_time = today.strftime("%X")
    current_date = today.strftime("%x")
    return render_template("home.html", day=day_name , time = current_time , date = current_date)

#@app.route("/movies")
def movies_page():
    return render_template("movies.html")

def actors_page():
    return "this is the actors page"

#@app.route('/createcustomer', methods=['GET', 'POST'])
def create_customer_page():
    print("deneme5")
    if request.method == "GET":
        return render_template(
            "movie_edit.html" #, min_year=1887, max_year=datetime.now().year
        )
    else:
        print("deneme4")
        form_name = request.form["name"]
        form_surname = request.form["surname"]
        form_address = request.form["address"]
        #movie = Movie(form_title, year=int(form_year) if form_year else None)
        
        #create_customer(form_name,form_surname,form_surname)
        create_customer(form_name,form_surname,form_address)
        #db = current_app.config["db"]
        #movie_key = db.add_movie(movie)
        return redirect(url_for("list_customers_page"))
    
def list_customers_page():
    if request.method == "GET":
        customers = get_customers()
        return render_template("customers.html", customers = sorted(customers))
    else:
        customers_todelete = request.form.getlist("person")
        
        for customer_id in customers_todelete:
            delete_customer(customer_id)
        
    return redirect(url_for("list_customers_page"))






















