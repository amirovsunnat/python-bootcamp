import smtplib

import requests

API_KEY = "your_api_key"
OWT_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 41.299496,
    "lon": 69.240074,
    "appid": API_KEY,
    "cnt": 4,
}
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_password"

response = requests.get(url=OWT_API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_codes = []
for hourly_data in weather_data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if condition_code < 700:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Rain is going to happen.\n\n"
                    "Today will be rain. Do not forget to take an "
                    "☔")

