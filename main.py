import os
from dotenv import load_dotenv
from modules.fetch_weather import get_weather_data
from modules.report import generate_pdf_report
from datetime import datetime

def main():
    load_dotenv(dotenv_path='config.env')
    api_key = os.getenv('OPENWEATHER_API_KEY')
    city = os.getenv('CITY')
    recipient = os.getenv('RECIPIENT_EMAIL')

    weather = get_weather_data(api_key, city)

    date_str = datetime.now().strftime('%Y-%m-%d')
    pdf_filename = f"rapport_meteo_{city}_{date_str}.pdf"

    generate_pdf_report(weather, pdf_filename)

    print(f"Rapport généré : {pdf_filename}")

if __name__ == '__main__':
    main()
