import smtplib

import requests
from bs4 import BeautifulSoup
import lxml
EMAIL = ""
PASSWORD = ""

url = ("https://www.amazon.com/Apple-MacBook-Laptop-14%E2%80%91core-30%E2%80%91core/dp/B0CM5GX9MF/"
       "ref=sr_1_1?crid=20WA2E9U9ZA81&keywords=macbook%2Blatest%2Bmodel%2B2024&qid=1706352160&sprefix"
       "=macbook%2Blatest%2Bmodel%2B202%2Caps%2C340&sr=8-1&th=1")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,uz;q=0.8,ru;q=0.7"
}

request = requests.get(url, headers=header)
request.raise_for_status()

soup = BeautifulSoup(request.content, "lxml")

# Find the price span
price = soup.find(name="span", class_="a-offscreen")

if price:
    # Extract the text and remove the currency symbol
    price_text = price.text.strip().replace('$', '')

    # Convert the price to float
    price_as_float = float(price_text)
    print(price_as_float)

    # if price exists then we will to check it
    if float(price) < 1999:
        message = f"Mackbook's price is lower than 1999, exactly it is ${price}, hurry up to buy!"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
else:
    print("Price not found.")

