Developer Guide
===============

Database Design
---------------

**For this project I decided to implement a delivery management system. So, I needed three tables. Customer table for holding the customer data, Company table for holding company and Myorder table for holding order data.**

.. figure:: images/tables.png

	Table Diagram

Code
------

This part will contain information about the code structure of this project.

Views
^^^^^

Views render what the user actually sees and also it gets input out of user. The main views functions will be discussed in Views subsection.

Views
===================================

**************
1. home_page
**************

This routes you to the login page.

.. code-block:: python

	def home_page():
	    return redirect(url_for("login_page"))

**************
2. signup_page
**************

This get the proper information from frontend and creates a user. Then if the user is a customer it creates a customer, else if the user is a company it creates a company.

.. code-block:: python

	def signup_page():
	    if request.method == "GET":
		return render_template("movie_edit.html")
	    else:
		form_username = request.form["username"]
		form_account_type = request.form["account_type"]
		form_password = request.form["password"]
		create_user(form_username,form_password,form_account_type)
		if(request.form["account_type"] == "Customer"):
		    form_name = request.form["Customer name"]
		    form_surname = request.form["Customer surname"]
		    form_address = request.form["Customer address"]
		    form_birth = request.form["Customer born"]
		    create_customer(form_username,form_name,form_surname,form_address,form_birth)
		    redirect(url_for("list_customers_page"))
		elif(request.form["account_type"] == "Company"):
		    form_name = request.form["Company name"]
		    form_founded = request.form["Founded year"]
		    form_avgday = request.form["Avarage Day"]
		    form_city = request.form["City"]
		    create_company(form_username, form_name, form_founded,form_avgday,form_city)
		return redirect(url_for("login_page"))
		

**************
3. dashboard
**************

This is the function that will view the customer dashboard. It will handle all order and profile operations. 

.. code-block:: python

	@login_required 
	def dashboard():
	    if request.method == "GET":
		companies = get_companies()
		orders = get_orders(current_user.username,"CUSTOMER")
		customerinfo = get_info(current_user.username,"CUSTOMER")
		return render_template("dashboard.html", companies = sorted(companies) , orders= orders, customerinfo=customerinfo) 
	    else:
		if 'CreateOrder' in request.form:
		    currentuser = current_user
		    company_id = request.form["which_company"]
		    item = request.form["item"]
		    howmany = request.form["Howmany"]
		    create_order(currentuser.username,company_id,item,howmany)
		    return redirect(url_for("dashboard"))
		elif 'DeleteOrder' in request.form:
		    orders = get_orders(current_user.username,"CUSTOMER")
		    orders_todelete = request.form.getlist("order")
		    for order_id in orders_todelete:
			delete_order(order_id)
		    return redirect(url_for("dashboard"))
		elif 'UpdateOrder' in request.form:
		    orders = get_orders(current_user.username,"CUSTOMER")
		    order_toupdate = request.form.getlist("order")
		    newvalue = request.form["Updateitem"]
		    update_order(order_toupdate[0],newvalue)
		    return redirect(url_for("dashboard"))
		elif 'Logout' in request.form:
		    logout_user()
		    return redirect(url_for("login_page"))
		elif 'Updateprofile' in request.form:
		    newvalue = request.form["Updatevalue"]
		    whichupdate = request.form["Whichupdate"]
		    update(current_user.username,whichupdate,newvalue,"CUSTOMER")
		    return redirect(url_for("dashboard"))
		    
**************
4. company_dashboard
**************

This is the function that will view the customer dashboard. It will handle all order and profile operations. 

.. code-block:: python

	@login_required 
	def company_dashboard():
	    if request.method == "GET":
		companies = get_companies()
		orders = get_orders(current_user.username,"COMPANY")
		info = get_info(current_user.username ,"COMPANY")
		return render_template("companydashboard.html", companies = sorted(companies) , orders= orders, customerinfo=info) 
	    else:
		if 'DeleteOrder' in request.form:
		    orders_todelete = request.form.getlist("order")
		    for order_id in orders_todelete:
			delete_order(order_id)
		    return redirect(url_for("company_dashboard"))
		elif 'Logout' in request.form:
		    logout_user()
		    return redirect(url_for("login_page"))
		elif 'Updateprofile' in request.form:
		    newvalue = request.form["Updatevalue"]
		    whichupdate = request.form["Whichupdate"]
		    update(current_user.username,whichupdate,newvalue ,"COMPANY")
		    return redirect(url_for("company_dashboard"))

**************
5. login_page
**************

This is the function that will view the login page. It will get your username and password. Then it checks wheter your password is correct or not. 

.. code-block:: python
		    
	def login_page():
	    logout_user()
	    form = LoginForm()
	    if form.validate_on_submit():
		username = form.data["username"]
		temp = get_user(username)
		if temp is not None:
		    realpassword, usertype = temp
		    user = User(username, realpassword, usertype)
		    password = form.data["password"]
		    if password == realpassword: ##burayı sonra hashli yaparsın
			login_user(user)
			flash("You have logged in.")
			if usertype == 'Customer':
			    next_page = request.args.get("next", url_for("dashboard"))
			elif usertype == 'Company':
			    next_page = request.args.get("next", url_for("company_dashboard"))
			return redirect(next_page)
		    else:
			return ("No such user")
	    return render_template("login.html", form=form)



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
