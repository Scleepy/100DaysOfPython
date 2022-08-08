import smtplib
import datetime as dt
import random
import pandas as pd

email = "enteremail@mail.com"
password = "password"

destination_email = "destination@mail.com"

time_now = dt.datetime.now()
current_month = time_now.month
current_day = time_now.day

current_info = (current_month, current_day)

birthday_data = pd.read_csv("birthdays.csv")
birthday_dictionary = {(row["month"], row["day"]): row for (index, row) in birthday_data.iterrows()}
print(birthday_dictionary)

if current_info in birthday_dictionary:
    complete_info = birthday_dictionary[current_info]
    letter_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

    print("ITS SOMEONES'S BIRTHDAY TODAY")

    with open(letter_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", complete_info["name"])

        print(content)

        with smtplib.SMTP("smtp.gmail.com") as connection: #Connect to server, smtp.mail.yahoo.com for yahoo mail
            connection.starttls() #Creating secure connection by encrypting message
            connection.login(user=email, password=password)

            connection.send(
                from_addr=email, 
                to_addr=complete_info["email"], 
                msg=f"Subject:Happy Birthday\n\n{content}"
            )