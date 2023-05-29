import quantstats as qs
from binance.client import Client
import ccxt
import pandas as pd
from datetime import datetime
import openpyxl
from dotenv import load_dotenv
import os

register1 = pd.read_excel('Registro_de_operaciones_Binance.xlsx',index_col='datetime', sheet_name = 'SamuelTM')
register2 = pd.read_excel('Registro_de_operaciones_Binance.xlsx',index_col='datetime', sheet_name = 'ThiagoTM')
load_dotenv()

publicsam = os.getenv('PUBLIC1')
privatesam = os.getenv('SECRET1')

publicthiago = os.getenv('PUBLIC2')
privatethiago = os.getenv('SECRET2')

def register_balance(API_KEY, PRIVATE_KEY):
      
    binance = ccxt.binanceusdm({
        'apiKey': API_KEY,
        'secret': PRIVATE_KEY,
        'verbose': False,
    })
    balances = (binance.fetch_balance())

    for x,y in balances.items():
        if x == 'total':
            total = x,y
            for pair,balance in total[1].items():
                if pair == 'USDT':
                    df = pd.DataFrame({
                        'Paridad': pair,
                        'Balance': balance},index=[1])
                    df['datetime'] = datetime.today().strftime('%Y-%m-%d')
                    df = df.set_index('datetime')
                    print(df)
    return df

if __name__ == '__main__':

    df1 = register_balance(publicsam, 
                     privatesam,
                     )
    
    df2 = register_balance(publicthiago, 
                     privatethiago,
                     )


    df4 = pd.concat([register1, df1])
    df5 = pd.concat([register2, df2])
  
writer = pd.ExcelWriter('Registro_de_operaciones_Binance.xlsx', mode = 'a', if_sheet_exists = 'overlay', engine = 'openpyxl')
df4.to_excel(writer, sheet_name = 'SamuelTM',)
df5.to_excel(writer, sheet_name = 'ThiagoTM')

writer.save()