-- nested (subqueries)
use company;

select distinct pnumber from project;

-- todos em employee
select * from employee;

-- projetos em que Smith trabalha
select distinct p.pnumber
from project as p
where p.pnumber in
	(
		select distinct w.pno
        from works_on as w, employee as e
        where w.essn = e.ssn
        and e.lname = 'Smith'
	)
	or
    (
		select p.pnumber
        from project as p, departament as d, employee as e
        where d.mgr_ssn = e.ssn
		and e.lname = 'Smith'
        and p.dnum = d.dnumber
	);

      
-- projetos em que Smith trabalha e o tempo em horas em cada projeto
select W.pno, W.hours 
from works_on as W, employee as E
where W.essn = E.ssn and E.lname='Smith';

-- projetos em que Smith gerencia
select pnumber 
from project as P, departament as D, employee as E
where P.dnum = D.dnumber 
	and D.mgr_ssn = E.ssn 
	and E.lname='Smith';

--
-- Como retornar ambas informações em uma mesma query? 
--

-- retornar todos os projetos que Smith trabalha e gerencia
select distinct pnumber 
from project 
where pnumber in (select pnumber 
				  from project, departament, employee
				  where dnum =dnumber 
                  and mgr_ssn = ssn 
                  and lname='Smith')
                  or pnumber in (select pno 
								from works_on, employee
								where rssn = ssn 
                                and lname='Smith'
                                );
        
-- comparação com apenas um atributo
select distinct essn 
from works_on 
where (pno, hours) in (select pno, hours 
						from works_on
						where essn = '123456789'
						);
                            
--
-- utilizando keywords
--

-- recuperando os maiores salários se comparados ao departamento 5
select lname, fname, salary 
from employee
where salary > all (select salary 
					from employee 
                    where dno=5
                    );


-- some e any?
select lname, fname, salary 
from employee
where salary = any (select salary 
					from employee 
                    where dno=5
                    );
                     
select lname, fname, salary 
from employee
where salary < all (select salary 
					from employee 
                    where dno=5
                    );
    
select * from employee where dno=5;

--
-- Evitando ambiguidade 
--

select e.fname, e.lname 
from employee as e
where e.ssn in (select d.essn
				from dependent d 
                where e.fname = d.dependent_name
                and e.sex = d.sex
                );
                    
select concat(e.fname, ' ', e.lname) as Complete_Name_Employee 
from employee as e
where e.ssn in (select d.essn 
				from dependent d 
                where e.ssn = d.essn
                and e.sex = d.sex
                );

--
--                    
-- Subqueries com cláusuls existis e unique 
--
--

-- que possuem dependentes
select e.fname, e.lname 
from employee as e
where exists (select *
				from dependent as d 
                where e.ssn=d.essn 
                and e.sex = d.sex
                );

-- recuperando nome de empregados que não possuem dependentes
select e.fname, e.lname 
from employee as e
where not exists (select *
					from dependent as d 
					where e.ssn=d.essn
                    ); 
                      
-- e os gerentes? tem dependentes?
select e.fname, e.lname 
from employee as e
where exists (select *
				from dependent as d 
                where e.ssn=d.essn 
                and e.sex = d.sex
			 )
				and exists (select * 
							from departament
							where ssn = mgr_ssn
                            ); 

-- acima de um n° de dependentes
select e.fname, e.lname 
from employee as e
where exists (select * 
				from dependent as d 
                where e.ssn=d.essn) >= 2; 

--
-- comparando com conjuntos explicítos
--

-- recuperando o ssn de todos empregados que trabalham nos projetos 1,2 ou 3
select distinct essn 
from works_on 
where pno in (1,2,3);
