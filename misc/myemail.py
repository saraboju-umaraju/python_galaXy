#!/usr/bin/python3
import smtplib
server = smtplib.SMTP("smtp.gmail.com" , 587)
server.ehlo()
server.starttls()
