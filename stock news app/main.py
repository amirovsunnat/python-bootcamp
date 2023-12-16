import smtplib

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# API KEYS
STOCK_API_KEY = "your_stock_api_key"
NEWS_API_KEY = "news_api_key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for key, value in stock_data.items()]

yesterday_price = stock_data_list[0]["4. close"]
day_before_yes_price = stock_data_list[1]["4. close"]

# find the difference
difference = abs(float(yesterday_price) - float(day_before_yes_price))
print(difference)

# find difference in percentage
difference_percentage = round((difference / float(yesterday_price)) * 100)
print(difference_percentage)

if difference_percentage > 0:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    # request news api
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    news_articles = news_data["articles"]
    three_top_articles = news_articles[:3]
    edited_articles = [f"Headline: {article['title']}\nBrief: {article['description']}"
                       for article in three_top_articles]
    # send email
    if difference_percentage > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"

    MY_EMAIL = "your_email_address"
    MY_PASSWORD = "your password"
    for article in edited_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: {STOCK}: {emoji}{difference_percentage}%\n\n{article}")
