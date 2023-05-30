import pandas as pd
import requests
import pytz
from datetime import datetime
from telegram import Bot

bot_token = "5963451255:AAGPxyC1fAWr_m-rugp5332ljeGN8HPL_hU"
channel_id = "-1001621135988"

url = 'https://economic-calendar.tradingview.com/events'
today = pd.Timestamp.today().normalize()
now = datetime.now(pytz.timezone('America/New_York'))

payload = {
    'from': (today + pd.offsets.Hour(23)).isoformat() + '.000Z',
    'to': (today + pd.offsets.Day(7) + pd.offsets.Hour(22)).isoformat() + '.000Z',
    'countries': ','.join(['US', 'CH', 'EU', 'AU', 'JP', 'GB', 'CA', 'NZ'])
}
data = requests.get(url, params=payload).json()
df = pd.DataFrame(data['result'])

# Aseguramos que la columna "date" es de tipo datetime y está en UTC
df['date'] = pd.to_datetime(df['date'], utc=True)

# Convertimos la columna "date" a la zona horaria de Nueva York
df['date'] = df['date'].dt.tz_convert('America/New_York')

# Filtramos los valores de 0 y 1 en la columna "importance"
df_filtered = df[df['importance'].isin([0, 1])]

# Seleccionamos solo las columnas que necesitamos
df_filtered = df_filtered[['title', 'country', 'importance', 'date']]

# Renombramos los valores 0 y 1 de la columna "importance" a "Medio" y "Alto"
df_filtered['importance'] = df_filtered['importance'].replace({0: 'Medio', 1: 'Alto'})

# Creamos el bot
bot = Bot(token=bot_token)


for index, row in df_filtered.iterrows():
        message = f"""
        - {row['date'].strftime('%d/%m/%Y')}
        - {row['country']}
        - {row['title']}
        - {row['importance']}
        """

# Enviamos el DataFrame como mensaje a Telegram
bot.send_message(chat_id=channel_id, text=str(message))



'''El de abajo podría ser el código final, pero no lo he probado'''	

# import pandas as pd
# import requests
# import pytz
# import time
# from datetime import datetime
# from telegram import Bot

# def send_info():
#     url = 'https://economic-calendar.tradingview.com/events'
#     today = pd.Timestamp.today().normalize()
#     now = datetime.now(pytz.timezone('America/New_York'))

#     payload = {
#         'from': (today + pd.offsets.Hour(23)).isoformat() + '.000Z',
#         'to': (today + pd.offsets.Day(7) + pd.offsets.Hour(22)).isoformat() + '.000Z',
#         'countries': ','.join(['US', 'CH', 'EU', 'AU', 'JP', 'GB', 'CA', 'NZ'])
#     }
#     data = requests.get(url, params=payload).json()
#     df = pd.DataFrame(data['result'])

#     df['date'] = pd.to_datetime(df['date'], utc=True)
#     df['date'] = df['date'].dt.tz_convert('America/New_York')

#     df_filtered = df[df['importance'].isin([0, 1])]
#     df_filtered = df_filtered[['title', 'country', 'importance', 'date']]
#     df_filtered['importance'] = df_filtered['importance'].replace({0: 'Medio', 1: 'Alto'})

#     message = df_filtered.to_string()
#     bot = Bot(token='YOUR_BOT_TOKEN')
#     bot.send_message(chat_id='YOUR_CHANNEL_ID', text=message)

# while True:
#     now = datetime.now(pytz.timezone('America/New_York'))
#     if now.weekday() == 0 and now.hour == 6:  # Check if it's Monday at 6 a.m.
#         send_info()
#     time.sleep(60)  # Wait for 60 seconds before checking the time again
