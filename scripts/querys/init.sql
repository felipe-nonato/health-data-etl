-- Active: 1715794477718@@192.168.25.83@5432
-- Estrutura do banco de dados baseada no arquivo operadoras_ativas.csv e relatorios de despesas trimestrais

CREATE TABLE operadoras_ativas (
    Registro_ANS INT PRIMARY KEY,
    CNPJ CHAR(14) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(50),
    Logradouro VARCHAR(255),
    Numero VARCHAR(50),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP CHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE
);

CREATE TABLE despesas_operadoras (
    ID SERIAL PRIMARY KEY,
    DATA DATE NOT NULL,
    REG_ANS INT NOT NULL,
    CD_CONTA_CONTABIL INT NOT NULL,
    DESCRICAO VARCHAR(150),
    VL_SALDO_INICIAL NUMERIC(18, 2) NOT NULL,
    VL_SALDO_FINAL NUMERIC(18, 2) NOT NULL
);
