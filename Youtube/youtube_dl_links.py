#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:23:18 2020

@author: kodiuser
"""
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import youtube_dl
import re

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/mnt/oldmedialib/youtubedl/%(title)s-%(id)s.%(ext)s',
    'continuedl': 'true',
    'download_archive': '/mnt/oldmedialib/youtubedl/archive.txt',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'

    }]
}
outdir = '/mnt/oldmedialib/youtubedl'
browser = webdriver.Chrome()

browser.get("https://www.youtube.com/user/Fluidified/videos")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 30

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

user_data = browser.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))


job_size = len(links)
count =0
wait = WebDriverWait(browser, 10)
regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
for x in links:
    if (x == 'https://www.youtube.com/watch?v=YCrSQd2FqcU'):
        print("Skipped download of " + x)
        continue
    else:
        browser.get(x)
        #time.sleep(10)
        #check_ad()
        v_id = regex.match(x)
        v_title = wait.until(EC.presence_of_element_located(
                       (By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
        #v_duration = browser.find_element_by_class_name("ytp-time-duration").text
        dlink = "https://www.youtube.com/watch?v=" + v_id.group('id')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            with open(outdir + '/videos.txt', 'a+') as file:
                file.write(dlink + "\n")
            file.close()
            #ydl.download([dlink])
        count += 1
        print("****************************************************************************************************")
        print("Completed " + v_title + " \nSo we have completed " + str(count) + "/" + str(job_size))
        print("****************************************************************************************************")


 No newline at end of file
