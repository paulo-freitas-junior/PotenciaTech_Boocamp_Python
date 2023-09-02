-- Criação do Schema de Bando de Dados Farmacia

CREATE SCHEMA IF NOT EXISTS farmacia;
USE farmacia;


-- criando a tabela farmacia
CREATE TABLE IF NOT EXISTS tipos_produto(
  id INT NOT NULL AUTO_INCREMENT,
  tipo VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
  );


-- criando a tabela fabricantes
CREATE TABLE IF NOT EXISTS fabricantes(
	id INT NOT NULL AUTO_INCREMENT,
	fabricante VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);


-- criando a tabela produtos
CREATE TABLE IF NOT EXISTS produtos(
	id INT NOT NULL AUTO_INCREMENT,
	id_fabricante INT NOT NULL,
	id_tipo_produto INT NOT NULL,
	produto VARCHAR(45) NOT NULL,
	designacao VARCHAR(200) NOT NULL,
	composicao VARCHAR(200) NOT NULL,
	preco DECIMAL(8,2) NOT NULL,
PRIMARY KEY (id),
INDEX fk_produtos_1_idx (id_fabricante ASC),
INDEX fk_produtos_2_idx (id_tipo_produto ASC),
CONSTRAINT fk_produtos_1 FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
CONSTRAINT fk_produtos_2 FOREIGN KEY (id_tipo_produto) REFERENCES tipos_produto(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- criando a tabela clientes
CREATE TABLE IF NOT EXISTS clientes(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	endereco VARCHAR(200) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	cep VARCHAR(15) NOT NULL,
	localidade VARCHAR(45) NOT NULL,
	cpf VARCHAR(15) NOT NULL,
PRIMARY KEY (`id`)
);


-- criando a tabela compras
CREATE TABLE IF NOT EXISTS compras(
	id INT NOT NULL AUTO_INCREMENT,
	id_cliente INT NOT NULL,
	data DATE NOT NULL,
PRIMARY KEY (id),
INDEX fk_compras_1_idx (id_cliente ASC),
CONSTRAINT fk_compras_1 FOREIGN KEY (id_cliente) REFERENCES clientes(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- criando a tabela médicos
CREATE TABLE IF NOT EXISTS medicos(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	crm VARCHAR(45) NOT NULL,
PRIMARY KEY (id)
);


-- criando a tabela de compra de produtos
CREATE TABLE IF NOT EXISTS produtos_compra(
	id INT NOT NULL AUTO_INCREMENT,
	id_produto INT NOT NULL,
	id_compra INT NOT NULL,
	quantidade INT NOT NULL,
PRIMARY KEY (id),
INDEX fk_produtos_compra_1_idx (id_produto ASC),
INDEX fk_produtos_compra_2_idx (id_compra ASC),
CONSTRAINT fk_produtos_compra_1 FOREIGN KEY (id_produto) REFERENCES produtos(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
CONSTRAINT fk_produtos_compra_2 FOREIGN KEY (id_compra) REFERENCES compras(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- criando a tabela de receitas médicas
CREATE TABLE IF NOT EXISTS receitas_medica(
	id INT NOT NULL AUTO_INCREMENT,
	id_medico INT NOT NULL,
	id_produto_compra INT NOT NULL,
	receita VARCHAR(45) NOT NULL,
PRIMARY KEY (id),
INDEX fk_receitas_medica_1_idx (id_produto_compra ASC),
INDEX fk_receitas_medica_2_idx (id_medico ASC),
CONSTRAINT fk_receitas_medica_1 FOREIGN KEY (id_produto_compra) REFERENCES produtos_compra(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
CONSTRAINT fk_receitas_medica_2 FOREIGN KEY (id_medico) REFERENCES medicos(id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
