import requests
from config import API_KEY, CITY

def fetch_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    weather = fetch_weather()
    print(weather)
