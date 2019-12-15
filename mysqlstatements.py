# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:37:41 2019

@author: Cenk
"""

import psycopg2 as dbapi2

dsn = """user='postgres' password='docker'
         host='localhost' port=5432 dbname='postgres'"""
import os
def update(username,whichupdate,newvalue,usertype):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT ID FROM SITEUSER
                            WHERE (USERNAME = %(username)s)           
                        """
    cursor.execute(statement, {'username' : username})
    user_id = cursor.fetchone()
    if usertype == "CUSTOMER":
        if whichupdate == 'NAME':
            statement = """UPDATE CUSTOMER SET NAME = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'SURNAME':
            statement = """UPDATE CUSTOMER SET SURNAME = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'ADDRESS':
            statement = """UPDATE CUSTOMER SET ADDRESS = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'bornin':
            statement = """UPDATE CUSTOMER SET YEAR_BORN = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'DELETE':
            statement = """DELETE FROM CUSTOMER
                                WHERE (ID = %(user_id)s);
                            DELETE FROM SITEUSER
                                WHERE (ID = %(user_id)s)
                            """
    elif usertype == "COMPANY":
        if whichupdate == 'NAME':
            statement = """UPDATE COMPANY SET NAME = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'avgday':
            statement = """UPDATE COMPANY SET AVGDAY = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'year_founded':
            statement = """UPDATE COMPANY SET YEAR_FOUNDED = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'city':
            statement = """UPDATE COMPANY SET CITY = %(newvalue)s
                                WHERE (ID = %(user_id)s)
                            """
        elif whichupdate == 'DELETE':
            statement = """DELETE FROM COMPANY
                                WHERE (ID = %(user_id)s);
                            DELETE FROM SITEUSER
                                WHERE (ID = %(user_id)s)
                            """
    
    cursor.execute(statement,{'newvalue' : newvalue ,'user_id' : user_id})
    connection.commit()
    cursor.close()
    connection.close()
    return



def get_info(username,usertype):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT ID FROM SITEUSER
                            WHERE (USERNAME = %(username)s)           
                        """
    cursor.execute(statement, {'username' : username})
    user_id = cursor.fetchone()
    
    if usertype == "CUSTOMER":
        statement = """SELECT NAME,SURNAME,ADDRESS,YEAR_BORN FROM CUSTOMER
                        WHERE (ID = %(user_id)s)        
                        """
    elif usertype == "COMPANY":
        statement = """SELECT NAME,AVGDAY,YEAR_FOUNDED,TOTAL_ORDERS,CITY FROM COMPANY
                        WHERE (ID = %(user_id)s)        
                        """
    cursor.execute(statement,{'user_id' : user_id})
    customerinfo = cursor.fetchall()
    cursor.close()
    connection.close()
    return customerinfo




def create_tables():
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement =  """CREATE TABLE SITEUSER(
                        ID SERIAL PRIMARY KEY,
                        USERNAME VARCHAR(40),
                        PASSWORD VARCHAR(100),
                        USERTYPE VARCHAR(10));
    
                    CREATE TABLE CUSTOMER(
                            ID INTEGER,
                            NAME VARCHAR(50),
                            SURNAME VARCHAR(50),
                            ADDRESS VARCHAR(300),
                            TOTAL_ORDERS INTEGER DEFAULT 0,
                            YEAR_BORN INTEGER,
                            CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
                   CREATE TABLE COMPANY(
                        ID INTEGER,
                        NAME VARCHAR(40),
                        AVGDAY INTEGER,
                        YEAR_FOUNDED INTEGER,
                        TOTAL_ORDERS INTEGER DEFAULT 0,
                        CITY VARCHAR(40),
                        CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
                   CREATE TABLE MYORDER(
                        ORDER_ID SERIAL PRIMARY KEY,
                        CUSTOMER_ID INTEGER,
                        COMPANY_ID INTEGER,
                        ORDER_DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                        ITEM VARCHAR(100),
                        HOW_MANY INTEGER,
                        CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (CUSTOMER_ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE,
                        CONSTRAINT CONSTRAINT2
                            FOREIGN KEY (COMPANY_ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
                        """
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    connection.close()
    return

def create_user(username,password,account_type):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
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
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT ID ,USERNAME , PASSWORD , USERTYPE FROM SITEUSER           
                        """
    cursor.execute(statement)
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers

def get_companies():
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT ID , NAME FROM COMPANY           
                        """
    cursor.execute(statement)
    customers = cursor.fetchall()
    cursor.close()
    connection.close()
    return customers

#def create_order():

def get_orders(username,usertype):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT ID FROM SITEUSER
                            WHERE (USERNAME = %(username)s)           
                        """
    cursor.execute(statement, {'username' : username})
    user_id = cursor.fetchone()
    if usertype == "CUSTOMER":
        statement = """SELECT MYORDER.ORDER_ID, MYORDER.ORDER_DATE ,COMPANY.NAME, COMPANY.AVGDAY ,MYORDER.ITEM,MYORDER.HOW_MANY FROM COMPANY,MYORDER
                        WHERE (COMPANY.ID = MYORDER.COMPANY_ID) AND (MYORDER.CUSTOMER_ID = %(user_id)s)     
                        """
    elif usertype == "COMPANY":
        statement = """SELECT
                        MYORDER.ORDER_ID, MYORDER.ORDER_DATE ,MYORDER.ITEM, COMPANY.AVGDAY, CUSTOMER.ADDRESS , MYORDER.HOW_MANY 
                        FROM
                        COMPANY INNER JOIN MYORDER
                        ON (COMPANY.ID = MYORDER.COMPANY_ID) AND (MYORDER.COMPANY_ID = %(user_id)s)
                        INNER JOIN CUSTOMER
                        ON (CUSTOMER.ID = MYORDER.CUSTOMER_ID) 
                        """
    cursor.execute(statement ,{'user_id' : user_id} )
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return orders

def delete_user(id_todelete):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """DELETE FROM SITEUSER
                    WHERE ( ID = (%(id_todelete)s) )           
                        """
                        
    cursor.execute(statement, {'id_todelete' : id_todelete})
    connection.commit()
    cursor.close()
    connection.close()
    return

def delete_order(id_todelete):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """DELETE FROM MYORDER
                    WHERE ( ORDER_ID = (%(id_todelete)s) )           
                        """
                        
    cursor.execute(statement, {'id_todelete' : id_todelete})
    connection.commit()
    cursor.close()
    connection.close()
    return

def update_order(id_todelete,newvalue):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """UPDATE MYORDER SET ITEM = %(newvalue)s
                    WHERE ( ORDER_ID = (%(id_todelete)s) )           
                        """
                        
    cursor.execute(statement, {'id_todelete' : id_todelete , 'newvalue' : newvalue})
    connection.commit()
    cursor.close()
    connection.close()
    return



def create_customer(username, name,surname,address,yearborn):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    statement = """SELECT ID FROM SITEUSER
                    WHERE (USERNAME = (%(username)s))           
                        """
    cursor.execute(statement, {'username' : username})
    #return username
    for item in cursor:
        user_id = item ###Burası degismeliiiiiiiiiiiiiiiiiiiiiiiiii
    statement = """INSERT INTO CUSTOMER (ID , NAME,SURNAME , ADDRESS, YEAR_BORN)
                    VALUES ( %(user_id)s , %(name)s , %(surname)s , %(address)s ,%(yearborn)s )            
                        """
    cursor.execute(statement, {'user_id' : user_id, 'name' : name , 'surname' : surname , 'address' : address , 'yearborn' : yearborn })
    connection.commit()
    cursor.close()
    connection.close()
    return
"""
CREATE TABLE COMPANY(
                        ID INTEGER,
                        NAME VARCHAR(40),
                        AVGDAY INTEGER,
                        YEAR_FOUNDED INTEGER DEFAULT 0,  
                        TOTAL_ORDERS INTEGER DEFAULT 0,
                        CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);

YEAR FOUNDED DEFAULT OLMASIN OLUR MU YAHU
"""
def create_company(username, name, year_founded,avgday,city):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    statement = """SELECT ID FROM SITEUSER
                    WHERE (USERNAME = (%(username)s))           
                        """
    cursor.execute(statement, {'username' : username})
    #return username
    for item in cursor:
        user_id = item ###Burası degismeliiiiiiiiiiiiiiiiiiiiiiiiii
    statement = """INSERT INTO COMPANY (ID , NAME , YEAR_FOUNDED, AVGDAY, CITY)
                    VALUES ( %(user_id)s , %(name)s , %(year_founded)s , %(avgday)s , %(city)s )            
                        """
    cursor.execute(statement, {'user_id' : user_id, 'name' : name , 'year_founded' : year_founded ,  'avgday':avgday, 'city' : city })
    connection.commit()
    cursor.close()
    connection.close()
    return

"""
CREATE TABLE MYORDER(
                        ORDER_ID SERIAL PRIMARY KEY,
                        CUSTOMER_ID INTEGER,
                        COMPANY_ID INTEGER,
                        ORDER_DATE DATE,
                        ITEM VARCHAR(100),
                        CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (CUSTOMER_ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE,
                        CONSTRAINT CONSTRAINT2
                            FOREIGN KEY (COMPANY_ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
                        """
def create_order(username,company_id,item,howmany):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT ID FROM SITEUSER
                            WHERE (USERNAME = %(username)s)           
                        """
    cursor.execute(statement, {'username' : username})
    user_id = cursor.fetchone()
    for item in cursor:
        user_id = item ###Burası degismeliiiiiiiiiiiiiiiiiiiiiiiiii
    statement = """INSERT INTO MYORDER (CUSTOMER_ID , COMPANY_ID , ITEM ,HOW_MANY)
                    VALUES ( %(customer_id)s , %(company_id)s , %(item)s ,%(howmany)s);
                    UPDATE CUSTOMER SET TOTAL_ORDERS = TOTAL_ORDERS + 1
                    WHERE ID = %(customer_id)s;
                    UPDATE COMPANY SET TOTAL_ORDERS = TOTAL_ORDERS + 1
                    WHERE ID = %(company_id)s
                        """
    cursor.execute(statement, {'customer_id' : user_id, 'company_id' : company_id , 'item' : item, 'howmany' : howmany  })
    connection.commit()
    cursor.close()
    connection.close()
    

def get_user(username):
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """SELECT PASSWORD , USERTYPE FROM SITEUSER
                            WHERE (USERNAME = %(username)s)           
                        """
    cursor.execute(statement, {'username' : username})
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def drop_tables():
    connection = dbapi2.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()
    
    statement = """ DROP TABLE MYORDER;
                    DROP TABLE CUSTOMER;
                    DROP TABLE COMPANY;
                    DROP TABLE SITEUSER;
                        """
    cursor.execute(statement)
    connection.commit()
    connection.close()
    return







