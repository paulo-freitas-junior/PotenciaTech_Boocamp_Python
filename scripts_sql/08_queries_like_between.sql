-- como utilizar like e between nas queries
use company;
select * from employee;

-- usando a COMPARAÇÃO (like) e a STRING MATCHING (%)
-- STRING MATCHING: _ e % 
-- String _ refere-se apenas á um caracter
-- String % refere-se à um matching de um ou mais elementos

select fname, lname 
from employee 
where address like '%Houston-TX%';

select fname, lname 
from employee 
where bdate like '19________';

select fname, lname 
from employee 
where bdate like '19__-__-__';

select fname, lname 
from employee 
where bdate like '__7_-__-__';

select fname, lname, bdate 
from employee 
where bdate like '__6%';

select fname, lname, bdate 
from employee
where bdate like '196%';

-- INTERVALO (between)
select dno, salary from employee;

select * 
from employee 
where (salary between 30000 and 40000);

select * 
from employee 
where (salary between 30000 and 40000) and dno=5;

-- como utilizar like e between nas queries

select Fname, Lname from employee where Address like '%Houston-TX%';

select Fname, Lname from employee where Bdate like '19________';
select Fname, Lname from employee where Bdate like '19__-__-__';
select Fname, Lname from employee where Bdate like '__7_-__-__';

select Fname, Lname, Bdate from employee where Bdate like '__6%';
select Fname, Lname, Bdate from employee where Bdate like '196%';

select Dno, Salary from employee;
select * from employee where (Salary between 30000 and 40000);
select * from employee where (Salary between 30000 and 40000) and Dno=5;

-- recuperando informações dos departamentos presentes em Stafford
select dname as Departament_Name, mgr_ssn as Manager
from departament d, dept_locations l, employee e
where d.dnumber = l.dnumber and dlocation = 'Stafford';

-- recuperando todos os gerentes que trabalhão em Stafford
select dname as Departament_Name, mgr_ssn as Manager
from departament d, dept_locations l, employee e
where d.dnumber = l.dnumber and dlocation = 'Stafford' and mgr_ssn = e.ssn;

-- recuperando todos os gerentes, departamentos e seus nomes
select d.dname as Departament_Name, concat(e.fname, ' ', e.lname) as Manager, d.mgr_ssn as Manager, l.dlocation
from departament d, dept_locations l, employee e
where d.dnumber = l.dnumber and mgr_ssn = e.ssn;

