#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:35:36 2020

@author: kodiuser
"""
from flask import Flask, render_template, request, flash
import random, requests, html, inflect, numexpr, math
from math import factorial

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/', methods=['GET', 'POST'])
def input():

    if request.method == 'GET':
        input_number = random.randrange(1000,9000,1)
        return render_template('index.html', input_number=input_number)
    if request.method == 'POST':
        def generate_answers(base_number,equation):
            correct_answers = {"q1":None,"q2":None,"q3":None, "q4":None, "q5":None, "q6":None, "q7":None, "q8":None, "q9":None, "q10":None,"q11":None, "q12":None, "q13":None, "blocks1000":None, "blocks100":None, "blocks10":None, "blocks1":None, "tallies1000":None, "tallies100":None, "tallies10":None, "tallies1":None}
            p = inflect.engine()
            joined = ""
            correct_answers['q1'] = str(base_number - 1)
            correct_answers['q2'] = str(base_number + 1)
            correct_answers['q6'] = str(base_number + 10)
            correct_answers['q7'] = str(base_number - 10)
            correct_answers['q8'] = str(base_number + 100)
            correct_answers['q9'] = str(printMaximum(base_number))
            correct_answers['q10'] = str(sum_digits(base_number))
            correct_answers['blocks1'] = str(0)
            correct_answers['blocks10'] = str(0)
            correct_answers['blocks100'] = str(0)
            correct_answers['blocks1000'] = str(0)
            correct_answers['tallies1'] = str(0)
            correct_answers['tallies10'] = str(0)
            correct_answers['tallies100'] = str(0)
            correct_answers['tallies1000'] = str(0)            
            correct_answers['q12'] = str(is_prime(base_number)).lower()
            #result_sqrt = is_square_root(base_number)
            #if result_sqrt[0]:
            #    correct_answers['q12'] = str(int(math.sqrt(base_number)))
            #else:
            #    correct_answers['q12'] = 'Oops. The low side showed ' + str(int(math.sqrt(result_sqrt[1]))) + ' and high side showed ' + str(int(math.sqrt(result_sqrt[2])))
            correct_answers['master_number'] = base_number
            correct_answers['q3'] = p.number_to_words(base_number).replace("-", " ").replace(",","")
            app.logger.debug(printMaximum(base_number))
            if (base_number - printMaximum(base_number)) < 0:
                correct_answers['q13'] = '>'
            elif (base_number - printMaximum(base_number)) == 0:
                correct_answers['q13'] = '='
            else:
                correct_answers['q13'] = '<'
            if (base_number % 2) == 0:
                correct_answers['q5'] = 'even'
            else:
                correct_answers['q5'] = 'odd'

            stored_values_thousandths = {
                  1: 0, # ones spot
                  2: 0, # tens spot
                  3: 0, # hundres spot
                  4: 0 # thousandths spot
                }
            for enum, value in enumerate(str(base_number)[::-1], 1):
                stored_values_thousandths[enum] = int(value)
                if enum == 1:
                    if stored_values_thousandths[1] == 0:
                        correct_answers['blocks1'] =  '0'
                    else:
                        correct_answers['blocks1'] = str(stored_values_thousandths[1])
                elif enum == 2:
                    if stored_values_thousandths[2] == 0:
                        correct_answers['blocks10'] =  '0'
                    else:
                        correct_answers['blocks10'] = str(stored_values_thousandths[2])
                elif enum == 3:
                    if stored_values_thousandths[3] == 0:
                        correct_answers['blocks100'] =  '0'
                    else:
                        correct_answers['blocks100'] = str(stored_values_thousandths[3])
                elif enum == 4:
                    if stored_values_thousandths[4] == 0:
                        correct_answers['blocks1000'] =  '0'
                    else:
                        correct_answers['blocks1000'] = str(stored_values_thousandths[4])
                else:
                    correct_answers['blocks1'] =  'error'
                    correct_answers['blocks10'] =  'error'
                    correct_answers['blocks100'] =  'error'
                    correct_answers['blocks1000'] =  'error'
            if correct_answers['blocks1000'] == '0':
                joined = ""
            elif correct_answers['blocks1000'] != '0' and correct_answers['blocks100'] == '0' and correct_answers['blocks10'] == '0' and correct_answers['blocks1'] == '0':
                joined += str(int(correct_answers['blocks1000'])*1000) 
            else:
                joined = str(int(correct_answers['blocks1000'])*1000) + '+'
            if correct_answers['blocks100'] == '0':
                joined += "" 
            elif correct_answers['blocks100'] != '0' and correct_answers['blocks10'] == '0' and correct_answers['blocks1'] == '0':
                joined += str(int(correct_answers['blocks100'])*100) 
            else:
                joined += str(int(correct_answers['blocks100'])*100) + '+'
            if correct_answers['blocks10'] == '0':
                joined += ""
            elif correct_answers['blocks10'] != '0' and correct_answers['blocks1'] == '0':
                joined += str(int(correct_answers['blocks10'])*10)                  
            else:
                joined += str(int(correct_answers['blocks10'])*10) + '+'
            if correct_answers['blocks1'] == '0':
                joined += ""                  
            else:
                joined += correct_answers['blocks1']              
            correct_answers['q4'] = joined
            correct_answers['tallies1000'] = correct_answers['blocks1000']            
            correct_answers['tallies100'] = correct_answers['blocks100']
            correct_answers['tallies10'] = correct_answers['blocks10']
            correct_answers['tallies1'] = correct_answers['blocks1']
            if equation == '':
                correct_answers['q11'] = 'Nothing'
            elif str(eval(equation)) == str(base_number):
                correct_answers['q11'] = str(equation)
            else:
                correct_answers['q11'] = str(correct_answers['q4'])
            return correct_answers

        def is_square_root(integer):
            root = math.sqrt(integer)
            low_root = int(root - 0.5) ** 2
            high_root = int(root + 0.5) ** 2
            return integer == int(root + 0.5) ** 2, low_root, high_root
        def is_prime(x):
            return factorial(x - 1)  % x == x - 1
        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        def printMaximum(num): 
          
            # Hashed array to store count of digits 
            count = [0 for x in range(10)] 
          
            # Converting given number to string 
            string = str(num) 
          
            # Updating the count array 
            for i in range(len(string)): 
                count[int(string[i])] = count[int(string[i])] +  1
          
            # Result stores final number 
            result = 0
            multiplier = 1
          
            # traversing the count array 
            # to calculate the maximum number 
          
            for i in range(10): 
                while count[i] > 0: 
                    result = result + ( i * multiplier ) 
                    count[i] = count[i] - 1
                    multiplier = multiplier * 10
          
            # return the result 
            return result 
        def check_answers(answers,correct_answers):
            checked = {"q1":None,"q2":None,"q3":None, "q4":None, "q5":None, "q6":None, "q7":None, "q8":None, "q9":None, "q10":None, "q11":None, "q12":None, "q13":None, "blocks1000":None, "blocks100":None, "blocks10":None, "blocks1":None, "tallies1000":None, "tallies100":None, "tallies10":None, "tallies1":None}
            for key, v1 in answers.items():
                try:
                    v2 = correct_answers[key]
                    if v1 != v2:
                        checked[key] = 'false'
                    else:
                        checked[key] = 'true'
                except KeyError:
                        checked[key] = 'error'
            return checked
        answers = {}
        placeholders = {"q1":"The number before is ","q2":"The number after is ","q3":"The word form is ", "q4":"The expanded form is ", "q5":"Odd or even? ", "q6":"The number 10 more is ", "q7":"The number 10 less is ", "q8":"The number 100 more is ", "q9":"The largest number using the digits is ", "q10":"The sum of the digits is ", "q11":"The possible equation is ", "q12":"The prime answer is ", "q13":"The largest number is ", "blocks1000":"It was ", "blocks100":"It was ", "blocks10":"It was ", "tallies1000":"It was ",  "tallies100":"It was ", "tallies10":"It was ", "tallies1":"It was ", "blocks1":"It was "}
        req = request.form
        for i in req:
            key = str(i)
            answers.update({key : str(req.get(i).lower()).strip()})
        app.logger.debug(answers)
        correct_answers = generate_answers(int(answers['master_number']),answers['q11'])
        app.logger.info(correct_answers)
        checked = check_answers(answers,correct_answers)
        if checked['q12'] == 'false' or answers['q12'] == 'None':
            n = int(answers['master_number'])
            for i in range(2, n):   # only odd numbers
                if n%i==0:
                    correct_answers['q12'] = str(n) + ' can be divided by ' + str(i)
                
        app.logger.info(checked)
        for key, value1 in checked.items():
            try:
                value2 = correct_answers[key]
                value3 = placeholders[key]
                
                if key != 'master_number':
                    if value1 == 'true':
                        flash(key + ' was correct.', 'bg-success')
                        flash('You entered ' + value2, 'bg-success')
                    else:
                        flash(key + ' was incorrect. ', 'bg-danger')
                        flash(value3 + value2, 'bg-danger')
            except KeyError:
                 continue
        return render_template('index.html', input_number=answers['master_number'])
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')