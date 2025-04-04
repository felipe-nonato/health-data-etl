# README - Health Data ETL Scripts

## Descrição

Este repositório contém scripts e consultas SQL desenvolvidos para atender aos requisitos de **Teste de Banco de Dados**. O objetivo é processar e analisar dados públicos disponibilizados pela ANS (Agência Nacional de Saúde Suplementar), utilizando bancos de dados compatíveis com **MySQL 8** ou **PostgreSQL >10.0**.

## Requisitos Atendidos

### Tarefas de Preparação

1. **Download de Arquivos**:
   - Baixar os arquivos dos últimos 2 anos do repositório público:  
     [Demonstrativos Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
   - Baixar os dados cadastrais das Operadoras Ativas no formato CSV:  
     [Operadoras Ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

### Tarefas de Código

2. **Estruturação de Tabelas**:

   - Criação de queries para estruturar tabelas necessárias para armazenar os dados do arquivo CSV.

3. **Importação de Dados**:

   - Desenvolvimento de queries para importar o conteúdo dos arquivos baixados, garantindo o uso do encoding correto.

4. **Análise de Dados**:
   - Elaboração de uma query analítica para responder às seguintes perguntas:
     - Quais as 10 operadoras com maiores despesas em **"EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR"** no último trimestre?
     - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

## Observações

- **Confidencialidade**: Este documento é confidencial e não deve ser divulgado ou copiado sem autorização expressa do remetente.
- **Compatibilidade**: Os scripts foram desenvolvidos para serem compatíveis com **MySQL 8** e **PostgreSQL >10.0**.

## Estrutura do Repositório

- `scripts/`: Contém os scripts em python para download dos documentos e SQL para criação de tabelas, importação de dados e análise.
- `data/`: Diretório sugerido para armazenar os arquivos baixados.

## Como Usar

1. Baixe os arquivos necessários executando `python3 get-datas.py`.
2. Execute os scripts SQL na ordem indicada:
   - Estruturação de tabelas.
   - Importação de dados.
   - Consultas analíticas.
3. Certifique-se de configurar o banco de dados corretamente antes de executar os scripts.

## Licença

Este projeto possui licença pública MIT.
