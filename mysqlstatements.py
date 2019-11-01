# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:37:41 2019

@author: Cenk
"""

import psycopg2 as dbapi2

dsn = """user='vagrant' password='vagrant'
         host='0.0.0.0' port=8080 dbname='itucsdb'"""

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
def create_tables():
    connection = dbapi2.connect()
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
    return