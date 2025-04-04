# Health Data ETL

## 📋 Sobre
Sistema de processamento de dados que inclui web scraping, transformação de dados, API REST e interface web.

## 🚀 Tecnologias

### Backend
- Python 3.8+
- Flask
- PostgreSQL
- Bibliotecas Python:
  - selium
  - requests
  - BeautifulSoup
  - PyPDF2
  - pdfplumber
  - pandas

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
python -m venv dir_name (substitua "dir_name" pelo diretorio que deseja trabalhar)
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
cp .env.example .env
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
├── tests/            # Testes unitários e integração
└── docs/            # Documentação adicional
```

## 🔍 Uso

### Executando o ETL
```bash
python etl.py
```

### Iniciando a API
```bash
uvicorn api.main:app --reload
```

### Rodando o Frontend
```bash
cd frontend
npm install
npm run serve
```

## 📝 Documentação da API

A documentação da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧪 Testes

```bash
pytest tests/
```

## 📈 Monitoramento

O sistema inclui logs e métricas básicas que podem ser visualizados através do endpoint `/metrics`.

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
