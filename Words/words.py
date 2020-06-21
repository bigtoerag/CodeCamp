#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:04 2020

@author: kodiuser
"""
from flask import Flask, render_template, request, flash
import random, requests, html

app = Flask(__name__)
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template('index.html')
if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')