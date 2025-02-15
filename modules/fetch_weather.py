import requests

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather_info = {
        'city': data.get('name'),
        'date': data.get('dt'),
        'temperature': data['main'].get('temp'),
        'temp_min': data['main'].get('temp_min'),
        'temp_max': data['main'].get('temp_max'),
        'humidity': data['main'].get('humidity'),
        'wind_speed': data['wind'].get('speed'),
        'description': data['weather'][0].get('description').capitalize()
    }
    return weather_info
