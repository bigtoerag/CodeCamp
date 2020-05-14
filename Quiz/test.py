#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:38:04 2020

@author: kodiuser
"""
import pickle

# load the previous score if it exists
try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0

print ("High score: %d" % score)

# your game code goes here
# let's say the user scores a new high-score of 10

# save the score
with open('score.dat', 'wb') as file:
    pickle.dump(score, file)