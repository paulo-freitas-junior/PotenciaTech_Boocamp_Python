-- Consultas em Múltiplas Tabelas

-- Compras identificadas por nome dos clientes
SELECT com.id as 'ID Compra', cli.nome as 'Cliente', com.data as 'Data Compra'
	FROM compras as com, clientes as cli
    WHERE com.id_cliente = cli.id;
    
-- Valores totais das compras realizadas por clientes
SELECT com.id as "Compra",
	cli.nome as "Cliente",
    SUM(proc.quantidade * pro.preco) as "Total",
    com.data as "Data Compra"
FROM compras as com, clientes as cli, produtos_compra as proc, produtos as pro
WHERE com.id = proc.id_compra and com.id_cliente = cli.id and proc.id_produto = pro.id
GROUP BY com.id;

-- Valores das compras por produto
SELECT com.id as "Compra",
	cli.nome as "Cliente",
    pro.produto as "Produto",
    proc.quantidade * pro.preco as "Total",
    com.data as "Data Compra"
FROM compras as com, clientes as cli, produtos_compra as proc, produtos as pro
WHERE com.id = proc.id_compra and com.id_cliente = cli.id and proc.id_produto = pro.id;