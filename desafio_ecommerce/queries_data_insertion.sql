-- inserindo dados na tabela Clientes
insert into clientes (cli_Nome, cli_NomeMeio, cli_Sobrenome, cli_Cpf, cli_End_Logradouro, cli_End_Numero, cli_End_Complemento, cli_End_Bairro, cli_End_CEP, cli_End_Cidade, cli_End_Estado, cli_Nascimento) 
			values  ('Lucas', 'Vieira', 'Araujo', 12345678911, 'Avenida Paulista', 1854, 'Apartamento 12','Paulista','12345678', 'São Paulo', 'SP', '1988-09-09'),
					('Adriana', 'Feline', 'Souza', 23456789012, 'Rua Pamplona', 785, 'Bloco B, Apto 34', 'Campos Elisios', '12345789', 'São Paulo', 'SP', '1987-12-12'),
					('André', 'Vieira', 'Ramos', 21745839845, 'Rua Belo Horizonte', 15, 'Casa', 'Mineirão', '25874589', 'Belo Horizonte', 'MG', '1979-08-14');


-- inserindo dados na tabela Produtos
insert into produtos (prod_Nome, prod_ClassificacaoKids, prod_Categoria, prod_Descricao, prod_Preco, prod_Avaliacao, prod_Tamanho)
			  values ('Celular', default, 'Eletrônico', 'Aparelho muito bom com 128gb', 1999.99, 6.0, '12x8x2'),
					 ('HotWheels', true, 'Brinquedos', 'Autorama HotWheels', 299.99, 7.5, null),
                     ('Blusa', default, 'Vestimenta', 'Moletom do DeadFish', 99.99, 8.5, null),
                     ('Whey', default, 'Alimentos', '25g de proteína por dose', 89.99, 9.5, null),
                     ('Sofá', default, 'Móveis', 'Reclinável e retrátil', 1989.99, 10.00, '4x5x3'); 
                     
-- inserindo valores na tabela Pedidos
insert into pedidos (idPedidoCliente, ped_Status, ped_Descricao, ped_ValorEnvio, ped_Pagamento)
			 values (1, 'Enviado', 'Foi entregue na trasnportadora', 20, default),
					(1, 'Em processamento', 'Aguardando o pagamento', 30, default),
                    (1, 'Enviado', 'Objeto em trânsito para o cliente', 40, default),
                    (1, 'Entregue', 'Objeto entregue para o cliente', 50, default),
                    (2, 'Enviado', 'Foi entregue na trasnportadora', 20, default),
                    (2, 'Em processamento', 'Aguardando o pagamento', 30, default),
                    (2, 'Enviado', 'Objeto em trânsito para o cliente', 40, default),
                    (2, 'Entregue', 'Objeto entregue para o cliente', 50, default),
                    (3, 'Enviado', 'Foi entregue na trasnportadora', 20, default),
                    (3, 'Enviado', 'Objeto em trânsito para o cliente', 40, default),
                    (3, 'Cancelado', 'Compra cancelada pelo cliente', 50, default),
                    (1, 'Em processamento', 'Aguardando o pagamento', 30, default),
                    (2, 'Enviado', 'Foi entregue na trasnportadora', 20, default),
                    (3, 'Enviado', 'Objeto em trânsito para o cliente', 40, default),
                    (2, 'Confirmado', 'Objeto entregue para o cliente', 50, default);


-- inseridos na tabela estoquesProdutos
insert into estoqueProdutos (est_Quantidade, est_Localidade)
			values (1, 'Canoas'), 
				   (2, 'Campinas'), 
                   (3, 'Deodoro'), 
                   (4, 'Ouro Preto'), 
                   (5, 'Trindade');


-- inserindo valores na tabela fornecedores
insert into fornecedores (for_NomeSocial, for_CNPJ, for_ContatoTelefone, for_Email)
			values ('Tektoy Brinquedos', '06085081000160', '11911111111', 'contato@tektoy.com.br'),
				   ('Suplementos Forte', '06075088000159', '11922222222', 'contato@suplementos.com.br'),
                   ('Móveis Sob Medida', '08075891000175', '11933333333', 'contato@moveissobmeida.com.br'),
                   ('Eletrônicos TecnoCell', '06075089000160', '11944444444', 'contato@tecnocell.com.br'),
                   ('Moda Moderna', '06085089000160 ','11955555555', 'contato@moderna.com.br');


-- inserindo valores na tabela vendedores
insert into vendedores (ven_nomeSocial, ven_nomeAbstrato, ven_CNPJ, ven_CPF, ven_localidade, ven_contatoTelefone, ven_Email)
			values ('Antonio Lima LTDA', 'Móveis Rústicos Lima', '00225801000160', '21057836847', 'São Paulo', '11987935468', 'contato@moveisrusticos.com.br'),
				   ('Salvador Leandro ME', 'Leandro Eletrônicos', '00227451000160', '21057896847', 'Minas Gerais', '13987653285', 'contato@leandrotec.com.br'),
                   ('Ahmad Salim Maluf LTDA', 'Explosão Fogos Artifícios', '00225812300160', '58757836847', 'Rio de Janeiro', '21991585478', 'contato@explosao.com.br'),
                   ('Teodoro Maria ME', 'Máquinas Costura Elgin', '00369801000160', '85057836847', 'Santa Catarina', '4398435874', 'contato@elgin.com.br');                  

select * from vendedores;

-- inserindo valores na tabela produtosVendedores
insert into produtosVendedores (idpVendedor, idpProduto, prodVend_Quantidade)
			values (1, 2, 10),				
                   (2, 4, 7),
                   (3, 5, 2),
                   (4, 1, 6),
                   (1, 3, 10);
               
               
-- inserindo valores na tabela produtosPedidos
insert into ordemPedidos (idOrdemProduto, idOrdemPedido, ord_Quantidade, ord_StatusPedido)
			values (1, 16, 1, default),
				   (1, 20, 1, default),
                   (2, 24, 1, 'Sem estoque'),
                   (3, 25, 1, default),
                   (4, 27, 1, 'Sem estoque'),
                   (5, 29, 1, default);


-- inserindo valores na tabela estoquesLocalidades
insert into estoquesLocalidades (idProdutoEstoque, idEstoque, est_Localidade)
			values (1, 2, 'São Paulo'),				
                   (2, 4, 'Minas Gerais'),
                   (3, 5, 'Bahia'),
                   (4, 1, 'Rio Grande do Sul'),
                   (5, 3, 'Rio de Janeiro');


-- inserindo valores na tabela produtosFornecedores
insert into produtosFornecedores (idProdFor_Produto, idProdFor_Fornecedor, prodFor_Quantidade)
			values (1, 4, 10),				
                   (2, 1, 7),
                   (3, 5, 2),
                   (4, 2, 6),
                   (5, 3, 10);
