import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "yourpassword"

data = pandas.read_csv("birthdays.csv")
data_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now().day
current_month = dt.datetime.now().month
tod_month = today, current_month
if tod_month in data_dict:
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        letter = letter_file.read().replace("[NAME]", data_dict[tod_month]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=data_dict[tod_month]["email"],
            msg=f"Subject: Happy Birthday\n\n{letter}"
        )





