#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:15:39 2020

@author: kodiuser
"""

from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        req = request.form
        att_dice_one = req.get('att_dice_one')
        att_dice_two = req.get('att_dice_two')
        att_dice_three = req.get('att_dice_three')
        def_dice_one = req.get('def_dice_one')
        def_dice_two = req.get('def_dice_two')
        if [att_dice_one, att_dice_two, att_dice_three].count('on') > 1:
            att_dice_err = 'Too many attack dice selected, try again'
            att_loses_feedback = ''
            def_loses_feedback = ''
            return render_template('index.html', att_dice_err=att_dice_err)
        elif [def_dice_one, def_dice_two].count('on') > 1:
            def_dice_err = 'Too many defence dice selected, try again'
            att_loses_feedback = ''
            def_loses_feedback = ''
            return render_template('index.html', def_dice_err=def_dice_err)
        else:
            if att_dice_one == 'on':
                att_dice_num = 1
            elif att_dice_two == 'on':
                att_dice_num = 2
            elif att_dice_three == 'on':
                att_dice_num = 3
            else:
                att_dice_num = 0
                
            if def_dice_one == 'on':
                def_dice_num = 1
            elif def_dice_two == 'on':
                def_dice_num = 2
            else:
                def_dice_num = 0
    else:
        att_loses_feedback = 'All attacking soldiers are standing tall and fighting strong'
        def_loses_feedback = 'All defending soldiers are standing tall and fighting strong'
        return render_template('index.html', att_loses_feedback=att_loses_feedback,def_loses_feedback=def_loses_feedback)  
    if att_dice_num == 0:
            att_dice_err = 'No attack dice selected, try again'
            att_loses_feedback = 'All attacking soldiers are standing tall and fighting strong'
            def_loses_feedback = 'All defending soldiers are standing tall and fighting strong'
            return render_template('index.html', att_dice_err=att_dice_err, att_loses_feedback=att_loses_feedback,def_loses_feedback=def_loses_feedback)
    elif def_dice_num == 0:
            def_dice_err = 'No defence dice selected, try again'
            att_loses_feedback = 'All attacking soldiers are standing tall and fighting strong'
            def_loses_feedback = 'All defending soldiers are standing tall and fighting strong'
            return render_template('index.html', def_dice_err=def_dice_err, att_loses_feedback=att_loses_feedback,def_loses_feedback=def_loses_feedback)
    else:
            att_loses_feedback = 'All attacking soldiers are standing tall and fighting strong'
            def_loses_feedback = 'All defending soldiers are standing tall and fighting strong'
            
            att_loses = 0
            def_loses = 0
    if att_dice_num == 3 and def_dice_num == 2:
                att_arr = np.random.randint(1,6, size=3)
                att_arr[::-1].sort()
                def_arr = np.random.randint(1,6, size=2)
                def_arr[::-1].sort()
                if def_arr[0] >= att_arr[0]:
                    att_loses += 1
                else:
                    def_loses += 1
                if def_arr[1] >= att_arr[1]:
                    att_loses += 1
                else:
                    def_loses += 1
                    
    elif att_dice_num == 2 and def_dice_num == 2:
                att_arr = np.random.randint(1,6, size=2)
                att_arr[::-1].sort()
                def_arr = np.random.randint(1,6, size=2)
                def_arr[::-1].sort()
                if def_arr[0] >= att_arr[0]:
                    att_loses += 1
                else:
                    def_loses += 1
                if def_arr[1] >= att_arr[1]:
                    att_loses += 1
                else:
                    def_loses += 1
            
    elif att_dice_num == 1 and def_dice_num == 2:
                att_arr = np.random.randint(1,6, size=1)
                att_arr[::-1].sort()
                def_arr = np.random.randint(1,6, size=2)
                def_arr[::-1].sort()
                if def_arr[0] >= att_arr[0]:
                    att_loses += 1
                else:
                    def_loses += 1
                
    elif att_dice_num == 3 and def_dice_num == 1:
                att_arr = np.random.randint(1,6, size=3)
                att_arr[::-1].sort()
                def_arr = np.random.randint(1,6, size=1)
                def_arr[::-1].sort()
                if def_arr[0] >= att_arr[0]:
                    att_loses += 1
                else:
                    def_loses += 1
            
    elif att_dice_num == 2 and def_dice_num == 1:
                att_arr = np.random.randint(1,6, size=2)
                att_arr[::-1].sort()
                def_arr = np.random.randint(1,6, size=1)
                def_arr[::-1].sort()
                if def_arr[0] >= att_arr[0]:
                    att_loses += 1
                else:
                    def_loses += 1
            
    elif att_dice_num == 1 and def_dice_num == 1:
                att_arr = np.random.randint(1,6, size=1)
                att_arr[::-1].sort()
                def_arr = np.random.randint(1,6, size=1)
                def_arr[::-1].sort()
                if def_arr[0] >= att_arr[0]:
                    att_loses += 1
                else:
                    def_loses += 1
            
    if att_loses == 0:
            att_loses_feedback = 'No attacking soldiers have fallen'
            def_loses_feedback = f'{def_loses} defending soldier(s) have fallen, and need to be removed from the battlefield'                    
    elif def_loses == 0:
            att_loses_feedback = f'{att_loses} attacking soldier(s) have fallen, and need to be removed from the battlefield'
            def_loses_feedback = 'No defending soldiers have fallen'                    
    else:    
            att_loses_feedback = f'{att_loses} attacking soldier(s) have fallen, and need to be removed from the battlefield'
            def_loses_feedback = f'{def_loses} defending soldier(s) have fallen, and need to be removed from the battlefield'                    
    return render_template('index.html', att_loses_feedback=att_loses_feedback,def_loses_feedback=def_loses_feedback)
     
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')