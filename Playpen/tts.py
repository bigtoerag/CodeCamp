#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:10:24 2020

@author: kodiuser
"""
import random
from random import randint
from gtts import gTTS
import os

lang = 'en-au'
my_name = 'Zachary'
my_age = randint(1, 9)
cloudy = ['yes', 'no'] 
rainy = ['yes','no']
day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
week_day = random.choice(day)
cloudy_day = random.choice(cloudy)
rainy_day = random.choice(rainy)
my_book = ['Harry Potter', 'Diary of an 8bit warrior', 'Minecraft anything']
my_love = random.getrandbits(1)

if week_day == 'saturday' or week_day == 'sunday':
        tts = gTTS(text='Its the weekend, so its time to party!', lang=lang)
        tts.save("message.mp3")
        os.system("mpg321 message.mp3")    
else:
    if my_age >= 6 and my_book == 'Harry Potter':
        message = my_name + ' loves ' + random.choice(my_book) + ' more than ' + random.choice(my_book)
        tts = gTTS(text=message, lang=lang)
        tts.save("message.mp3")
        os.system("mpg321 message.mp3")
    elif cloudy_day == 'yes' and my_age <= 6:
        message = my_name + ' would rather read ' + random.choice(my_book) + ' than ' + random.choice(my_book)
        tts = gTTS(text=message, lang=lang)
        tts.save("message.mp3")
        os.system("mpg321 message.mp3")         
    elif rainy_day == 'yes' and my_age <= 6:
        message = my_name + ' really loves to huddle up warm and read ' + random.choice(my_book) + ' on colder days'
        tts = gTTS(text=message, lang=lang)
        tts.save("message.mp3")
        os.system("mpg321 message.mp3")         
    else:
        message = my_name + ' loves running around in the sun. But he is not good at putting on suncream!'
        tts = gTTS(text=message, lang=lang)
        tts.save("message.mp3")
        os.system("mpg321 message.mp3")