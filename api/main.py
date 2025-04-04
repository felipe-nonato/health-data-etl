from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Construindo o caminho absoluto para o arquivo CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPERADORAS_CSV_PATH = os.path.join(BASE_DIR, '../scripts/data/operadoras_ativas.csv')

# Carregando o DataFrame de operadoras ativas
operadoras_df = pd.read_csv(OPERADORAS_CSV_PATH, sep=';', encoding='utf-8', low_memory=False)

# Convertendo os nomes das colunas para letras minúsculas
operadoras_df.columns = operadoras_df.columns.str.lower()

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
    return results, 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
