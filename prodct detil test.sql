create database ems;
use ems;
create table productdetils(productid int primary key auto_increment, productname varchar(50), productcategory varchar(60), productbrand varchar(55),product_price int);
select * from productdetils;
insert into productdetils (productname,productcategory,productbrand,product_price)
values ('watch','chrograph','mars',8000),
		('mobile','smartphone','apple',20000),
        ('laptop','compact','victas',40000),
        ('TV','network','samsung',30000),
        ('Headphone','headset','apple',2500);
alter table productdetils drop productbrand;
alter table productdetils add column productdiscout int;
