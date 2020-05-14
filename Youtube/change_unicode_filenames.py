#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:23:14 2020

@author: kodiuser
"""

import os
import re
import sys

crapola = ["🌱","🍉","🌴","🍍","🍓","☘","🌿","&","♫"]

directory = '/mnt/oldmedialib/youtubedl'
os.chdir(directory)
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        for i in crapola:
            newfilename = filename.replace(i,"-")
            print(filename)
            if newfilename != filename:
                fullpath = os.path.join(directory, filename)
                newfullpath = os.path.join(directory, newfilename)
                print('Yay -' + newfilename)
                os.rename(f'{fullpath}', f'{newfullpath}')
                print('Changed -' + filename)
                print('To -'+ newfilename)
                break
            else:
                continue
        continue
    else:

        print("Not the required file type")
        continue
