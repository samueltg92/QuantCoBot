import myfxbook
import pandas as pd
import pytz
from datetime import datetime


fx = myfxbook.myfxbook('quantlabsmx@gmail.com', 'Holacomoestas0')

print('Login: ',fx.login())




cuentas = fx.get_my_accounts()
lista_cuentas = cuentas['accounts']

# Convertir la lista de diccionarios en un DataFrame
df = pd.DataFrame(lista_cuentas)


print(df)


# print('Logout: ',fx.logout())