import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from telegram import Bot

# Leer el archivo CSV
df = pd.read_csv('ff_calendar_thisweek.csv')

# Seleccionar las divisas
currencies = ['USD', 'CHF', 'EUR', 'AUD', 'JPY', 'GBP', 'CAD', 'NZD']

# Filtrar por impacto y divisa
filtered_df = df[(df['Impact'].isin(['High', 'Medium'])) & (df['Country'].isin(currencies))]

# Dibujar el DataFrame como una tabla en una figura
fig, ax = plt.subplots(figsize=(10, 4)) # Ajusta el tamaño según tus necesidades
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=filtered_df.values, colLabels=filtered_df.columns, loc='center')

# Guardar la figura como una imagen
plt.savefig('filtered_news.png')

# # Configurar el bot de Telegram
# bot = Bot(token='5963451255:AAGPxyC1fAWr_m-rugp5332ljeGN8HPL_hU')

# # Enviar la imagen al grupo
# with open('filtered_news.png', 'rb') as f:
#     bot.send_photo(chat_id=1510902602, photo=f)
    

