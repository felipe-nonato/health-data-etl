import time
import os
import zipfile

from constants import download_path
from constants import driver

def reject_cookies():
    """
    Função para rejeitar cookies em um site.
    """
    try:
        time.sleep(5)  # Aguarda o carregamento da página
        button = driver.find_element("xpath", '/html/body/div[5]/div/div/div/div/div[2]/button[2]')
        button.click()
        print("Cookies rejeitados com sucesso.")
    except Exception as e:
        print(f"Erro ao rejeitar cookies: {e}")


def download_by_xpath(xpath, file_name, time_download):
    """
    Função para baixar arquivos a partir de um elemento localizado por XPath.
    """
    try:
        time.sleep(5)  # Aguarda o carregamento da página
        
        button = driver.find_element("xpath", xpath)
        button.click()
        
        time.sleep(time_download)  # Aguarda o download iniciar
        # Verifica se o arquivo foi baixado
        file_path = os.path.join(download_path, file_name)
        if os.path.exists(file_path):
            print(f"Arquivo baixado com sucesso: {file_path}")
        else:
            print("Arquivo não encontrado na pasta de downloads.")
    
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        
        
def zip_files_in_directory():
    zip_file_path = os.path.join(download_path, "anexos.zip")
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(download_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file != "anexos.zip":  # Evita adicionar o próprio arquivo ZIP
                    zipf.write(file_path, os.path.relpath(file_path, download_path))
                print(f"Arquivos compactados com sucesso: {zip_file_path}")