#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:04 2020

@author: kodiuser
"""
from flask import Flask, render_template, request, flash
#import json, random, requests, re, html
import random, requests, html
#from html.parser import HTMLParser
global score
score = 0
global session_count
session_count = 0
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=['GET', 'POST'])
def input():

    if request.method == 'GET':
        current_score = request.args.get('current_score')
        current_questions = request.args.get('current_questions')
        if current_score == None:
            current_questions = 0
            current_score = 'You have completed nothing.'
        app.logger.info(current_score)
        app.logger.info(current_questions)
        randomiser = random.getrandbits(1)
        if randomiser == 0:
            question_type = 'boolean'
        else:
            question_type = 'multiple'
        app.logger.info(question_type)   
        url = 'https://opentdb.com/api.php?amount=1&&difficulty=easy&category=27&type=' + question_type
        resp = requests.get(url=url)
        json_array = resp.json() # Check the JSON Response Content documentation below
        quiz_list = []
        i = 0
        if question_type == 'boolean':
            choices = {"choice_a":None, "choice_b":None}
            choices['choice_a'] = json_array['results'][i]['incorrect_answers'][0]
            choices['choice_b'] = json_array['results'][i]['correct_answer']
            keys =  list(choices.items())
            quiz_details = {"question":None, "choice_a":None, "choice_b":None, "answer":None,"category":None,"difficulty":None}
            quiz_details['question'] = json_array['results'][i]['question']
            quiz_details['choice_a'] = keys[0][1]
            quiz_details['choice_b'] = keys[1][1]
            quiz_details['answer'] = json_array['results'][i]['correct_answer']
            quiz_details['category'] = json_array['results'][i]['category']
            quiz_details['difficulty'] = json_array['results'][i]['difficulty']
            quiz_list.append(quiz_details)
            question = random.choice(quiz_list)
            return render_template('index.html', answer=question['answer'],question=html.unescape(question['question']),choice_a=question['choice_a'],choice_b=question['choice_b'],category=question['category'],difficulty=question['difficulty'].title(),current_score=current_score,current_questions=current_questions,question_type=question_type)
            
        else:
            choices = {"choice_a":None, "choice_b":None, "choice_c":None, "choice_d":None}
            choices['choice_a'] = json_array['results'][i]['incorrect_answers'][0]
            choices['choice_b'] = json_array['results'][i]['incorrect_answers'][1]
            choices['choice_c'] = json_array['results'][i]['incorrect_answers'][2]
            choices['choice_d'] = json_array['results'][i]['correct_answer']
            keys =  list(choices.items())
            random.shuffle(keys)
            quiz_details = {"question":None, "choice_a":None, "choice_b":None, "choice_c":None, "choice_d":None,"answer":None,"category":None,"difficulty":None}
            quiz_details['question'] = json_array['results'][i]['question']
            quiz_details['choice_a'] = keys[0][1]
            quiz_details['choice_b'] = keys[1][1]
            quiz_details['choice_c'] = keys[2][1]
            quiz_details['choice_d'] = keys[3][1]
            quiz_details['answer'] = json_array['results'][i]['correct_answer']
            quiz_details['category'] = json_array['results'][i]['category']
            quiz_details['difficulty'] = json_array['results'][i]['difficulty']
            quiz_list.append(quiz_details)
            question = random.choice(quiz_list)
            return render_template('index.html', answer=html.unescape(question['answer']),question=html.unescape(question['question']),choice_a=html.unescape(question['choice_a']),choice_b=html.unescape(question['choice_b']),choice_c=html.unescape(question['choice_c']),choice_d=html.unescape(question['choice_d']),category=question['category'],difficulty=question['difficulty'].title(),current_score=current_score,current_questions=current_questions,question_type=question_type)

    if request.method == 'POST':
        global session_count
        global score
        session_count += 1
        session_count_string = 'Questions answered: ' + str(session_count)
        req = request.form
        ans_choice = req.get('slct')
        orig_choice_a = req.get('choice_a_hidden')
        orig_choice_b = req.get('choice_b_hidden')
        orig_choice_c = req.get('choice_c_hidden')
        orig_choice_d = req.get('choice_d_hidden')
        answer = req.get('verify')
        app.logger.info(orig_choice_a)
        app.logger.info(orig_choice_b)
        app.logger.info(orig_choice_c)
        app.logger.info(orig_choice_d)
        app.logger.info('You chose ' + ans_choice)
        app.logger.info('The correct answer was ' + answer)
        if ans_choice == answer:
                result = 'Correct'
                score += 1
                current_score = 'Correct ratio: ' + str("{0:.0%}".format(score/session_count))
                #'You have completed ' + str(session_count) + ' questions this session. So far ' + str("{0:.0%}".format(score/session_count)) + ' are correct.'
                flash('Correctamundo!')
                app.logger.info(session_count)
                app.logger.info(score)
                return render_template('index_result.html',result=result,current_score=current_score,current_questions=session_count_string)
        else:
                result = 'Incorrect'
                hint = 'The correct answer was .... ' + answer
                flash('The correct answer was .... ' + answer)
                app.logger.info(session_count)
                app.logger.info(score)
                current_score = 'Correct ratio: ' + str("{0:.0%}".format(score/session_count))
                #'You have completed ' + str(session_count) + ' questions this session. So far ' + str("{0:.0%}".format(score/session_count)) + ' are correct.'
                return render_template('index_result.html',result_err=result,hint=hint,current_score=current_score,current_questions=session_count_string)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
