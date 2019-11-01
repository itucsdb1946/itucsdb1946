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

#from mysqlstatements import create_tables


#from server import app
print("deneme1")
#@app.route("/")
def home_page():
    #create_tables()
    dsn = """user='vagrant' password='vagrant'
         host='0.0.0.0' dbname='itucsdb'"""

    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = """CREATE TABLE CUSTOMER (
                        CUSTOMER_ID SERIAL PRIMARY KEY,
                        NAME VARCHAR(50),
                        SURNAME VARCHAR(50),
                        SCORE FLOAT,
                        VOTES INTEGER DEFAULT 0,
                        DIRECTORID INTEGER REFERENCES PERSON (ID)
                    )
                    CREATE TABLE COMPANY(
                    COMPANY_ID SERIAL PRIMARY KEY,
                    NAME VARCHAR(40),
                    AVGDAY INTERVAL,
                    YEAR_FOUNDED INTEGER,
                    TOTAL_ORDERS INTEGER DEFAULT 0
                    )
                    
                    CREATE TABLE ORDER(
                    ORDER_ID SERIAL PRIMARY KEY,
                    CUSTOMER_ID REFERENCES CUSTOMER (ID),
                    COMPANY_ID REFERENCES COMPANY (ID),
                    ORDER_DATE DATE,
                    URGENT BOOLEAN
                    )
                    
                    """
    cursor.execute(statement)
    cursor.commit()
    cursor.close()   
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


def movie_add_page():
    if request.method == "GET":
        return render_template(
            "movie_edit.html", min_year=1887, max_year=datetime.now().year
        )
    else:
        form_title = request.form["title"]
        form_year = request.form["year"]
        movie = Movie(form_title, year=int(form_year) if form_year else None)
        with dbapi2.connect(dsn) as connection:
            with connection.cursor() as cursor:
                for item in movie_data:
                    statement = """
                INSERT INTO MOVIE (TITLE, YR, SCORE, VOTES, DIRECTORID)
                           VALUES (%(title)s, %(year)s, %(score)s, %(votes)s,
                                   %(directorid)s)
                RETURNING id
            """
            item['directorid'] = person_ids[item['director']]
            cursor.execute(statement, item)
            connection.commit()
        
        
        #db = current_app.config["db"]
        movie_key = db.add_movie(movie)
        return redirect(url_for("movie_page", movie_key=movie_key))