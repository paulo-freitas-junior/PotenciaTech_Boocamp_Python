-- Criando o Schema Company
create schema if not exists company;

-- Mudando para o schema 'company'
use company;

-- CRIAÇÃO DAS TABELAS DE FORMA SIMPLES 
-- Criação com constraints abordada em outro script

-- Criando tabela de empregados (employee)
create table company.employee (
	fname varchar(15) not null,
    mint char,
    lname varchar(15) not null,
    ssn char(9) not null,
    bdate date,
    address varchar(30),
    sex char,
    salary decimal(10,2),
    super_ssn char(9),
    dno int not null,
    primary key (ssn)
);

-- Criando a tabela de departamentos (departamet)
create table departament (
	dname varchar(15) not null,
    dnumber int not null,
    mgr_ssn char(9),
    mgr_start_date date,
    dept_create_date date,
    primary key (dnumber),
    unique (dname),
    foreign key (mgr_ssn) references employee(ssn)
);

-- Criando a tabela localização de departamentos (dept_locations)
create table dept_locations (
	dnumber int not null,
    dlocation varchar(15) not null,
    primary key (dnumber, dlocation),
    foreign key (dnumber) references departament(dnumber)
);

-- Criando a tabela de Projetos (project)
create table project (
	pname varchar(15) not null,
    pnumber int not null,
    plocation varchar(15),
    dnum int not null,
    primary key (pnumber),
    unique (pname),
    foreign key (dnum) references departament(dnumber)
);

-- Criando a tabela Trabalha_Para (works_on)
create table works_on (
	essn char(9) not null,
    pno int not null,
    hours decimal(3,1) not null,
    primary key (essn, pno),
    foreign key (essn) references employee(ssn),
    foreign key (pno) references project(pnumber)    
);

-- Criando a tabela de dependentes (dependent)
create table dependent (
	essn char(9) not null,
    dependent_name varchar(15) not null,
    sex char,
    bdate date,
    relationship varchar(8),
    primary key (essn, dependent_name),
    foreign key (essn) references employee(ssn)
);

show tables;
desc departament;