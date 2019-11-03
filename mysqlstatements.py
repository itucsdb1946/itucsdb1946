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
    connection.close()
    return

def create_customer(name,surname,address):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    
    statement = """INSERT INTO CUSTOMER (NAME,SURNAME , ADDRESS)
                    VALUES ( %s , %s , %s )            
                        """
    cursor.execute(statement, (name,surname,address))
    connection.commit()
    cursor.close()
    connection.close()
    return

def get_customers():
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    
    statement = """SELECT CUSTOMER_ID,NAME,SURNAME,ADDRESS FROM CUSTOMER           
                        """
    cursor.execute(statement)
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers

def delete_customer(id_todelete):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    
    statement = """DELETE FROM CUSTOMER
                    WHERE ( CUSTOMER_ID = (%(id_todelete)s) )           
                        """
                        
    cursor.execute(statement, {'id_todelete' : id_todelete})
    connection.commit()
    cursor.close()
    connection.close()
    return










