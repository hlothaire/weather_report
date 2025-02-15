import schedule
import time
import os
import subprocess

def job():
    # Exécute le script principal
    os.system('python main.py')

if __name__ == '__main__':
    # Planifier la tâche tous les jours à 8h00
    schedule.every().day.at("08:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)
