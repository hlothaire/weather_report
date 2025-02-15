# Weather Report Automation

Ce projet automatise la génération quotidienne d'un rapport météo pour une ville donnée en utilisant l'API OpenWeatherMap.

## Structure du projet
- `config.env` : variables d'environnement contenant la configuration (API key).
- `requirements.txt` : dépendances Python nécessaires.
- `main.py` : script principal orchestrant la récupération des données, la génération du rapport.
- `modules/`
  - `fetch_weather.py` : interroge l'API météo et retourne les données.
  - `report.py` : génère un rapport PDF à partir des données météo.
- `utils/`
  - `scheduler.py` : exemple de planification quotidienne du script (avec `schedule` ou `APScheduler`).

## Installation
1. Cloner le dépôt ou décompresser l'archive.
2. Créer un environnement virtuel et installer les dépendances :
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Remplir le fichier `config.env` avec vos informations :
   ```ini
   OPENWEATHER_API_KEY=VotreCléAPI
   CITY=Paris
   ```

## Usage
### Exécution manuelle
```bash
python main.py
```

### Planification
Vous pouvez utiliser le module `utils/scheduler.py` ou un `cron` pour exécuter `main.py` tous les jours à une heure fixe.
