import smtplib
import datetime as dt
import random

email = "enteremail@mail.com"
password = "password"

destination_email = "destination@mail.com"

time_now = dt.datetime.now()
time_weekday = time_now.weekday()

if(time_weekday == 0):
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection: #Connect to server, smtp.mail.yahoo.com for yahoo mail
        connection.starttls() #Creating secure connection by encrypting message
        connection.login(user=email, password=password)

        connection.send(
            from_addr=email, 
            to_addr=destination_email, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
