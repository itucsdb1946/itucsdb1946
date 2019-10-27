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
    print("DENEME5")
    connection = dbapi2.connect(dsn)
    print("DENEME2")
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
    print("DENEME3")
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
    print("DENEME4")    
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