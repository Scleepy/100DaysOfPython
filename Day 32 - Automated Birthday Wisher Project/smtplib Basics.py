import smtplib

email = "enteremail@mail.com"
password = "password"

destination_email = "destination@mail.com"

with smtplib.SMTP("smtp.gmail.com") as connection: #Connect to server, smtp.mail.yahoo.com for yahoo mail
    connection.starttls() #Creating secure connection by encrypting message
    connection.login(user=email, password=password)

    connection.send(
        from_addr=email, 
        to_addr=destination_email, 
        msg="Subject:Hello\n\nLorem Ipsum"
    )
