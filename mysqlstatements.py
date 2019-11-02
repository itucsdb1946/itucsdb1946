# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:37:41 2019

@author: Cenk
"""

import psycopg2 as dbapi2

dsn = """user='postgres' password='docker'
         host='localhost' port=5432 dbname='postgres'"""
def create_tables():
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    print ("oh yeah connected")
    
    statement = """CREATE TABLE CUSTOMER(
                            CUSTOMER_ID SERIAL PRIMARY KEY,
                            NAME VARCHAR(50),
                            SURNAME VARCHAR(50),
                            ADDRESS VARCHAR(300),
                            TOTAL_ORDERS INTEGER DEFAULT 0);
                   CREATE TABLE COMPANY(
                        COMPANY_ID SERIAL PRIMARY KEY,
                        NAME VARCHAR(40),
                        AVGDAY INTERVAL,
                        YEAR_FOUNDED INTEGER,
                        TOTAL_ORDERS INTEGER DEFAULT 0);
                   CREATE TABLE MYORDER(
                        ORDER_ID SERIAL PRIMARY KEY,
                        CUSTOMER_ID INTEGER REFERENCES CUSTOMER(CUSTOMER_ID),
                        COMPANY_ID INTEGER REFERENCES COMPANY(COMPANY_ID),
                        ORDER_DATE DATE,
                        URGENT BOOLEAN
                        )              
                        """
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    return

def create_customer(name,surname,address):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    print ("oh yeah connected")
    
    statement = """INSERT INTO CUSTOMER (NAME,SURNAME , ADDRESS)
                    VALUES ( %s , %s , %s )            
                        """
    cursor.execute(statement, (name,surname,address))
    connection.commit()
    cursor.close()
    return

def list_customer():
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    print ("oh yeah connected")
    
    statement = """SELECT NAME,SURNAME,ADDRESS FROM CUSTOMER           
                        """
    cursor.execute(statement)
    customers = ""
    for name, surname, address in cursor:
        customers += name + "-" +  surname + "-" + address + "<br />"
    return customers