#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:23:14 2020

@author: kodiuser
"""
import os
import eyed3

directory = '/mnt/medialib/MP3/Music/Compilations/YouTubeDownloads/Deep Legacy/'
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        file = directory + filename
        cover = directory + os.path.splitext(filename)[0] + '.jpg'
        # load tags
        audiofile = eyed3.load(file)
        print(cover)
        # read image into memory
        imagedata = open(cover,"rb").read()
        # append image to tags
        audiofile.tag.images.set(3,imagedata,"image/jpeg",u"you can put a description here")
        # write it back
        audiofile.tag.save()
        continue
    else:
        print("Not the required file type")
        continue
