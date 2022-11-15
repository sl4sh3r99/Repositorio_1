import datetime
import pytz

# en ts se ingresa el timestamp que poseemos
ts = 1668485375

#aqui se transforma el timestamp a fecha
dt = datetime.datetime.fromtimestamp((ts))
aware = dt.replace(tzinfo=pytz.UTC)
#aqui se cambia de UTC de Londres a UTC Mexico
mx = aware.astimezone(pytz.timezone('America/Mexico_City'))

#se imprimen ambas para poder apreciar la comparacion
print(f'Londres: {aware}')
print(f'Mexico: {mx}')