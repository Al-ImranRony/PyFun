# Sending mail using python

import os
import imghdr
import smtplib
from email.message import EmailMessage

Email_Address = os.environ.get('Email_User')
Email_Password = os.environ.get('Email_Pass')

msg = EmailMessage()
msg['Subject'] = "Give a subject"
msg['From'] = Email_Address
msg['To'] = 'imranrony831@gmail.com'
msg.set_content("Image attached...")

with open('sunset.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
 
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(Email_Address, Email_Password)

    server.send_message(msg)
    print("Email sent.")
