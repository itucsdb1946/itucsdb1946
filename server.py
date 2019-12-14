# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:00:41 2019

@author: Cenk
"""

from flask import Flask #render_template  #applications are instances of this class
from flask_bootstrap import Bootstrap
from flask_login import LoginManager,login_required
#from datetime import datetime

import views
from views import User
from mysqlstatements import get_user
lm = LoginManager()

DEBUG = False
if(DEBUG == False):
	url = os.getenv("DATABASE_URL")
else:
    url = "dbname='postgres' user='postgres' host='localhost' password='hastayimpw'"
    initialize(url)


@lm.user_loader
def load_user(user_id):
    username = user_id
    temp = get_user(username)
    if temp is not None:
        realpassword, usertype = temp
        user = User(username, realpassword, usertype)
        return user
    else:
        return None

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    Bootstrap(app)

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/signup", view_func=views.signup_page , methods = ['GET','POST'])
    app.add_url_rule("/listcustomer", view_func=views.list_customers_page , methods = ['GET','POST'])
    app.add_url_rule("/createcustomer", view_func=views.create_customer_page , methods = ['GET','POST'])
    app.add_url_rule("/login", view_func=views.login_page, methods=["GET", "POST"])
    app.add_url_rule("/customerpage", view_func=views.customer_page, methods=["GET", "POST"])
    app.add_url_rule("/dashboard", view_func=views.dashboard, methods=["GET", "POST"])
    app.add_url_rule("/companydashboard", view_func=views.company_dashboard, methods=["GET", "POST"])
    app.add_url_rule("/droptables", view_func=views.drop_tables_page)
    app.add_url_rule("/currentuser", view_func=views.current_user_page)
    
    lm.init_app(app)
    lm.login_view = "login_page"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)
