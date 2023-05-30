import myfxbook
from dotenv import load_dotenv
import os
from myfxbook import Myfxbook


'''
Añadir datos de calendario economico con investpy
DeepAtlas:
id= 9951687
accountId= 74095769

Apollo:
id=10135756
accountId=61212991
'''

load_dotenv()


fx = Myfxbook(email = os.getenv('MYFXBOOK_USER'), password = os.getenv('MYFXBOOK_PASS'))
fx.login()

#Obtengo info de todas las cuentas de TheQuantCompany
accounts = fx.get_my_accounts()

# #Obtengo info de ganancia daily. Toma como parametros el id de la cuenta que quiero y el rango de fechas (start y end)
# daily_gain = fx.get_daily_gain(id=9951687)

# #Obtengo datos daily. Toma como parametros el id de la cuenta que quiero y el rango de fechas (start y end)
# daily_data = fx.get_data_daily(id=pass, start=pass, end=pass)

# #Obtengo historial de alguna cuenta en especifico (id)
# history = fx.get_history(id=9951687)

