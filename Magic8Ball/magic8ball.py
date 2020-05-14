#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:45:10 2020

@author: kodiuser
"""
# Import the modules
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def input():
    ball_roll = 0
    answer_feedback = 'What is the answer?'
    answer_sentiment = '#happy_as'
    answer_err = ''
    
    if request.method == 'POST':
        ball_roll = np.random.randint(1,20, size=1) 

        #Affirmative
        if ball_roll == 1: 
            answer_feedback = "It is certain."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 2: 
            answer_feedback = "It is decidedly so."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 3: 
            answer_feedback = "Without a doubt."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 4: 
            answer_feedback = "Yes - definitely."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 5: 
            answer_feedback = "You may rely on it."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 6: 
            answer_feedback = "As I see it, yes."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 7: 
            answer_feedback = "Most likely."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 8: 
            answer_feedback = "Outlook good."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 9: 
            answer_feedback = "Yes."
            answer_sentiment = "#Affirmative"
        elif ball_roll == 10: 
            answer_feedback = "Signs point to yes."
            answer_sentiment = "#Affirmative"
            #Non commital
        elif ball_roll == 11: 
            answer_feedback = "Reply hazy, try again."
            answer_sentiment = "#Non commital"
        elif ball_roll == 12: 
            answer_feedback = "Ask again later."
            answer_sentiment = "#Non commital"
        elif ball_roll == 13: 
            answer_feedback = "Better not tell you now."
            answer_sentiment = "#Non commital"
        elif ball_roll == 14: 
            answer_feedback = "Cannot predict now."
            answer_sentiment = "#Non commital"
        elif ball_roll == 15: 
            answer_feedback = "Concentrate and ask again."
            answer_sentiment = "#Non commital"
            #Negative
        elif ball_roll == 16: 
            answer_feedback = "Don't count on it."
            answer_sentiment = "#Negative"
        elif ball_roll == 17: 
            answer_feedback = "My reply is no."
            answer_sentiment = "#Negative"
        elif ball_roll == 18: 
            answer_feedback = "My sources say no."
            answer_sentiment = "#Negative"
        elif ball_roll == 19: 
            answer_feedback = "Outlook not so good."
            answer_sentiment = "#Negative"
        elif ball_roll == 20: 
            answer_feedback = "Very doubtful."
            answer_sentiment = "#Negative"
        else:
            answer_err = "Oops something went wrong!"
            answer_sentiment = "#wonky"
    return render_template('index.html', answer_feedback=answer_feedback, answer_sentiment=answer_sentiment, answer_err=answer_err)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')