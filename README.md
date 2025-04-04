# Health Data ETL

## 📋 Sobre

Sistema de processamento de dados que inclui web scraping, transformação de dados, API REST e interface web.

## 🚀 Tecnologias

### Backend

- Python 3.8+
- Flask
- PostgreSQL
- Bibliotecas Python:
  - asttokens: 3.0.0
  - blinker: 1.9.0
  - click: 8.1.8
  - comm: 0.2.2
  - debugpy: 1.8.13
  - decorator: 5.2.1
  - distro: 1.9.0
  - exceptiongroup: 1.2.2
  - executing: 2.2.0
  - Flask: 3.1.0
  - ipykernel: 6.29.5
  - ipython: 8.34.0
  - itsdangerous: 2.2.0
  - jedi: 0.19.2
  - Jinja2: 3.1.6
  - jupyter_client: 8.6.3
  - jupyter_core: 5.7.2
  - MarkupSafe: 3.0.2
  - matplotlib-inline: 0.1.7
  - nest-asyncio: 1.6.0
  - numpy: 2.2.4
  - packaging: 24.2
  - pandas: 2.2.3
  - parso: 0.8.4
  - pexpect: 4.9.0
  - platformdirs: 4.3.7
  - prompt_toolkit: 3.0.50
  - psutil: 7.0.0
  - ptyprocess: 0.7.0
  - pure_eval: 0.2.3
  - Pygments: 2.19.1
  - python-dateutil: 2.9.0.post0
  - pytz: 2025.2
  - pyzmq: 26.4.0
  - six: 1.17.0
  - stack-data: 0.6.3
  - tabula-py: 2.10.0
  - tornado: 6.4.2
  - traitlets: 5.14.3
  - typing_extensions: 4.13.1
  - tzdata: 2025.2
  - wcwidth: 0.2.13
  - Werkzeug: 3.1.3

### Frontend

- Vue.js
- Axios

## 🛠️ Instalação

1. Clone o repositório

```bash
git clone https://github.com/felipe-nonato/health-data-etl.git
cd health-data-etl
```

2. Configure o ambiente virtual

```bash
python3 -m venv venv
source dir_name/bin/activate  # Linux/Mac
# ou
.\dir_name\Scripts\activate  # Windows
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente

```bash
cp .env.sample .env
# Edite o arquivo .env com suas configurações
```

5. Inicie o banco de dados

```bash
docker-compose up -d postgres
docker exec -i meu_postgres psql -U meu_usuario -d meu_banco < ~/Codes/health-data-etl/scripts/querys/init.sql
docker cp /home/lipe/Codes/health-data-etl/scripts/data/. meu_postgres:/tmp
```

## 📊 Estrutura do Projeto

```
├── api/                 # Código da API
├── scraping/            # Scraping de dados
├── data-transformation/  # Transformação dos dados
├── scripts/            # Scripts de download e consulta de dados de operadoras ANS
├── frontend/          # Interface Vue.js
└── tests/            # Testes unitários e integração
```

## 🔍 Uso

### Executando o ETL

```bash
python3 etl.py # Esse Script já inicia a API
```

### Iniciando a API

```bash
python3 api/main.py
```

### Rodando o Frontend

```bash
cd frontend
npm install
npm run dev
```

## 🧪 Testes

No dirétorio `/tests` é possível encontrar uma collection do Postman para teste de API e uma pasta http para teste com extensões no Vscode.

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
