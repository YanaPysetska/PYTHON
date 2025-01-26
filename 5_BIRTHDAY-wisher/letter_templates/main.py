import random
import pandas
import datetime as dt
import smtplib
from settings import FROM_EMAIL,PASSWORD

now = dt.datetime.now()
month=now.month
day=now.day

#Dictionary from birthdays.csv:
data = pandas.read_csv("birthdays.csv")
records = data.to_dict(orient='records')

#___________________Letters_____________________
with open("letter_1.txt", "r") as f1:
    message_body = f1.read()
with open("letter_2.txt", "r") as f2:
    message_body_2 = f2.read()
with open("letter_3.txt", "r") as f3:
    message_body_3 = f3.read()

letters=[message_body,message_body_2,message_body_3]


for record in records:
    if record.get('month') == month and record.get('day') == day:
        txt = random.choice(letters)
        birthday_message = txt.replace("[NAME]", record['name'])
        FROM_EMAIL = FROM_EMAIL
        TO_EMAIL = record['email']
        PASSWORD = PASSWORD
        connection=smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(FROM_EMAIL,
                            TO_EMAIL,
                            birthday_message
                            )
        print('sent')
        connection.close()
        break
    else:
        print('There is no birthday today')












