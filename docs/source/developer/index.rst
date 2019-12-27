Developer Guide
===============

Database Design
---------------

**For this project I decided to implement a delivery management system. So, I needed three tables. Customer table for holding the customer data, Company table for holding company and Myorder table for holding order data.**

.. figure:: images/tables.png

	Table Diagram

Code
------


Models
^^^^^^

Views
^^^^^

Views are what end-users are exposed to. It couples models and templates, renders them and serves them
to the users. These views are explained in detail on member specific implementation pages.

They are located at the folder ``routes/``

Templates
^^^^^

Templates contained a Html template that i manipulated to serve this project.

They are located at the folder ``templates/`` and are to be used by views.

My SQL Statements
^^^^^

The queries used for this project are gathered into a single python file.

And, they are located at the file ``mysqlstatements.py``

.. toctree::

   member1
   member2
