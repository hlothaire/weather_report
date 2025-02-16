import os
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

from modules.fetch_weather import get_5day_forecast
from modules.report import generate_pdf_with_graph

def main():
    load_dotenv(dotenv_path='config.env')
    api_key = os.getenv('OPENWEATHER_API_KEY')
    city    = os.getenv('CITY')

    df_5day = get_5day_forecast(api_key, city)

    print(df_5day)

    plt.figure(figsize=(8, 5))
    plt.plot(df_5day['date'], df_5day['temp'], marker='o', linestyle='-')
    plt.title(f"Prévision 5 jours – Température à {city}")
    plt.xlabel("Date")
    plt.ylabel("Température (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    today_str = datetime.now().strftime('%Y-%m-%d')
    graph_filename = f"graphique_meteo_5day_{city}_{today_str}.png"
    plt.savefig(graph_filename)
    plt.close()
    print(f"Graphique 5 jours sauvegardé : {graph_filename}")

    pdf_filename = f"rapport_meteo_{city}_{today_str}.pdf"
    generate_pdf_with_graph(city, graph_filename, pdf_filename)
    print(f"PDF généré avec graphique : {pdf_filename}")

if __name__ == '__main__':
    main()

