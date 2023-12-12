import datetime as dt
import smtplib
from random import choice

# get random quote
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote = choice(quotes)
        print(quote)

    # send quote to our own email
    MY_EMAIL = "yourmail@gmail.com"
    MY_PASSWORD = "yourpassword"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivations\n\n{quote}")
