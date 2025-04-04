-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT
    o.registro_ans,
    o.nome_fantasia,
    c.descricao,
    SUM(c.vl_saldo_final) AS total_despesas
FROM
    despesas_operadoras c
    JOIN operadoras_ativas o ON c.reg_ans = o.registro_ans
WHERE
    c.descricao ILIKE '%SINISTROS%SAÚDE MEDICO HOSPITALAR%'
    AND c.data >= '2024-10-01'
    AND c.data < '2025-01-01'
GROUP BY
    o.registro_ans,
    o.nome_fantasia,
    c.descricao
ORDER BY
    total_despesas DESC
LIMIT 10;

