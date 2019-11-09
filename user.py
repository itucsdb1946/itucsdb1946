#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 00:51:11 2019

@author: cenk
"""
from flask_login import UserMixin
from mysqlstatements import getpassword

class User(UserMixin):
    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.active = True

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active


def get_user(user_name):
    username , password , usertype = getpassword(user_name)
    return User(username , password , usertype)