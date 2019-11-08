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
    
    statement =  """CREATE TABLE SITEUSER(
                        ID SERIAL PRIMARY KEY,
                        USERNAME VARCHAR(40),
                        PASSWORD VARCHAR(100),
                        USERTYPE VARCHAR(10));
    
                    CREATE TABLE CUSTOMER(
                            ID INTEGER REFERENCES SITEUSER(ID),
                            NAME VARCHAR(50),
                            SURNAME VARCHAR(50),
                            ADDRESS VARCHAR(300),
                            TOTAL_ORDERS INTEGER DEFAULT 0,
                            DELETE CASCADE);
                   CREATE TABLE COMPANY(
                        ID INTEGER REFERENCES SITEUSER(ID),
                        NAME VARCHAR(40),
                        AVGDAY INTERVAL,
                        YEAR_FOUNDED INTEGER,
                        TOTAL_ORDERS INTEGER DEFAULT 0,
                            DELETE CASCADE);
                   CREATE TABLE MYORDER(
                        ORDER_ID SERIAL PRIMARY KEY,
                        CUSTOMER_ID INTEGER REFERENCES SITEUSER(ID),
                        COMPANY_ID INTEGER REFERENCES SITEUSER(ID),
                        ORDER_DATE DATE,
                        URGENT BOOLEAN,
                        DELETE CASCADE);
                        """
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    connection.close()
    return

def create_user(username,password,account_type):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    
    statement = """INSERT INTO SITEUSER (USERNAME , PASSWORD , USERTYPE)
                    VALUES ( %s , %s , %s )            
                        """
    cursor.execute(statement, (username,password,account_type))
    connection.commit()
    cursor.close()
    connection.close()
    return

def get_customers():
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    
    statement = """SELECT ID ,USERNAME , PASSWORD , USERTYPE FROM SITEUSER           
                        """
    cursor.execute(statement)
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers

def delete_user(id_todelete):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    
    statement = """DELETE FROM SITEUSER
                    WHERE ( ID = (%(id_todelete)s) )           
                        """
                        
    cursor.execute(statement, {'id_todelete' : id_todelete})
    connection.commit()
    cursor.close()
    connection.close()
    return

def create_customer(username, name,surname,address):
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = """SELECT ID FROM SITEUSER
                    WHERE (USERNAME = (%(username)s))           
                        """
    cursor.execute(statement, {'username' : username})
    #return username
    for item in cursor:
        user_id = item ###Burası degismeliiiiiiiiiiiiiiiiiiiiiiiiii
    statement = """INSERT INTO CUSTOMER (ID , NAME,SURNAME , ADDRESS)
                    VALUES ( %(user_id)s , %(name)s , %(surname)s , %(address)s )            
                        """
    cursor.execute(statement, {'user_id' : user_id, 'name' : name , 'surname' : surname , 'address' : address })
    connection.commit()
    cursor.close()
    connection.close()
    return










