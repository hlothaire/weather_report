import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fetch_weather import fetch_weather

def create_report(output_dir=os.path.join(os.path.dirname(__file__), '..', 'reports')):
    data = fetch_weather()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = os.path.join(output_dir, f"weather_report_{date_str}.pdf")
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Météo pour {data.get('name', 'N/A')} le {date_str}")
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    y = 720
    lines = [
        f"Description : {weather_desc}",
        f"Température actuelle : {temp} °C",
        f"Température min : {temp_min} °C",
        f"Température max : {temp_max} °C",
        f"Humidité : {humidity} %",
        f"Vitesse du vent : {wind_speed} m/s",
    ]

    for line in lines:
        c.drawString(100, y, line)
        y -= 20

    c.save()
    return filename

if __name__ == "__main__":
    report_path = create_report()
    print(f"Rapport généré : {report_path}")
