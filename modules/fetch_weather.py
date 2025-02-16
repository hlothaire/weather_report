import requests
import pandas as pd
from datetime import datetime

def get_current_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    cod = data.get('cod')
    if (isinstance(cod, int) and cod != 200) or (isinstance(cod, str) and cod != "200"):
        message = data.get('message', 'Erreur inconnue')
        raise RuntimeError(f"OpenWeatherMap (current) renvoie une erreur : {message} (cod={cod})")

    weather_info = {
        'city': data.get('name'),
        'date': datetime.fromtimestamp(data.get('dt')),
        'temperature': data['main'].get('temp'),
        'temp_min': data['main'].get('temp_min'),
        'temp_max': data['main'].get('temp_max'),
        'humidity': data['main'].get('humidity'),
        'wind_speed': data['wind'].get('speed'),
        'description': data['weather'][0].get('description').capitalize(),
        'lat': data['coord'].get('lat'),
        'lon': data['coord'].get('lon')
    }
    return weather_info


def get_5day_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url)
    data = resp.json()

    cod = data.get('cod')
    if cod != "200":
        message = data.get('message', 'Erreur inconnue')
        raise RuntimeError(f"OpenWeatherMap (forecast) renvoie une erreur : {message} (cod={cod})")

    entries = data['list']

    rows = {}
    for e in entries:
        ts = e.get('dt')
        dt_obj = datetime.fromtimestamp(ts)
        date_str = dt_obj.strftime('%Y-%m-%d')

        if dt_obj.hour == 12:
            rows[date_str] = e['main'].get('temp')
        else:
            if date_str not in rows:
                rows[date_str] = e['main'].get('temp')

    dates_triees = sorted(rows.keys())
    dates_sel = dates_triees[:5]

    data_rows = []
    for d in dates_sel:
        data_rows.append({'date': datetime.strptime(d, '%Y-%m-%d'), 'temp': rows[d]})

    df = pd.DataFrame(data_rows)
    return df
