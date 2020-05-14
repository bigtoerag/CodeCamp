# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = datetime.now()
url = "https://www.cityofsydney.nsw.gov.au/explore/facilities/sports-facilities"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
request = urllib.request.Request(url,headers={'User-Agent': user_agent})
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')
#First lets get the HTML of the table called site Table where all the links are displayed
field_name = soup.find("td",attrs={'id':'Sports field followed by its current status_td1_0'})
field_status = soup.find("td",attrs={'id':'Sports field followed by its current status_td1_1'})
tick = 'https://getdrawings.com/free-icon/tick-icon-61.png'
cross = 'https://p7.hiclipart.com/preview/217/368/931/x-mark-drawing-red-check-mark-cross.jpg'

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email =   # Enter your address
receiver_email =   # Enter receiver address
password =

if "Open" not in field_status.text:
    status_image = cross
    button_border = '#ff0000'
else:
    status_image = tick
    button_border = '#4CAF50'

subject = 'The current status, as of ' + now.strftime("%H:%M:%S") + ' shows ' + field_name.text + ' is ' + field_status.text
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
text = "Latest Update @" + now.strftime("%d/%m/%Y %H:%M:%S") + "from the Official Website - https://www.cityofsydney.nsw.gov.au/explore/facilities/sports-facilities"
html = """<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>ADO Ground Status Email</title>
  <style type="text/css">
  body {margin: 0; padding: 0; min-width: 100%!important;}
  img {height: auto;}
  .content {width: 100%; max-width: 600px;}
  .header {padding: 0 0 0 0;}
  .innerpadding {padding: 5px 5px 5px 5px;}
  .borderbottom {border-bottom: 1px solid #000000;}
  .subhead {font-size: 15px; color: #ffffff; font-family: sans-serif; letter-spacing: 10px;}
  .h1, .h2, .bodycopy {color: #153643; font-family: sans-serif;}
  .h1 {font-size: 24px; line-height: 28px; font-weight: bold;}
  .h2 {padding: 0 0 5px 0; font-size: 20px; line-height: 28px; font-weight: bold;}
  .bodycopy {font-size: 14px; line-height: 22px;}
  .button {color: #fcfcfc; text-align: center; font-size: 18px; font-family: sans-serif; font-weight: bold; padding: 0 30px 0 30px; border: 2px solid """ + button_border + """;}
  .button a, a:link, a:visited, a:focus {color: """ + button_border + """ !important; text-decoration: none !important;}
  .footer {padding: 5px 5px 5px 5px;}
  .footercopy {font-family: sans-serif; font-size: 10px; color: #000;}
  .footercopy a {color: #ffffff; text-decoration: underline;}

  @media only screen and (max-width: 550px), screen and (max-device-width: 550px) {
  body[yahoo] .hide {display: none!important;}
  body[yahoo] .buttonwrapper {background-color: transparent!important;}
  body[yahoo] .button {padding: 0px!important;}
  body[yahoo] .button a {background-color: #e05443; padding: 15px 15px 13px!important;}
  body[yahoo] .unsubscribe {display: block; margin-top: 20px; padding: 10px 50px; background: #2f3942; border-radius: 5px; text-decoration: none!important; font-weight: bold;}
  }

  /*@media only screen and (min-device-width: 601px) {
    .content {width: 600px !important;}
    .col425 {width: 425px!important;}
    .col380 {width: 380px!important;}
    }*/

  </style>
</head>

<body yahoo bgcolor="#fff">
<table width="100%" bgcolor="#fff" border="0" cellpadding="0" cellspacing="0">
<tr>
  <td>
    <!--[if (gte mso 9)|(IE)]>
      <table width="600" align="center" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td>
    <![endif]-->
    <table bgcolor="#ffffff" class="content" align="center" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td bgcolor="#fff" class="header">
          <table width="30%" align="center" border="0" cellpadding="0" cellspacing="0">
            <tr>
              <td height="" style="padding: 0 0 0 0;">
                <img class="" src="https://live.staticflickr.com/4019/4336679185_daa059e597_b.jpg" width="380px" height="" border="0" alt="" />
              </td>
            </tr>
          </table>
         </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td class="h2" align="center">
                The ADO ground status is """ + field_status.text + """
              </td>
            </tr>
            </table>
        </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
                    <!--[if (gte mso 9)|(IE)]>
            <table width="100%" align="left" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
          <![endif]-->
          <table width="100%" align="left" border="0" cellpadding="0" cellspacing="0">
            <tr>
              <td height="115" style="padding: 0 20px 20px 0;">
                <img class="fix" src=""" + status_image + """ width="115" height="115" border="0" alt="" />
              </td>
               <td>
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td class="bodycopy">
                      As of """ + now.strftime("%H:%M %p") + """ today the ground status was checked on the official council website.
                For further detailed info click on the button.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding: 20px 0 0 0;">
                      <table class="buttonwrapper" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td class="button" height="45">
                            <a href="https://www.cityofsydney.nsw.gov.au/explore/facilities/sports-facilities">Sports Facilities</a>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
                </td>
              </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <tr>
        <td class="footer" bgcolor="#fff">
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td align="center" class="footercopy">
                &reg; <i>Marcus using Python 2020</i>

              </td>
            </tr>
            </table>
        </td>
      </tr>
    </table>
    <!--[if (gte mso 9)|(IE)]>
          </td>
        </tr>
    </table>
    <![endif]-->
    </td>
  </tr>
</table>
</body>
</html>"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
