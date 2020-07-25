#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:37:03 2020
  
{
    "time": "00:00",
    "quote_first": "As ",
    "quote_time_case": "midnight",
    "quote_last": " was striking bronze blows upon the dusky air, Dorian Gray, dressed commonly, and with a muffler wrapped round his throat, crept quietly out of his house.",
    "title": "The Picture of Dorian Gray",
    "author": "Oscar Wilde"
  },
  
@author: kodiuser
"""
import re
import json
filepath = '/home/kodiuser/Documents/Lit_Clock/litclock_annotated.csv'
thisdict = {}
y = ""
with open(filepath) as fp:
   for line in fp:
       line_items = str(line).split('|');
       print(line_items);
       thisdict["time"] = line_items[0];
       thisdict["quote_first"] = re.split('(.*?)\.*'+line_items[1], line_items[2], re.IGNORECASE)[1];
       thisdict["quote_time_case"] = line_items[1];
       thisdict["quote_last"] = re.split('(.*?)\.*'+line_items[1], line_items[2], re.IGNORECASE)[2];
       thisdict["title"] = line_items[3].rstrip();
       thisdict["author"] = line_items[4].rstrip(' \n');
       
       y += json.dumps(thisdict)+','
       print(y+'\n')
