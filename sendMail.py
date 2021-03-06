# Sending mail using python

import os
import imghdr
import smtplib
from email.message import EmailMessage

Email_Address = os.environ.get('Email_User')
Email_Password = os.environ.get('Email_Pass')

contacts = ['imranrony831@gmail.com', 'imranrony537@outlook.com']

msg = EmailMessage()
msg['Subject'] = "Give a subject"
msg['From'] = Email_Address
msg['To'] = ', '.join(contacts) 
msg.set_content("Details of subject..")

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:gray;">This is a HTML email ! </h1>
    </body>
</html>
""", subtype='html')

files = ['sunset.jpg', 'colorPhoto.jpg']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

# For sending pdf or other files like pdf  maintype='application' & subtype='octet-stream' 
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(Email_Address, Email_Password)

    server.send_message(msg)
    print("Email sent.")
