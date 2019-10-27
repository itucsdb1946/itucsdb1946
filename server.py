# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:00:41 2019

@author: Cenk
"""

from flask import Flask #render_template  #applications are instances of this class

#from datetime import datetime

import views

import psycopg2 as dbapi2


dsn = """user='vagrant' password='vagrant'
         host='0.0.0.0' port=8080 dbname='itucsdb'"""



def create_app():
    connection = dbapi2.connect(dsn)
    try:
        cursor = connection.cursor()
        statement = """CREATE TABLE PERSON (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(40) UNIQUE NOT NULL
        )"""
        cursor.execute(statement)
        connection.commit()
        cursor.close()
    except dbapi2.DatabaseError:
        connection.rollback()
    finally:
        connection.close()
        app = Flask(__name__)
        
    connection = dbapi2.connect(dsn)
    try:
        cursor = connection.cursor()
        statement = """CREATE TABLE PERSON (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(40) UNIQUE NOT NULL
        )"""
        cursor.execute(statement)
        connection.commit()
        cursor.close()
    except dbapi2.DatabaseError:
        connection.rollback()
    finally:
        connection.close()
        app = Flask(__name__)
        
    connection = dbapi2.connect(dsn)    
    try:
        cursor = connection.cursor()
        statement = """CREATE TABLE PERSON (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(40) UNIQUE NOT NULL
        )"""
        cursor.execute(statement)
        connection.commit()
        cursor.close()
    except dbapi2.DatabaseError:
        connection.rollback()
    finally:
        connection.close()
    
    app = Flask(__name__)



    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/movies", view_func=views.movies_page)
    app.add_url_rule("/actors", view_func=views.actors_page)

    return app


if __name__ == "__main__":
    print("deneme")
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True) # there was an error
    
"""
app = Flask(__name__)

__name__ is one such special variable. If the source file is 
executed as the main program, the interpreter sets the __name__ 
variable to have a value “__main__”. If this file is 
being imported from another module, __name__ will be set to the module’s name.

@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    current_time = today.strftime("%X")
    current_date = today.strftime("%x")
    
    https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    different laters indicate different string returns
    A is for weekdays full name For ex: Monday
    
    return render_template("home.html", day=day_name , time = current_time , date = current_date)

@app.route("/movies")
def movies_page():
    return render_template("movies.html")


A view function is defined to handle requests to the home page. 
It simply returns a string containing the title. 
The route decorator registers the / route with this function. 
So whenever there is a request to the / route, 
this function will be invoked and its result 
will be sent back to the client as the response.
"""