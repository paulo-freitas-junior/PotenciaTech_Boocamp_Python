-- Arquivo de queries de consultas
-- ###############################

-- ARQUIVO SERÁ ATUALIZADO


-- Qual a quantidade total de clientes cadastrados?
select	count(*) from clientes;

-- Quantos clientes cadastrados são do estado de SP?
select	count(*) from clientes where cli_End_Estado = 'SP';

-- Quais foram todos os pedidos realizados por todos os clientes cadastrados?
select	* 
from	clientes c, pedidos p
where	c.idCliente = p.idPedidoCliente;

-- Quantos pedidos no total foram realizados para cada cliente?
select	concat(cli_Nome,' ',cli_NomeMeio,' ',cli_Sobrenome) as Nome_Cliente, count(*) as Total_Pedidos
from	clientes c, pedidos p
where	c.idCliente = p.idPedidoCliente
group by	idCliente
order by	Total_Pedidos desc;

-- Quantos pedidos foram realizados pelos clientes? ( Usando INNER JOIN )?
select	c.idCliente, c.cli_Nome, count(*) as Total_Pedidos
from	clientes c inner join pedidos p 
		ON c.idCliente = p.idPedidoCliente
group by	c.idCliente;

-- Qual a quantidade de produtos em estoque e a localização do estoque?
select	p.prod_Nome as 'Produto', ep.est_Quantidade as 'Quantidade', ep.est_Localidade as 'Local Estoque'
from	produtos p , estoqueprodutos ep
where	p.idProduto = ep.idProdutoEstoque
group by	idProduto;

-- Quais produtos são fornecidos por determinados fornecedores?

select prod_Nome as 'Nome do Produto', for_NomeSocial as 'Nome do Fornecedor'
from produtos, fornecedores, produtosfornecedores
where idProduto = idProdFor_Produto and idFornecedor = idProdFor_Fornecedor;

-- Quais produtos estão em falta no estoque ?

select	idProduto, prod_Nome, prod_Preco, est_Quantidade
from	produtos, estoqueprodutos
where 	idProduto = idProdutoEstoque;


-- Quais os pedidos que foram entregues para determinados clientes e qual a localidade de origem do envio e a localidade de entrega desses pedidos?
