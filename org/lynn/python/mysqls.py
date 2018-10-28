# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Cailinfeng'

import mysql.connector

con = mysql.connector.connect(user='root', password='123456', database='lynn', host='127.0.0.1')
cursor = con.cursor()
cursor.execute("select * from t_user where id = %s", [1])
values = cursor.fetchall()
for v in values:
    print(v)
