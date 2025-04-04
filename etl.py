import sys
import os
import threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scraping.scraper import run_scraper
from scripts.get_datas import get_data

from api.main import app  # Importando a aplicação Flask
def run_etl():
    
    # Escalando em multi threads
    def scraper_thread():
        print("Rodando scraper...")
        run_scraper()
        
    def process_and_start_api():
        # Step 2: Process data
        print("Processando os dados...")
        get_data()

    scraper = threading.Thread(target=scraper_thread)
    processor = threading.Thread(target=process_and_start_api)

    scraper.start()
    processor.start()

    scraper.join()
    processor.join()
    
    # Step 3: Start API
    print("Iniciando API...")
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":
    run_etl()
