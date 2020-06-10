#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:56:25 2020

@author: kodiuser
"""

# Importing all necessary libraries 
import cv2 
import os 

# Read the video from specified path 
cam = cv2.VideoCapture("/home/kodiuser/Videos/56767491_267242774021945_2664444745178152960_n.mp4") 

# frame 
currentframe = 0
#extract every x frames as defined by the increment so you can jump static points such as PPT videos
increment = 10

while(True): 
	
	# reading from frame 
	ret,frame = cam.read() 

	if ret: 
		# if video is still left continue creating images 
		name = '/home/kodiuser/Documents/export/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name) 

		# writing the extracted images 
		cv2.imwrite(name, frame) 

		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += increment
	else: 
		break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
