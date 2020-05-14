#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:41:04 2020

@author: kodiuser
"""

import json
import sys, os, random
from termcolor import colored
import requests

url_all = 'https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple'
url_easy_gn = 'https://opentdb.com/api.php?amount=50&category=9&difficulty=easy&type=multiple'
url_medium_gn = 'https://opentdb.com/api.php?amount=50&category=9&difficulty=medium&type=multiple'


resp = requests.get(url=url_easy_gn)
json_array = resp.json() # Check the JSON Response Content documentation below
#input_file = open('/mnt/medialib/Python/Quiz/questions.json')
#json_array = json.load(input_file)
quiz_list = []
rand_answers = []
max_questions = 5
count = 1
score = 0
i = 0
while i < len(json_array['results']):
    choices = {"choice_a":None, "choice_b":None, "choice_c":None, "choice_d":None}
    choices['choice_a'] = json_array['results'][i]['incorrect_answers'][0]
    choices['choice_b'] = json_array['results'][i]['incorrect_answers'][1]
    choices['choice_c'] = json_array['results'][i]['incorrect_answers'][2]
    choices['choice_d'] = json_array['results'][i]['correct_answer']
    keys =  list(choices.items())
    random.shuffle(keys)
    quiz_details = {"question":None, "choice_a":None, "choice_b":None, "choice_c":None, "choice_d":None,"answer":None}
    quiz_details['question'] = json_array['results'][i]['question']
    quiz_details['choice_a'] = keys[0][1]
    quiz_details['choice_b'] = keys[1][1]
    quiz_details['choice_c'] = keys[2][1]
    quiz_details['choice_d'] = keys[3][1]
    quiz_details['answer'] = json_array['results'][i]['correct_answer']
    quiz_list.append(quiz_details)
    i += 1


while count <= max_questions:
    question = random.choice(quiz_list)
    print('_________________________________________________________________')
    print(question['question'])
    print('A: ' + question['choice_a'])
    print('B: ' + question['choice_b'])
    print('C: ' + question['choice_c'])
    print('D: ' + question['choice_d'])
    input_answer = input('The answer is?: ')
    print('_________________________________________________________________')
    if input_answer.upper() == 'A':
        if question['choice_a'] == question['answer']:
            print(' ')
            print(colored('Well done that was correct!', 'green'))
            score += 1
        else:
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
            print(colored('Oops that was incorrect!', 'yellow'))
            print(colored('The correct answer was ' + question['answer'],'yellow'))
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
    elif input_answer.upper() == 'B':
        if question['choice_b'] == question['answer']:
            print(' ')
            print(colored('Well done that was correct!', 'green'))
            score += 1
        else:
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
            print(colored('Oops that was incorrect!', 'yellow'))
            print(colored('The correct answer was ' + question['answer'],'yellow'))
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
    elif input_answer.upper() == 'C':
        if question['choice_c'] == question['answer']:
            print(' ')
            print(colored('Well done that was correct!', 'green'))
            score += 1
        else:
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
            print(colored('Oops that was incorrect!', 'yellow'))
            print(colored('The correct answer was ' + question['answer'],'yellow'))
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
    elif input_answer.upper() == 'D':
        if question['choice_d'] == question['answer']:
            print(' ')
            print(colored('Well done that was correct!', 'green'))
            score += 1
        else:
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
            print(colored('Oops that was incorrect!', 'yellow'))
            print(colored('The correct answer was ' + question['answer'],'yellow'))
            print(colored('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX','yellow'))
    count += 1
percent = (score/5)    
if score < 3:
    print('You got ' + str(score) + ' out of 5.  Thats works out to be pretty bad!')
elif score < 5:
    print('You got ' + str(score) + ' out of 5.  Thats works out to be middle of the road so I expect better from you!')
else:
    print('You got a perfect score!.  Thats works out to be ' + str("{:.0%}".format(percent)))