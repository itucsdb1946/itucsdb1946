# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:37:41 2019

@author: Cenk
"""

def create_tables():
    with dbapi2.connect(dsn) as connection:
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
    NAME VARCHAR(40),
    AVGDAY INTERVAL,
    YEAR_FOUNDED INTEGER,
    TOTAL_ORDERS INTEGER DEFAULT 0
    )
    
    """
    cursor.execute(statement)
    cursor.close()
    return