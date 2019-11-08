# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:00:41 2019

@author: Cenk
"""

from flask import Flask #render_template  #applications are instances of this class

#from datetime import datetime

import views




dsn = """user='vagrant' password='vagrant'
         host='0.0.0.0' port=8080 dbname='itucsdb'"""



def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/createuser", view_func=views.create_user_page , methods = ['GET','POST'])
    app.add_url_rule("/listcustomer", view_func=views.list_customers_page , methods = ['GET','POST'])
    app.add_url_rule("/createcustomer", view_func=views.create_customer_page , methods = ['GET','POST'])
    
    

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)
    
    # there was an error