from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(weather_data, output_filename):
    c = canvas.Canvas(output_filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, f"Rapport Météo pour {weather_data['city']}")

    report_date = datetime.fromtimestamp(weather_data['date']).strftime('%Y-%m-%d %H:%M:%S')
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Date : {report_date}")

    c.drawString(50, height - 130, f"Description : {weather_data['description']}")
    c.drawString(50, height - 150, f"Température actuelle : {weather_data['temperature']} °C")
    c.drawString(50, height - 170, f"Température minimale : {weather_data['temp_min']} °C")
    c.drawString(50, height - 190, f"Température maximale : {weather_data['temp_max']} °C")
    c.drawString(50, height - 210, f"Humidité : {weather_data['humidity']} %")
    c.drawString(50, height - 230, f"Vitesse du vent : {weather_data['wind_speed']} m/s")

    c.showPage()
    c.save()
