create database  ems;
use ems;
create table employee(id int primary key auto_increment,name varchar(50),salary int);

select* from employee;

describe employee;


alter table employee drop  id;
alter table employee add column id int primary key auto_increment;
alter table employee change name NAME VARCHAR(50);

insert into employe+e(NAME,salary)
values('suraj',52000),
      ('Sanjana',10000),
      ('Ritu',2000000);
      
delete from employee where id=0;

select SALARY from  employee;