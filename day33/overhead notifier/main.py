import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 41.299496
MY_LONG = 69.240074


def is_iss_close():
    """Returns true if iss close to our location, otherwise false."""
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data_of_iss = res.json()

    iss_latitude = float(data_of_iss["iss_position"]["latitude"])
    iss_longitude = float(data_of_iss["iss_position"]["longitude"])
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_night():
    """Returns true if it is night otherwise false."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    return sunset <= time_now <= sunrise


MY_EMAIL = "youremail"
MY_PASSWORD = "yourpassword"

while True:
    time.sleep(100)
    if is_night() and is_iss_close():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:LOOK UP ON THE SKY☝️\n\nISS came close.Look up to see it.")



