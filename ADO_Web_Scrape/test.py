#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:10:16 2020

@author: kodiuser
"""

import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Attacker Dice')],
            [sg.Checkbox('One Die', enable_events=True),sg.Checkbox('Two Dice', enable_events=True),sg.Checkbox('Three Dice', enable_events=True)],
            [sg.Text('_'  * 80)],
            [sg.Text('Defender Dice')],
            [sg.Checkbox('One Die', enable_events=True),sg.Checkbox('Two Dice', enable_events=True)],
            [sg.Text('_'  * 80)],
            [sg.Button('Roll'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Dice roller for RISK', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    elif event in (None, 'Roll'):	# if user closes window or clicks cancel
        print('Muppet')


window.close()