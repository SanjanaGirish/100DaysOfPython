import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ACCESS_KEY = "* ENTER DATA HERE *"
NEWS_API_KEY = "* ENTER DATA HERE *"
account_sid = "* ENTER DATA HERE *"
auth_token = "* ENTER DATA HERE *"

stock_parameters = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK_NAME,
                    "outputsize": "compact",
                    "datatype": "json",
                    "apikey": ACCESS_KEY}

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before
# yesterday then print("Get News").

# Get yesterday's closing stock price.
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()
stock_close_prices = [value['4. close']
                      for (key, value) in data['Time Series (Daily)'].items()]
current_dates = [k for (k, v) in data['Time Series (Daily)'].items()]


yesterday_close_price = float(stock_close_prices[0])
day_before_close_price = float(stock_close_prices[1])

if day_before_close_price < yesterday_close_price:
    symbol = "🔺"
elif day_before_close_price > yesterday_close_price:
    symbol = "🔻"
else:
    symbol = ""

# Find the positive difference between the two
diff_stock_price = abs(day_before_close_price - yesterday_close_price)

# Work out the percentage difference in price between closing price yesterday
# and closing price the day before yesterday.
percentage_diff = round((diff_stock_price / day_before_close_price) * 100, 2)

# If percentage is greater than 5 then print("Get News").
new_params = {"q": COMPANY_NAME,
              "from": current_dates[1],
              "apiKey": NEWS_API_KEY}
if percentage_diff > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=new_params)
    news_data = news_response.json()
# Use Python slice operator to create a list that contains the first 3 articles.
    main_articles = news_data['articles'][:3]
    # Create a new list of the first 3 article's headline and description
    main_article_details = [(item['title'], item["description"])
                            for item in main_articles]

    # Use twilio.com/docs/sms/quickstart/python
    client = Client(account_sid, auth_token)

    # Send each article as a separate message via Twilio.
    for item in main_article_details:
        message_text = f"TSLA: {symbol}{percentage_diff}\nHeadline: {item[0]}\n" \
                  f"Brief: {item[1]}"
        message = client.messages \
            .create(body=message_text,
                    from_='* ENTER TRIAL NUMBER *',
                    to='* ENTER YOUR PHONE NUMBER *')
        print(message.status)

# Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
and prominent investors are required to file by the SEC The 13F filings show 
the funds' and investors' portfolio positions as of March 31st, near the height
 of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds...
"""

