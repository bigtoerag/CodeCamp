# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib, ssl

now = datetime.now()
url = "https://www.cityofsydney.nsw.gov.au/explore/facilities/sports-facilities"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')
#First lets get the HTML of the table called site Table where all the links are displayed
field_name = soup.find("td",attrs={'id':'Sports field followed by its current status_td1_0'})
field_status = soup.find("td",attrs={'id':'Sports field followed by its current status_td1_1'})

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "htoobsucram@gmail.com"  # Enter your address
receiver_email = "subscribe@marcusandzoe.com"  # Enter receiver address
password = "hqyrriywicegplks"

if "Closed" in field_status.text:
    subject = 'The current status shows ' + field_name.text + ' is Closed'
    body = 'Latest Update @' + now.strftime("%d/%m/%Y %H:%M:%S") + ' from the Official Website - https://www.cityofsydney.nsw.gov.au/explore/facilities/sports-facilities'
else:
    subject = 'The current status, as of ' + now.strftime("%d/%m/%Y %H:%M:%S") + ' shows ' + field_name.text + ' is ' + field_status.text
    body = 'Latest Update from the Official Website - https://www.cityofsydney.nsw.gov.au/explore/facilities/sports-facilities'
    
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender_email, receiver_email, subject, body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, email_text)