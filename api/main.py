from flask import Flask, request, jsonify
import pandas as pd
import os
import json

app = Flask(__name__)

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
    Endpoint para buscar operadoras com base em qualquer parâmetro fornecido.
    Parâmetros aceitos:
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
    complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico,
    representante, cargo_representante, regiao_de_comercializacao, data_registro_ans
    """
    # Obtendo os parâmetros da requisição
    query_params = {key.lower(): value for key, value in request.args.to_dict().items()}

    if not query_params:
        return jsonify({"error": "Pelo menos um parâmetro de busca é necessário"}), 400

    # Filtrando o DataFrame com base nos parâmetros fornecidos
    filtered_operadoras = operadoras_df
    for key, value in query_params.items():
        if key in operadoras_df.columns:
            filtered_operadoras = filtered_operadoras[
                filtered_operadoras[key].astype(str).str.contains(value, case=False, na=False)
            ]
        else:
            return jsonify({"error": f"Parametro invalido: {key}"}), 400

    # Convertendo o DataFrame filtrado para uma lista de dicionários
    results = filtered_operadoras.to_dict(orient='records')

    # Retornando o JSON com encoding correto
    return app.response_class(
        response=json.dumps(results, ensure_ascii=False),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)