# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:30:57 2019

@author: Cenk
"""

import psycopg2 as dbapi2

dsn = """user='postgres' password='docker'
         host='localhost' port=5432 dbname='postgres'"""

connection = dbapi2.connect(dsn)
cursor = connection.cursor()
print ("oh yeah connected")

statement = """DROP TABLE MYORDER;
DROP TABLE CUSTOMER;
DROP TABLE COMPANY;
               DROP TABLE SITEUSER;
                    """
cursor.execute(statement)
connection.commit()
cursor.close()   

"""
CREATE TABLE COMPANY(
                    COMPANY_ID SERIAL PRIMARY KEY,
                    NAME VARCHAR(40),
                    AVGDAY INTERVAL,
                    YEAR_FOUNDED INTEGER,
                    TOTAL_ORDERS INTEGER DEFAULT 0
                    )
                    
                    CREATE TABLE ORDER(
                    ORDER_ID SERIAL PRIMARY KEY,
                    CUSTOMER_ID REFERENCES CUSTOMER (CUSTOMER_ID),
                    COMPANY_ID REFERENCES COMPANY (COMPANY_ID),
                    ORDER_DATE DATE,
                    URGENT BOOLEAN
                    )


DROP TABLE MYORDER;

               DROP TABLE CUSTOMER;

               DROP TABLE COMPANY;
"""
