-- Criando o Schema Company
create schema if not exists company;
use company;

-- CRIAÇÃO DAS TABELAS USANDO CONSTRAINTS - APENAS EXEMPLO NÃO EXECUTAR
-- Criação com constraints

-- Criando tabela de empregados (employee)
create table employee (
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
    constraint chk_salary_employee check (salary > 2000.0),
    constraint pk_employee primary key (ssn)
);

desc employee;

-- Criando a tabela de departamentos (departamet)
create table departament (
	dname varchar(15) not null,
    dnumber int not null,
    mgr_ssn char(9),
    mgr_start_date date,
    dept_create_date date,
    constraint check_date_dept check (dept_create_date < mgr_start_date),
    constraint pk_dept primary key (dnumber),
    constraint unique_name_dept unique (dname),
    constraint fk_dept foreign key (mgr_ssn) references employee(ssn)
);

desc departament;

-- Criando a tabela localização de departamentos (dept_locations)
create table dept_locations (
	dnumber int not null,
    dlocation varchar(15) not null,
    constraint pk_dept_locatins primary key (dnumber, dlocation),
    constraint fk_dept_locatins foreign key (dnumber) references departament(dnumber)
);

desc dept_locations;

-- Criando a tabela de Projetos (project)
create table project (
	pname varchar(15) not null,
    pnumber int not null,
    plocation varchar(15),
    dnum int not null,
    constraint pk_project primary key (pnumber),
    constraint unique_project unique (pname),
    constraint fk_project foreign key (dnum) references departament(dnumber)
);

desc project;

-- Criando a tabela Trabalha_Para (works_on)
create table works_on (
	essn char(9) not null,
    pno int not null,
    hours decimal(3,1) not null,
    constraint pk_works_on primary key (essn, pno),
    constraint fk_works_on_essn foreign key (essn) references employee(ssn),
    constraint fk_works_on_pno foreign key (pno) references project(pnumber)    
);

desc works_on;

-- Criando a tabela de dependentes (dependent)
create table dependent (
	essn char(9) not null,
    dependent_name varchar(15) not null,
    sex char,
    bdate date,
    relationship varchar(8),
    age int not null,
    constraint chk_age_dependent check (age < 21),
    constraint pk_dependent primary key (essn, dependent_name),
    constraint fk_dependent foreign key (essn) references employee(ssn)
);

desc dependent;

-- Verificando as CONSTRAINTS criadas no Schema Company
select * from information_schema.table_constraints
	where constraint_schema = 'company';

-- Verificando as CONSTRAINTS REFERENCES criadas no Schema Company (Primary Keys)
select * from information_schema.referential_constraints
	where constraint_schema = 'company';
