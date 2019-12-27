Tables
===================================

.. note:: All table creations exist in db_init.py file.

**************
Customer
**************
This table will contain customer information. It will have a reference to siteuser table on id.

1. Creation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

                    CREATE TABLE IF NOT EXISTS CUSTOMER(
                            ID INTEGER PRIMARY KEY,
                            NAME VARCHAR(50),
                            SURNAME VARCHAR(50),
                            ADDRESS VARCHAR(300),
                            TOTAL_ORDERS INTEGER DEFAULT 0,
                            YEAR_BORN INTEGER,
                            CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);

* ``id`` ``PRIMARY KEY`` id of customer referenced on siteuser table
* ``name``	First name of the customer
* ``surname``	Last name of the customer
* ``address``	Address of the customer
* ``total_orders``	Total orders of the customer which will be updated once he/she makes an order 
* ``year_born``	The year the customer was born



2. Reading 
~~~~~~~~~~~~~~~~~~~~~~~~

For reading both customer and company information i implemented a single function. By giving the username as an argument you will choose which user you want to get the information of and with usertype you will be able to use two different select statements for two different tables.

.. code-block:: python

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

You can see the specific sql statement below.

.. code-block:: sql

    SELECT NAME,SURNAME,ADDRESS,YEAR_BORN FROM CUSTOMER
                             WHERE (ID = %(user_id)s))
	
3. Inserting
~~~~~~~~~~~~~~~~~~~~~~~~

For inserting a new customer to the table i implemented the function below. It will take name, surname, address, yearborn as parameters and create the customer for given username.

.. code-block:: python

    def create_customer(username, name,surname,address,yearborn):
        connection = dbapi2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        statement = """SELECT ID FROM SITEUSER
                        WHERE (USERNAME = (%(username)s))           
                            """
        cursor.execute(statement, {'username' : username})
        for item in cursor:
            user_id = item
        statement = """INSERT INTO CUSTOMER (ID , NAME,SURNAME , ADDRESS, YEAR_BORN)
                        VALUES ( %(user_id)s , %(name)s , %(surname)s , %(address)s ,%(yearborn)s )            
                            """
        cursor.execute(statement, {'user_id' : user_id, 'name' : name , 'surname' : surname , 'address' : address , 'yearborn' : yearborn })
        connection.commit()
        cursor.close()
        connection.close()
        return

			
4. Updating 
~~~~~~~~~~~~~~~~~~~~~~~~

In order to update an existing user information on system i implemented a single function for both customer and company data. You will choose your update type by giving the usertype.

The arguments for this function: 

* ``username``  Username of the user which will be updated
* ``whichupdate``	Specifies which value will be updated
* ``newvalue``	What value will the current value be updated to
* ``usertype``	Specifies which update to be used

.. code-block:: python
	
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
		
		
5. Deleting
~~~~~~~~~~~~~~~~~~~~~~~~

For deleting a customer from the system. The same function in update will be used and "whichupdate" argument "DELETE". Then, the following sql statement will be ran.

.. code-block:: sql

    DELETE FROM CUSTOMER
        WHERE (ID = %(user_id)s);
        DELETE FROM SITEUSER
        WHERE (ID = %(user_id)s)

The arguments for this function: 

* ``username``  Username of the user which will be updated
* ``whichupdate``	Specifies which value will be updated
* ``newvalue``	What value will the current value be updated to
* ``usertype``	Specifies which update to be used


.. code-block:: python

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
	
****************
Company
****************
This table will hold company information and it will have a reference to siteuser table on id.

1. Creation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

    CREATE TABLE IF NOT EXISTS COMPANY(
             ID INTEGER PRIMARY KEY,
             NAME VARCHAR(40),
             AVGDAY INTEGER,
             YEAR_FOUNDED INTEGER,
             TOTAL_ORDERS INTEGER DEFAULT 0,
             CITY VARCHAR(40),
             CONSTRAINT CONSTRAINT1
                FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                ON DELETE CASCADE);

* ``id`` ``PRIMARY KEY`` id of company referenced on siteuser table
* ``name``	First name of the company
* ``avgday``	Avarage day for a company to deliver an order
* ``year_founded``	The year that the company was founded
* ``total_orders``	Total orders of the compant which will be updated once a customer makes an order from this specific company 
* ``city``	The city that this company is stationed on.


2. Reading
~~~~~~~~~~~~~~~~~~~~

For reading a companys information the same function used for customer will be used. Simply we will give "COMPANY" as the usertype.

Function arguments:  

* ``username``  Username of the user which we will get the information of
* ``usertype``	Specifies which select will be used

.. code-block:: python

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

You can see the specific sql statement for this operation below.

.. code-block:: sql

    SELECT NAME,AVGDAY,YEAR_FOUNDED,TOTAL_ORDERS,CITY FROM COMPANY
                            WHERE (ID = %(user_id)s)  
	
	
3. Inserting
~~~~~~~~~~~~~~~~~~~~

For instering a new company to the system, I implemented a create_company function. This function will take following arguments and create a company for given username.

Function arguments: 

* ``username``  Username of the user which we will create a company for
* ``name``	The name of the new company
* ``year_founded``	The year that this new company was founded
* ``avgday``	Avarage day for this new company to deliver an order
* ``city``	The city that this new company is stationed at 

.. code-block:: python

    def create_company(username, name, year_founded,avgday,city):
        connection = dbapi2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        statement = """SELECT ID FROM SITEUSER
                        WHERE (USERNAME = (%(username)s))           
                            """
        cursor.execute(statement, {'username' : username})
        for item in cursor:
            user_id = item
        statement = """INSERT INTO COMPANY (ID , NAME , YEAR_FOUNDED, AVGDAY, CITY)
                        VALUES ( %(user_id)s , %(name)s , %(year_founded)s , %(avgday)s , %(city)s )            
                            """
        cursor.execute(statement, {'user_id' : user_id, 'name' : name , 'year_founded' : year_founded ,  'avgday':avgday, 'city' : city })
        connection.commit()
        cursor.close()
        connection.close()
        return

You can see the specific sql statement for this operation below.

.. code-block:: sql

    INSERT INTO COMPANY (ID , NAME , YEAR_FOUNDED, AVGDAY, CITY)
                 VALUES ( %(user_id)s , %(name)s , %(year_founded)s , %(avgday)s , %(city)s ) 

4. Updating
~~~~~~~~~~~~~~~~~~~~

In order to update an existing user information on system i implemented a single function for both customer and company data. You will choose your update type by giving the usertype. For this specific update you will set usertype "COMPANY".

The arguments for this function: 

* ``username``  Username of the user which will be updated
* ``whichupdate``	Specifies which value will be updated
* ``newvalue``	What value will the current value be updated to
* ``usertype``	Specifies which update to be used

.. code-block:: python
	
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
		
		

5. Deleting
~~~~~~~~~~~~~~~~~~~~

For deleting a customer from the system. The same function in update will be used and "whichupdate" argument "DELETE". Then, the following sql statement will be ran.

.. code-block:: sql

    DELETE FROM COMPANY
        WHERE (ID = %(user_id)s);
        DELETE FROM SITEUSER
        WHERE (ID = %(user_id)s)

The arguments for this function: 

* ``username``  Username of the user which will be updated
* ``whichupdate``	Specifies which value will be updated
* ``newvalue``	What value will the current value be updated to
* ``usertype``	Specifies which update to be used


.. code-block:: python

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
	
****************
Myorder
****************

This is the table for holding order information. The orders will be created by customers. Then, both customers and companies will see the orders in their allowed manner.

1. Creation
~~~~~~~~~~~~~~~~~~~~


.. code-block:: sql
	
    CREATE TABLE IF NOT EXISTS MYORDER(
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

* ``order_id`` ``PRIMARY KEY`` id of the order
* ``customer_id``	Id of the customer who made the order, it is referenced from Customer table
* ``company_id``	Id of the company who received the order, it is referenced from Customer table
* ``order_date``	Date the order was created
* ``item``	The item that was ordered
* ``how_many``	How many of the given item was ordered

2. Reading
~~~~~~~~~~~~~~~~~~~~

For getting order information following function was implemented. Since, we have different user dashboard and we want list the orders in  a different way, I added usertype as an argument to this function. If the user is a customer the orders he/she made will be listed and if the user is a company the orders which were made from that specific company will be listed.

Function arguments:

* ``username``  Username of the user whose related orders will be listed
* ``usertype``	For specifiying the listing difference

.. code-block:: python

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
	
3. Inserting
~~~~~~~~~~~~~~~~~~~~

When a customer creates an order this function below will be called. Then with the proper parameters an order will be created linked to the that user. 

.. code-block:: python

    def create_order(username,company_id,item,howmany):
        connection = dbapi2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        
        statement = """SELECT ID FROM SITEUSER
                                WHERE (USERNAME = %(username)s)           
                            """
        cursor.execute(statement, {'username' : username})
        user_id = cursor.fetchone()
        for item in cursor:
            user_id = item
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

4. Updating
~~~~~~~~~~~~~~~~~~~~

In our system a customers can update the item that they ordered. By doing they will cause the calling of this following function. Then the value of the item will be updated with the new value. 

Function arguments:

* ``id_todelete``  Id of the order that will be updated
* ``newvalue``	What value the attribute will be updated to

.. code-block:: python

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

5. Deleting
~~~~~~~~~~~~~~~~~~~~

In order to delete a order, i implemented this function below. The id which is given as parameter of an order will be deleted. 

Function arguments:

* ``id_todelete``  Id of the order that will be deleted

.. code-block:: python

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

*********************
Extra Table Siteuser
*********************

This is the table for holding user information like username, password and account type.

1. Creation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql
	
    CREATE TABLE IF NOT EXISTS SITEUSER(
              ID SERIAL PRIMARY KEY,
              USERNAME VARCHAR(40),
              PASSWORD VARCHAR(100),
              USERTYPE VARCHAR(10));

* ``id`` ``PRIMARY KEY`` Id of the user
* ``username``	Username of the user
* ``password``	Password of the user
* ``usertype``	Account type of the user

2. Reading
~~~~~~~~~~~~~~~~~~~~

This function will be called to get the id of the user with username.

Function arguments:

* ``username``  Username of the user whose user_id will be returned.

.. code-block:: python

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
	
3. Inserting
~~~~~~~~~~~~~~~~~~~~

This function will be used to create a user after signup. 

.. code-block:: python

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


4. Deleting
~~~~~~~~~~~~~~~~~~~~

In order to delete a user, i implemented this function below. The id which is given as parameter of a user will be deleted. 

Function arguments:

* ``id_todelete``  Id of the order that will be deleted

.. code-block:: python

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
