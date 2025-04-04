import os
import requests
import zipfile
import pandas as pd
from datetime import datetime

def criar_diretorio(diretorio):
    os.makedirs(diretorio, exist_ok=True)

def baixar_arquivo(url, caminho_destino):
    print(f"Baixando {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(caminho_destino, "wb") as f:
            f.write(response.content)
        print(f"Arquivo salvo: {caminho_destino}")
        return True
    else:
        print(f"Erro ao baixar {url} - Código {response.status_code}")
        return False

def extrair_csv_de_zip(caminho_zip, diretorio_destino):
    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith('.csv'):
                    zip_ref.extract(file, diretorio_destino)
                    print(f"Arquivo CSV extraído: {file}")
                    return os.path.join(diretorio_destino, file)
    except zipfile.BadZipFile:
        print(f"Erro: {caminho_zip} não é um arquivo zip válido")
    return None

def modificar_csv(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv, delimiter=';', encoding='UTF-8')
        if 'VL_SALDO_INICIAL' in df.columns and 'VL_SALDO_FINAL' in df.columns:
            df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.')
            df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.')
            df.to_csv(caminho_csv, index=False, sep=';', encoding='UTF-8')
            print(f"Arquivo CSV modificado e salvo: {caminho_csv}")
    except Exception as e:
        print(f"Erro ao modificar o CSV {caminho_csv}: {e}")

def processar_demonstracoes_contabeis(anos, trimestres, diretorio_destino, url_template):
    for ano in anos:
        for trimestre in trimestres:
            url = url_template.format(ano=ano, trimestre=trimestre)
            caminho_zip = os.path.join(diretorio_destino, f"demonstracoes_{trimestre}_{ano}.zip")
            
            if baixar_arquivo(url, caminho_zip):
                caminho_csv = extrair_csv_de_zip(caminho_zip, diretorio_destino)
                if caminho_csv:
                    modificar_csv(caminho_csv)
                os.remove(caminho_zip)
                print(f"Arquivo zip removido: {caminho_zip}")

def get_data():
    # Configurações
    diretorio_destino = "scripts/data"
    criar_diretorio(diretorio_destino)
    
    ano_atual = datetime.now().year
    anos = [ano_atual - 1, ano_atual - 2]
    trimestres = ["1T", "2T", "3T", "4T"]
    
    demonstracoes_url_template = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/{ano}/{trimestre}{ano}.zip"
    operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    dicionario_operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/dicionario_de_dados_das_operadoras_ativas.ods"
    
    # Processar Demonstrativos Contábeis
    processar_demonstracoes_contabeis(anos, trimestres, diretorio_destino, demonstracoes_url_template)
    
    # Baixar Dados das Operadoras Ativas
    caminho_operadoras = os.path.join(diretorio_destino, "operadoras_ativas.csv")
    baixar_arquivo(operadoras_url, caminho_operadoras)
    
    # Baixar Dicionário de Dados das Operadoras Ativas
    caminho_dicionario = os.path.join(diretorio_destino, "dicionario_operadoras_ativas.ods")
    baixar_arquivo(dicionario_operadoras_url, caminho_dicionario)
    
    print("✅ Download concluído!")

if __name__ == "__main__":
    get_data()
