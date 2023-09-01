-- Populando as tabelas
desc person;

-- Inserindo dados na tabela person (respeitando a ordem dos campos)
insert into	person values
('1','Carolina','Silva','F','1979-08-21','Rua Tal','Cidade J','RJ','Brasil','26054-089'),
('2','Andre','Bezerra','M','1977-05-07','Rua Vrau','Cidade P','SP','Brasil','05789-120'),
('3','Antonio','Lima','M','1987-11-03','Rua B','Cidade Munhoz','SC','Brasil','38704-120'),
('4','Marina','Souza','F','1985-01-28','Rua C','Cidade Pardua','MA','Brasil','85704-350'),
('5','Roberta','Silva','F','1979-08-12','Rua D','Cidade Mare','RJ','Brasil','26089-356'),
('6','Luiz','Silva','M','1974-04-18','Rua Tal','Cidade J','RJ','Brasil','26054-089');

select * from person