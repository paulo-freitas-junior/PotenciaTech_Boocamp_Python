-- case statement
use company;
show tables;

UPDATE EMPLOYEE
SET Salary =
	CASE	WHEN Dno = 5 THEN Salary + 2000
			WHEN Dno = 4 THEN Salary + 1500
			WHEN Dno = 1 THEN Salary + 3000
			ELSE (Salary + 0) 
	END;
    
--
-- join statement
--
--

select e.Fname, e.Lname, d.Dname 
	from employee e join departament d;
    
select Fname, Lname, Address 
	from employee e join departament d 
    on Dno = Dnumber;

select * from employee join works_on on ssn = essn;
select * from employee join departament on ssn = mgr_ssn;

select Fname, Lname, Address 
	from employee e join departament d 
    on e.Dno = d.Dnumber 
	where Dname = 'Research';

SELECT Fname, Lname, Address
	FROM EMPLOYEE NATURAL JOIN departament AS dept
	WHERE dept.Dname = 'Research';

--
--
-- inner join - JOIN ON -
-- Mostra apenas o a intersecção existente entre as tabelas
--
show tables;
desc departament;
desc dept_locations;

select Fname, Lname, Dname 
	from employee join departament on Dnumber = Dno;

-- utilizando using para o atributo de junção - ( Dnumber existe com mesmo nome mas duas tabelas )
select * 
from departament join dept_locations
using(Dnumber);
        
SELECT *
FROM employee INNER JOIN dependent ON SSN = Essn;

SELECT Fname, Lname, count(*)
FROM employee INNER JOIN dependent ON SSN = Essn
group by SSN;

select Sex, count(*) from dependent group by Sex;

--
--
-- Junção de três ou mais tabelas
--
--

desc project;
desc departament;

SELECT *
FROM departament INNER JOIN project ON Dnumber = Dnum;

SELECT *
FROM departament INNER JOIN project ON Dnumber = Dnum 
				 INNER JOIN employee ON Mgr_ssn = Ssn;

--
-- com employee
--
desc employee;
SELECT *
FROM departament INNER JOIN project ON Dnumber = Dnum
				 INNER JOIN employee ON Dno = Dnumber;
    

--
-- com works_on
--
SELECT *
FROM departament 
	INNER JOIN project ON Dnumber = Dnum
	INNER JOIN employee ON Dno = Dnumber;


desc works_on;
SELECT *
FROM works_on 
	INNER JOIN project ON Pno = Pnumber
	INNER JOIN employee ON Essn = Ssn;
    
    
SELECT sum(hours),Pname
FROM works_on
	INNER JOIN project p
	ON Pno = Pnumber
	INNER JOIN employee e
    ON Essn = Ssn
group by Pname;


select	concat(Fname, ' ', Lname) as Complete_Name, Dno as DeptNumber, Pname as ProjectName, Plocation as Location
from employee
	inner join works_on on Ssn = Essn
	inner join project on Pno = Pnumber
where Plocation like 'S%'
order by Pnumber;

-- departament, dept_location, employee
select Dnumber, Dname, Fname, concat(Fname,' ',Lname) as Manager, Salary, round(Salary*0.05,2) as Bonus_Salarial
from departament
	inner join dept_locations using (Dnumber)
    inner join employee on Ssn = Mgr_Ssn
group by Dnumber
having count(*)>1;
    
--
--
-- Join em subqueries - NESTED
--
--

desc departament;
show tables;

SELECT a.Fname, a.Lname, a.Salary
	FROM employee a INNER JOIN
		(SELECT Dname, Dnumber, Mgr_ssn
		FROM departament
		WHERE Mgr_start_date < '1980-01-01' AND Mgr_start_date > '1960-01-01') e
		ON a.Ssn = e.Mgr_ssn
	INNER JOIN
		(SELECT *
		FROM project
		WHERE Plocation like '%Houston%') b
		ON e.Dnumber = b.Dnum;


-- gerentes que começaram a atuar a partir de 1980 dentro de Houston
SELECT a.Fname, a.Lname, a.Salary
	FROM employee a INNER JOIN
		(SELECT Dname, Dnumber, Mgr_ssn
		FROM departament
		WHERE Mgr_start_date > '1980-01-01') e
		ON a.Ssn = e.Mgr_ssn
	INNER JOIN
		(SELECT *
		FROM project
		WHERE Plocation like '%Houston%') b
		ON e.Dnumber = b.Dnum;

--
-- Tabela sendo utilizada mais de uma vez na query
--


--
-- Outer JOIN
--


SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name
FROM (EMPLOYEE AS E LEFT OUTER JOIN EMPLOYEE AS S
ON E.Super_ssn = S.Ssn);


-- left outer join = left join
-- MYSQL não permite o uso do full outer join
SELECT Pnumber, Dnum, Lname, Address, Bdate
FROM ((PROJECT OUTER JOIN DEPARTMENT ON Dnum = Dnumber)
			   JOIN EMPLOYEE ON Mgr_ssn = Ssn)
WHERE Plocation = ‘Stafford’;

SELECT E.Lname, S.Lname
FROM EMPLOYEE E, EMPLOYEE S
WHERE E.Super_ssn >= S.Ssn;