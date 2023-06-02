import requests
import pandas as pd
from datetime import datetime, timedelta
import pytz

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
apikey = "X6TLMVBZSSL8LOJG"

# Calculate the current time and the time one hour ago
now = pd.Timestamp.now(pytz.utc)
one_hour_ago = now - pd.Timedelta(hours=1)

# Format the times
formatted_now = now.strftime('%Y%m%dT%H%M')
formatted_one_hour_ago = one_hour_ago.strftime('%Y%m%dT%H%M')

topics = ["blockchain","financial_markets","economy_macro","finance","technology"]

news_data = []

def convert_datetime(x):
    if x is not None:
        return datetime.strptime(x, '%Y%m%dT%H%M%S')
    else:
        return None

for topic in topics:

    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics={topic}&time_from={formatted_one_hour_ago}&time_to={formatted_now}&sort=LATEST&limit=1&apikey={apikey}"

    r = requests.get(url)
    data = r.json()
    
    if 'feed' in data:
        for news_item in data['feed']:
            news_info = {}
            news_info['title'] = news_item.get('title', None)
            news_info['published_time'] = convert_datetime(news_item.get('time_published', None))
            
            # Check if source is a dictionary
            if isinstance(news_item.get('source', {}), dict):
                news_info['source'] = news_item.get('source', {}).get('name', None)
            else:
                news_info['source'] = news_item.get('source', None)
                
            news_info['summary'] = news_item.get('summary', None)
            news_data.append(news_info)

# Convert to dataframe for easier manipulation
df = pd.DataFrame(news_data)
print(df)