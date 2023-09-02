-- Inserindo dados nas tabelas do Banco de Dados farmácia
use farmacia;

-- Tipos produtos
INSERT INTO tipos_produto (tipo) VALUES ('Remédios');
INSERT INTO tipos_produto (tipo) VALUES ('Cosméticos');
INSERT INTO tipos_produto (tipo) VALUES ('Diversos');
-- SELECT * FROM tipos_produto;

-- Fabricantes
INSERT INTO fabricantes (fabricante) VALUES ('Roche');
INSERT INTO fabricantes (fabricante) VALUES ('Vitalis');
INSERT INTO fabricantes (fabricante) VALUES ('Palmolive');
-- select * from fabricantes;

-- Medicos
INSERT INTO medicos (nome, crm) VALUES ('Reinaldo Segre', '456987SP');
INSERT INTO medicos (nome, crm) VALUES ('Décio Pinto', '169169MG');
INSERT INTO medicos (nome, crm) VALUES ('Lair Ribeiro', '171171MA');
-- select * from medicos;

-- Clientes
INSERT INTO clientes (nome, endereco, telefone, cep, localidade, cpf) 
	VALUES ('Adriane Galisteu','Rua Bento Freitas, 66', '(11)9978-5852', '06969-069', 'São Paulo', '123.456.789-10');
INSERT INTO clientes (nome, endereco, telefone, cep, localidade, cpf) 
	VALUES ('Fausto Silva','Rua da Globo, 05', '(21)9876-5432', '05678-901', 'Rio de Janeiro', '234.567.890-12');
INSERT INTO clientes (nome, endereco, telefone, cep, localidade, cpf) 
	VALUES ('Silvio Santos','Rua SBT, 04', '(11)9875-3944', '05678-123', 'Anhanguera', '456.789.123-45');
-- select * from clientes;

-- Produtos
INSERT INTO produtos (produto, designacao, composicao, preco, id_tipo_produto, id_fabricante) 
	VALUES ('Dipirona', 'Dores em geral', 'Metilpropileno', '12.44', 1, 1);
INSERT INTO produtos (produto, designacao, composicao, preco, id_tipo_produto, id_fabricante) 
	VALUES ('Sabonete', 'Limpeza', 'Sei lah', '3.56', 2, 2);
INSERT INTO produtos (produto, designacao, composicao, preco, id_tipo_produto, id_fabricante) 
	VALUES ('Protetor Solar', 'Protetor Solar', 'Soro de abacate', '98.12', 2, 1);
-- select * from produtos;

-- Compras
 INSERT INTO compras (id_cliente, data) VALUES (1, '2023-08-15');
 INSERT INTO compras (id_cliente, data) VALUES (2, '2022-06-22');
 INSERT INTO compras (id_cliente, data) VALUES (1, '2023-09-01');
 -- select * from compras;
 
-- Produtos Compra
INSERT INTO produtos_compra (id_compra, id_produto, quantidade) VALUES (1, 1, 2);
INSERT INTO produtos_compra (id_compra, id_produto, quantidade) VALUES (1, 2, 3);
INSERT INTO produtos_compra (id_compra, id_produto, quantidade) VALUES (2, 3, 1);
-- select * from produtos_compra;

-- Receitas Medicas
INSERT INTO receitas_medica (id_produto_compra, id_medico, receita) VALUES (1, 1, 'receita0001.pdf');
INSERT INTO receitas_medica (id_produto_compra, id_medico, receita) VALUES (3, 2, 'receita0002.pdf');
-- select * from receitas_medica;