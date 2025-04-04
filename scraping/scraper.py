import sys

sys.path.append("/home/lipe/Codes/teste/scraping")

from constants import driver
from functions import reject_cookies, download_by_xpath, zip_files_in_directory

def run_scraper():
    try:
        # Acessa site de Agencia Nacional de Saúde Suplementar
        url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"  # Substitua pela URL do site que deseja acessar
        driver.get(url)
        
        reject_cookies()
        
        # Baixa o anexo I
        download_by_xpath(
            xpath='//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]',
            file_name="Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", 
            time_download=30
        )
        
        #Baixa o anexo II
        download_by_xpath(
            xpath='//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a', 
            file_name="Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf", 
            time_download=10
        )

        # Compacta os arquivos na pasta de downloads
        zip_files_in_directory()
        
    finally:
        # Fecha o navegador
        driver.quit()