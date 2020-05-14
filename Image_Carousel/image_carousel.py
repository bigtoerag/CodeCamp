#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:15:39 2020

@author: kodiuser
"""
from flask import Flask, render_template, url_for
app = Flask(__name__, static_folder='static', template_folder='templates')
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html') 
if __name__ == '__main__':
 app.run(debug=True,host='0.0.0.0')