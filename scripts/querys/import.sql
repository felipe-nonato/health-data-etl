--- IMPORTAÇÃO DE CONTEÚDO POR MEIO DO ARQUIVO

COPY operadoras_ativas 
FROM '/tmp/operadoras_ativas.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';

-- Ensure the table schema matches the CSV structure
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/1T2023.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';

-- Ensure the file exists and matches the schema
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/2t2023.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';
-- Ensure the table schema matches the CSV structure
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/3T2023.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';
-- Ensure the table schema matches the CSV structure
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/4T2023.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';
-- Ensure the table schema matches the CSV structure
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/1T2024.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';
-- Ensure the file exists and matches the schema
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/2T2024.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';
-- Ensure the table schema matches the CSV structure
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/3T2024.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';
-- Ensure the table schema matches the CSV structure
COPY despesas_operadoras (data, reg_ans, cd_conta_contabil,descricao, vl_saldo_inicial, vl_saldo_final)
FROM '/tmp/4T2024.csv' 
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8';