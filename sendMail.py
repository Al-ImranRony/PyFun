# Sending mail using python

import smtplib

password = input("Enter password: ")

sender = "imranrony687@gmail.com"
receiver = "abirhasanmubin@gmail.com"
message = "Hello there !"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
print("Login success.")
server.sendmail(sender, receiver, message)
print("Email sent.")
