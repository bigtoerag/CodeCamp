#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:19:16 2020

@author: kodiuser
"""

from flask import Flask, render_template, request
import random
import astor
import ast
import numpy as np

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        num_dice = 0
        roll_result = []
        size=0
        def operands():
            signs = ['+','-']
            operand = random.choice(signs)
            return operand
        
        def fix(formula):
            def recurse(node):
                result = ''
                if isinstance(node, ast.BinOp):
                    if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
                        result += '('
                    result += recurse(node.left)
                    result += recurse(node.op)
                    result += recurse(node.right)
                    if isinstance(node.op, ast.Mult) or isinstance(node.op, ast.Div):
                        result += ')'
                elif isinstance(node, ast.Add):
                    result += '+'
                elif isinstance(node, ast.Sub):
                    result += '-'
                elif isinstance(node, ast.Mult):
                    result += '*'
                elif isinstance(node, ast.Div):
                    result += '/'
                elif isinstance(node, ast.Num):
                    result += str(node.n)
                else:
                    for child in ast.iter_child_nodes(node):
                        result += recurse(child)
                return result
            
            
            def search_expr(node):
                returns = []
                for child in ast.iter_child_nodes(node):
                    if isinstance(child, ast.Expr):
                        return child
                    returns.append(search_expr(child))
                for ret in returns:
                    if isinstance(ret, ast.Expr):
                        return ret
                return None
            a = ast.parse(formula)
            expr = search_expr(a)
            output = recurse(expr)
            return output
            
        def result(size):
            if size == '1':
                #generate 1 random die
                result = np.random.randint(1,6, size=int(size))
                equation = 'You didnt choose enough dice for an equation!'
                answer = 'Ploop'
            elif size == '2':
                #generate 2 random dice
                result = np.random.randint(1,6, size=int(size))
                equation = str(result[0]) + operands() + str(result[1])
                answer = eval(equation)
            elif size == '3':
                #generate 3 random dice
                result = np.random.randint(1,6, size=int(size))
                equation = str(result[0]) + operands() + str(result[1]) + operands() + str(result[2])
                answer = eval(equation)
            elif size == '4':
                #generate 4 random dice
                result = np.random.randint(1,6, size=int(size))
                equation = str(result[0]) + operands() + str(result[1]) + operands() + str(result[2]) + operands() + str(result[3])
                answer = eval(equation)
            elif size == '5':
                #generate 5 random dice
                result = np.random.randint(1,6, size=int(size))
                equation = str(result[0]) + operands() + str(result[1]) + operands() + str(result[2]) + operands() + str(result[3]) + operands() + str(result[4])
                answer = eval(equation)
            elif size == '6':
                #generate 2 random dice
                result = np.random.randint(1,6, size=int(size)*5)
                equation = str(result[0]) + operands() + str(result[1]) + operands() + str(result[2]) + operands() + str(result[3]) + operands() + str(result[4]) + operands() + str(result[5])
                answer = eval(equation)
            else:
                roll_err = 'Nothing worked'
                return roll_err
            #equation = fix(equation)
            return equation, size, answer
        req = request.form
        num_dice = req.get('dice')
        roll_result = result(num_dice)
        if num_dice == '1':
            formatted_equation = roll_result[0]
        else:
            formatted_equation = fix(roll_result[0])
        app.logger.info(formatted_equation)
        return render_template('index_multi_dice_roll.html',formatted_equation=formatted_equation, roll_result=roll_result, size=size)

    else:
        return render_template('index_multi_dice_roll.html')
     
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')