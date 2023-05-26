import requests
from datetime import date, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = os.getenv("STOCK_NAME")
COMPANY_NAME = os.getenv("COMPANY_NAME")
STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "it"
    }

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()
    all_articles = (data['articles'])
    return all_articles

def get_previous_date_from_timestap(timestamp):
    year = timestamp[0:4]
    month = timestamp[5:7]
    day = timestamp[8:10]
    last_date = date(int(year), int(month), int(day))
    return last_date - timedelta(1)


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "30min",
    "apikey": ALPHAVANTAGE_API_KEY
}

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()

last_refreshed = (data['Meta Data']['3. Last Refreshed'])
today_close = float(data['Time Series (30min)'][last_refreshed]['4. close'])

# alternative through list comprehension
# list_of_close = [value['4. close'] for (key, value) in data['Time Series (30min)'].items()]
# close = (list_of_close[0])

# TODO 2. - Get the day before yesterday's closing stock price

previous_date = get_previous_date_from_timestap(last_refreshed)

closes_previous_day = [value for (key, value) in data['Time Series (30min)'].items() if str(previous_date) in key]
close_previous_day = float(closes_previous_day[0]['4. close'])


# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
up_down = None
difference = (close_previous_day - today_close)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_perc = round(difference*100/close_previous_day)


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

print(diff_perc)
if abs(diff_perc) >= 0:  # just to test, it should be 5
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    all_articles = get_news()

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_3_articles = all_articles[:3]

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    new_list = [f"{STOCK_NAME}: {up_down} {abs(diff_perc)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_3_articles]
    print(new_list)

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.


# TODO 9. - Send each article as a separate message via Twilio.

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

