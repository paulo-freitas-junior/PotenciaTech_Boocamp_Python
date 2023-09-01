use company;
desc employee;

-- EXPRESSÕES E CONCATENAÇÃO DE STRINGS
-- ------------------------------------

-- recuperando informações dos departamentos presentes em Stafford
select dname as department, mgr_ssn as manager 
from departament d, dept_locations l
where d.Dnumber = l.Dnumber;

-- padrão sql -> || no MySQL usa a função concat()
select dname as department, concat(fname, ' ', lname) from departament d, dept_locations l, employee e
where d.dnumber = l.dnumber and mgr_ssn = e.ssn;

-- recuperando info dos projetos em Stafford
select * from project, departament where dnum = dnumber and plocation = 'Stafford';

-- recuperando info sobre os departamentos e projetos localizados em Stafford
SELECT pnumber, dnum, lname, address, bdate
FROM project, departament, employee
WHERE dnum = dnumber AND mgr_ssn = ssn AND plocation = 'Stafford';

SELECT * FROM employee WHERE dno IN (3,6,9);


-- OPERADORES LÓGICOS
-- ------------------

SELECT bdate, address
FROM employee
WHERE fname = ‘John’ AND minit = ‘B’ AND lname = ‘Smith’;

SELECT fname, lname, address
FROM employee, departament
WHERE dname = ‘Research’ AND dnumber = dno;


-- EXPRESSÕES E ALIAS
-- ------------------

-- recolhendo o valor do INSS-*
select fname, lname, salary, salary*0.011 from employee;
select fname, lname, salary, salary*0.011 as INSS from employee;
select fname, lname, salary, round(salary*0.011,2) as INSS from employee;

-- definir um aumento de salário para os gerentes que trabalham no projeto associado ao ProdutoX
select e.fname, e.lname, (1.1*e.salary) as increased_sal from employee as e,
works_on as w, project as p where e.ssn = w.essn and w.pno = p.pnumber and p.pname='ProductX';

-- concatenando e fornecendo alias
select dname as department, concat(fname, ' ', lname) as Manager from departament d, dept_locations l, employee e
where d.dnumber = l.dnumber and mgr_ssn = e.ssn;

-- recuperando dados dos empregados que trabalham para o departamento de pesquisa
select fname, lname, address from employee, departament
	where dname = 'Research' and dnumber = dno;

-- definindo alias para legibilidade da consulta
select e.fname, e.lname, e.address from employee e, departament d
	where d.dname = 'Research' and d.dnumber = e.dno;