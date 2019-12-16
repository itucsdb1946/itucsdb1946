#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 00:50:22 2019

@author: cenk
"""

DEBUG = True
PORT = 8080
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin": "$pbkdf2-sha256$29000$PIdwDqH03hvjXAuhlLL2Pg$B1K8TX6Efq3GzvKlxDKIk4T7yJzIIzsuSegjZ6hAKLk",
    "normaluser": "$pbkdf2-sha256$29000$Umotxdhbq9UaI2TsnTMmZA$uVtN2jo0I/de/Kz9/seebkM0n0MG./KGBc1EPw5X.f0",
}

ADMIN_USERS = ["admin"]

def is_admin(checkpassword):
    if checkpassword == "admin123":
        return True
    else:
        return False
    
