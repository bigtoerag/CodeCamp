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
def home():
    roll_feedback = ''
    colour_feedback = ''
    colour = ''
    colour_roll = 2
    roll_dice_num = 0
    if request.method == 'POST':
        req = request.form
        roll_dice = req.get('roll_dice')
        colour_dice = req.get('colour_dice') 
        if roll_dice != 'on' and colour_dice != 'on':
            roll_dice_err = 'No dice selected, try again'
            colour_dice_err = 'No colour roll selected, try again'
            return render_template('index_gol.html', roll_dice_err=roll_dice_err, colour_dice_err=colour_dice_err)
        else:
            #return redirect(request.url)
            if roll_dice == 'on' and colour_dice == 'on':
                roll_dice_num = np.random.randint(1,10, size=1)
                roll_feedback = 'You rolled a ' + str(roll_dice_num[0])
                colour_roll = np.random.randint(2, size=1)
                if colour_roll == 0:
                    colour = 'red'
                    colour_feedback = 'You rolled Red!'
                else:
                    colour = 'black'
                    colour_feedback = 'You rolled Black!'
                print(roll_feedback, colour_feedback)
                return render_template('index_gol.html', roll_feedback=roll_feedback,colour_feedback=colour_feedback, colour=colour)
            elif roll_dice == 'on':
                colour = 'teal'
                roll_dice_num = np.random.randint(1,10, size=1)
                roll_feedback = 'You rolled a ' + str(roll_dice_num[0])
                colour_feedback = 'No need for a colour choice now!'
                print(roll_feedback, colour_feedback)
                return render_template('index_gol.html', roll_feedback=roll_feedback,colour_feedback=colour_feedback, colour=colour)
            elif colour_dice == 'on':
                colour_feedback = np.random.randint(2, size=1)
                roll_feedback = 'No need for a number roll!'
                if colour_feedback == 0:
                    colour = 'red'
                    colour_feedback = 'You rolled Red!'
                else:
                    colour = 'black'
                    colour_feedback = 'You rolled Black!' 
                print(roll_feedback, colour_feedback)
                return render_template('index_gol.html', roll_feedback=roll_feedback,colour_feedback=colour_feedback, colour=colour)
                
    else:
        return render_template('index_gol.html')   
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')