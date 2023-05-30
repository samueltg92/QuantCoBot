import myfxbook
import pandas as pd
import pytz
from datetime import datetime

today = pd.Timestamp.today().normalize()

fx = myfxbook.myfxbook('quantlabsmx@gmail.com', 'Holacomoestas0')

print('Login: ',fx.login())




cuentas = fx.get_my_accounts()
ganancia_diaria = fx.get_daily_gain(id='9951687', start = 2023-5-28, end = 2023-5-29)
print(ganancia_diaria)



# print('Logout: ',fx.logout())