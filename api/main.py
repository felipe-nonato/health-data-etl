from flask import Flask, request, jsonify, make_response
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)

# Configurando o CORS para permitir todas as origens
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Construindo o caminho absoluto para o arquivo CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPERADORAS_CSV_PATH = os.path.join(BASE_DIR, '../scripts/data/operadoras_ativas.csv')

# Carregando o DataFrame de operadoras ativas
operadoras_df = pd.read_csv(OPERADORAS_CSV_PATH, sep=';', encoding='utf-8', low_memory=False)

# Convertendo os nomes das colunas para letras minúsculas
operadoras_df.columns = operadoras_df.columns.str.lower()

@app.after_request
def add_cors_headers(response):
    """
    Adiciona os cabeçalhos CORS a todas as respostas.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

@app.route('/')
def index():
    """
    Rota principal que retorna um HTML simples com as rotas disponíveis.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Health Data ETL</title>
    </head>
    <body>
        <h1>Bem-vindo à API Health Data ETL</h1>
        <p>Rotas disponíveis:</p>
        <ul>
            <li><strong>GET /operadoras</strong>: Busca operadoras com base em parâmetros específicos ou uma query geral.</li>
            <ul>
                <li>Parâmetros aceitos:</li>
                <li><code>query</code>: Busca geral em todos os campos.</li>
                <li><code>registro_ans</code>, <code>cnpj</code>, <code>razao_social</code>, <code>nome_fantasia</code>, <code>modalidade</code>, <code>logradouro</code>, <code>numero</code>, <code>complemento</code>, <code>bairro</code>, <code>cidade</code>, <code>uf</code>, <code>cep</code>, <code>ddd</code>, <code>telefone</code>, <code>fax</code>, <code>endereco_eletronico</code>, <code>representante</code>, <code>cargo_representante</code>, <code>regiao_de_comercializacao</code>, <code>data_registro_ans</code></li>
            </ul>
        </ul>
        <p>Exemplo de uso:</p>
        <ul>
            <li><code>/operadoras?query=São Paulo</code></li>
            <li><code>/operadoras?cidade=São Paulo&uf=SP</code></li>
        </ul>
    </body>
    </html>
    """
    response = make_response(html_content, 200)
    response.headers["Content-Type"] = "text/html"
    return response

@app.route('/operadoras', methods=['GET'])
def search_operadoras():
    """
    Endpoint para buscar operadoras com base em qualquer parâmetro fornecido ou por uma query geral.
    Parâmetros aceitos:
    - query: busca em todos os campos de uma vez.
    - Outros parâmetros específicos: registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
      complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico,
      representante, cargo_representante, regiao_de_comercializacao, data_registro_ans
    """
    # Obtendo os parâmetros da requisição
    query_params = {key.lower(): value for key, value in request.args.to_dict().items()}
    general_query = query_params.pop('query', None)

    # Se nenhum parâmetro for fornecido, retorna todas as operadoras
    filtered_operadoras = operadoras_df

    if general_query:
        # Filtrando por uma busca geral em todas as colunas
        mask = filtered_operadoras.apply(
            lambda row: row.astype(str).str.contains(general_query, case=False, na=False).any(), axis=1
        )
        filtered_operadoras = filtered_operadoras[mask]
    else:
        # Filtrando o DataFrame com base nos parâmetros fornecidos
        for key, value in query_params.items():
            if key in operadoras_df.columns:
                filtered_operadoras = filtered_operadoras[
                    filtered_operadoras[key].astype(str).str.contains(value, case=False, na=False)
                ]
            else:
                return jsonify({"error": f"Parametro invalido: {key}"}), 400

    # Convertendo o DataFrame filtrado para JSON
    results = filtered_operadoras.to_json(orient='records', force_ascii=False)

    # Retornando o JSON como string
    response = make_response(results, 200)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
