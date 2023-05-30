# chat id the quant company: "-1001621135988"
# chat id prueba: "-1001938210460"


'''El de abajo podría ser el código final, pero no lo he probado'''	

import pandas as pd
import requests
import pytz
import time
from datetime import datetime
from telegram import Bot

def country_to_emoji(country_code):
    offset = ord('🇦') - ord('A')
    return ''.join(chr(ord(c) + offset) for c in country_code)

def send_info():
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

    df['date'] = pd.to_datetime(df['date'], utc=True)
    df['date'] = df['date'].dt.tz_convert('America/New_York')

    df_filtered = df[df['importance'].isin([1])]
    df_filtered = df_filtered[['title', 'country', 'importance', 'date']]
    df_filtered['importance'] = df_filtered['importance'].replace({0: 'Medio', 1: 'Alto'})

    bot = Bot(token="5963451255:AAGPxyC1fAWr_m-rugp5332ljeGN8HPL_hU")
    
    # Calculamos las fechas de inicio y fin de la semana
    inicio_semana = today.strftime('%d/%m/%Y')
    fin_semana = (today + pd.offsets.Day(7)).strftime('%d/%m/%Y')

    message = f"Feliz inicio de semana, procedemos a actualizar las noticias para la semana {inicio_semana} a {fin_semana}\n----------------\n"
    for index, row in df_filtered.iterrows():
        flag_emoji = country_to_emoji(row['country'])
        message += f"""
- Fecha: {row['date'].strftime('%d/%m/%Y')}
- Divisa: {flag_emoji} {row['country']}
- Noticia: {row['title']}
- Importancia: {row['importance']}
----------------
"""

    bot.send_message(chat_id="-1001938210460", text=message)

# while True:
#     now = datetime.now(pytz.timezone('America/New_York'))
#     if now.weekday() == 0 and now.hour == 6:  # Check if it's Monday at 6 a.m.
#         send_info()
#     time.sleep(60)  # Wait for 60 seconds before checking the time again
send_info()
