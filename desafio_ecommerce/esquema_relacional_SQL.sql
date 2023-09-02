-- criação do banco de dados para o cenário de E-commerce 

create database if not exists ecommerce;
use ecommerce;

-- clients
-- criar tabela Clientes
create table clientes(
	idCliente int auto_increment primary key,
    cli_Nome varchar(10),
    cli_NomeMeio varchar(10),
    cli_Sobrenome varchar(10),
    cli_CPF char(11) not null,
    cli_End_Logradouro varchar(255),
    cli_End_Numero int,
    cli_End_Complemento varchar(20),
    cli_End_Bairro varchar(30),
    cli_End_CEP char(8),
    cli_End_Cidade varchar(30),
    cli_End_Estado enum('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA',
						'PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO') not null,
    cli_Nascimento date not null,
    constraint unique_cpf_cliente unique (cli_CPF)
);

-- products
-- criar tabela Produtos
create table produtos(
	idProduto int auto_increment primary key,
	prod_Nome varchar(255) not null,
    prod_ClassificacaoKids bool default false,
    prod_Categoria enum('Eletrônico','Vestimenta','Brinquedos','Alimentos','Móveis') not null,
    prod_Descricao text,
    prod_Preco decimal(10,2) not null,
    prod_Avaliacao float default 0,
    prod_Tamanho varchar(10)
);


-- para ser continuado no desafio: termine de implementar a tabela e crie a conexão com as tabelas necessárias
-- além disso, reflita essa modificação no diagrama de esquema relacional
-- criar constraints relacionadas ao pagamento


-- payments
-- criar tabela de Pagamentos
create table pagamentos(
	idClientePagamento int,
    idPagamento int,
    pag_Tipo enum('Boleto','Cartão Crédito'),
    pag_LimiteLiberado float,
    pag_NumeroCartao int(16),
    primary key(idClientePagamento, idPagamento),
    constraint fk_pagamentos_cliente foreign key(idClientePagamento) references clientes(idCliente)
);


-- orders
-- criar tabela Pedidos
create table pedidos(
	idPedido int auto_increment primary key,
    idPedidoCliente int,
    ped_Status enum('Cancelado','Confirmado','Em processamento','Enviado','Entregue') default 'Em processamento',
    ped_Descricao varchar(255),
    ped_ValorEnvio decimal(10,2) default 10,
    ped_Pagamento boolean default false, 
	constraint fk_pedidos_cliente foreign key (idPedidoCliente) references clientes(idCliente)
	on update cascade
);


-- storage
-- criar tabela de Estoques
create table estoqueProdutos(
	idProdutoEstoque int auto_increment primary key,
    est_Localidade varchar(255),
    est_Quantidade int default 0
);


-- suplier
-- criar tabela de Fornecedores
create table fornecedores(
	idFornecedor int auto_increment primary key,
    for_NomeSocial varchar(255) not null,
    for_CNPJ char(15) not null,
    for_ContatoTelefone varchar(11) not null,
    for_Email varchar(100) not null,
    constraint unique_fornecedor unique (for_CNPJ)
);


-- seller
-- criar tabela Vendedores
create table vendedores(
	idVendedor int auto_increment primary key,
    ven_nomeSocial varchar(255) not null,
    ven_nomeAbstrato varchar(255),
    ven_CNPJ char(15),
    ven_CPF char(11),
    ven_localidade varchar(255),
    ven_contatoTelefone char(11) not null,
    ven_Email varchar(100) not null,
    constraint unique_cnpj_vendedores unique (ven_CNPJ),
    constraint unique_cpf_vendedores unique (ven_CPF)
);


-- tabelas de relacionamentos M:N


-- productSeller
-- criar tabela de Vendedores de Produtos
create table produtosVendedores(
	idpVendedor int,
    idpProduto int,
	prodVend_Quantidade int default 1,
    primary key (idpVendedor, idpProduto),
    constraint fk_produtos_vendedor foreign key (idpVendedor) references vendedores(idVendedor),
    constraint fk_produtos_produto foreign key (idpProduto) references produtos(idProduto)
);


-- productOrder
-- criar tabela de Ordem de Pedidos
create table ordemPedidos(
	idOrdemProduto int,
    idOrdemPedido int,
    ord_Quantidade int default 1,
    ord_StatusPedido enum('Disponível', 'Sem estoque') default 'Disponível',
    primary key (idOrdemProduto, idOrdemPedido),
    constraint fk_ordemPedidos_produto foreign key (idOrdemProduto) references produtos(idProduto),
    constraint fk_ordemPedidos_pedido foreign key (idOrdemPedido) references pedidos(idPedido)
);


-- storageLocation
-- criar tabela de Localização dos Estoques
create table estoquesLocalidades(
	idProdutoEstoque int,
    idEstoque int,
    est_Localidade varchar(255) not null,
    primary key (idProdutoEstoque, idEstoque),
    constraint fk_estoquesLocalidades_produtos foreign key (idProdutoEstoque) references produtos(idProduto),
    constraint fk_estoquesLocalidades_estoque foreign key (idEstoque) references estoqueProdutos(idProdutoEstoque)
);


-- productSupplier
-- criar a tabela de Produtos que são Fornecidos pelos Fornecedores
create table produtosFornecedores(
	idProdFor_Fornecedor int,
    idProdFor_Produto int,
    prodFor_Quantidade int not null,
    primary key (idProdFor_Fornecedor, idProdFor_Produto),
    constraint fk_produtosFornecedores_fornecedor foreign key (idProdFor_Fornecedor) references fornecedores(idFornecedor),
    constraint fk_produtosFornecedores_produto foreign key (idProdFor_Produto) references produtos(idProduto)
);

