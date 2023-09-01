SHOW databases

CREATE DATABASE firstExample;

USE firstExample;

show tables;

create table periodicos(
id int auto_increment primary key,
nome_periodico varchar(20),
issn int,
id_editora int
);

create table editora(
id int auto_increment,
nome_editora varchar(120) unique,
pais varchar(5),
primary key(id)
);

alter table periodicos add constraint fk_editora_periodico foreign key(id_editora) references editora(id)

insert into editora(nome_editora, pais)
values ('IEEE','EUA'),('DataScienceMagazine','EUA');

select	* from editora

select * from periodicos;

insert into periodicos(nome_periodico, issn, id_editora)
values ('Special Issue','12345678','1');

select * from periodicos;


