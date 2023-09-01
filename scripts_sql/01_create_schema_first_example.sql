-- Criando meu primeiro SCHEMA no MySQL
show schemas;			-- visualiza os schemas existentes
show databases;			-- visualiza os banco de dados existentes

-- Criando a database (automaticamente cria o schema com mesmo nome)
create database if not exists first_example;

-- Alterando para o database criado
use first_example;

-- Verificando se existem tabelas
show tables;

-- Criando a primeira tabela do banco de dados
create table person (
	person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	gender enum('M','F'),
	birth_date date,
	street varchar(30),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
    constraint pk_person primary key (person_id)
);

-- Exibe uma descrição da estrutura da Tabela
desc person;

-- Criando a tabela Favorite Food
create table favorite_food (
	person_id smallint unsigned,
    food varchar(20),
    constraint pk_favorite_food primary key (person_id, food),
    constraint fk_favorite_food_person_id foreign key (person_id) references person(person_id)
);

-- Exibindo a estrutura da Tabela
desc favorite_food;

-- Exibindo as Chaves primárias e Extrangeiras criadas
show databases;
select * from information_schema.table_constraints
	where constraint_schema = 'first_example';
