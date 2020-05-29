#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:06:36 2020

@author: kodiuser
"""
from PIL import Image
from PIL import ExifTags
import os
import subprocess
import imghdr

def get_date(path):
    exifData = {}
    img = Image.open(path)
    exifDataRaw = img.getexif()
    for tag, value in exifDataRaw.items():
        decodedTag = ExifTags.TAGS.get(tag, tag)
        exifData[decodedTag] = value
        if decodedTag == 'DateTimeOriginal':
            print(decodedTag, value)#[0:7].replace(':','-'))
            break
        else:
            continue

path = '/home/kodiuser/Pictures'
#files = subprocess.call(["find",path,"-maxdepth","1","-type","f"])
for file in subprocess.check_output(["find",path,"-maxdepth","1","-type","f"], universal_newlines=True).split('\n'):
    print(file)
    print(get_date(file))


