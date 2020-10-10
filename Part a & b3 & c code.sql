#DROP DATABASE IF EXISTS db_consumer_panel;
CREATE DATABASE db_consumer_panel;
use db_consumer_panel;

DROP TABLE IF EXISTS households;
CREATE TABLE households(
hh_id    		BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
hh_race     	INT,
hh_is_latinx   	INT,
hh_income   	INT,
hh_size     	INT,
hh_zip_code   	VARCHAR(5),
hh_state   		VARCHAR(2),
hh_residence_type INT,
primary key   (hh_id)
);

DROP TABLE IF EXISTS products;
CREATE Table products(               
brand_at_prod_id         VARCHAR(100),
department_at_prod_id    VARCHAR(100),
prod_id                  BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
group_at_prod_id         VARCHAR(100),
module_at_prod_id        VARCHAR(100),
amount_at_prod_id        DECIMAL(6,2),
units_at_prod_id         VARCHAR(100),
Primary Key 			 (prod_id)
);

DROP TABLE IF EXISTS trips;
CREATE TABLE trips(
hh_id                        BIGINT UNSIGNED NOT NULL,
TC_date                      DATE,
TC_retailer_code             INT NOT NULL, 
TC_retailer_code_store_code  INT NOT NULL,                 
TC_retailer_code_store_zip3  INT,
TC_total_spent               DECIMAL(6,2) NOT NULL,
TC_id                        INT UNSIGNED NOT NULL AUTO_INCREMENT,
PRIMARY KEY  (TC_id)                
);

DROP TABLE IF EXISTS purchases;
create table purchases(
TC_id							INT UNSIGNED NOT NULL,
quantity_at_TC_prod_id  		INT,
total_price_paid_at_TC_prod_id  FLOAT,
coupon_value_at_TC_prod_id      FLOAT,
deal_flag_at_TC_prod_id			FLOAT,
prod_id							BIGINT UNSIGNED NOT NULL
);

ALTER TABLE trips ADD CONSTRAINT FK_hh_id FOREIGN KEY (hh_id) REFERENCES households(hh_id);
ALTER TABLE purchases ADD CONSTRAINT FK_TC_id FOREIGN KEY (TC_id) REFERENCES trips(TC_id);
ALTER TABLE purchases ADD CONSTRAINT FK_prod_id FOREIGN KEY (prod_id) REFERENCES products(prod_id);


## Part A—1,2,3
SELECT count(DISTINCT TC_id) FROM trips;
SELECT count(DISTINCT hh_id) FROM households;
SELECT COUNT(DISTINCT TC_retailer_code) FROM trips;
SELECT COUNT(DISTINCT TC_retailer_code_store_code) FROM trips;

## Part A-4
SELECT count(DISTINCT prod_id) FROM products;
SELECT department_at_prod_id, count(prod_id) FROM products GROUP BY department_at_prod_id;
SELECT department_at_prod_id, count(DISTINCT module_at_prod_id) FROM products GROUP BY department_at_prod_id;
SELECT module_at_prod_id, count(prod_id) FROM products GROUP BY module_at_prod_id;
SELECT group_at_prod_id, count(prod_id) FROM products GROUP BY group_at_prod_id;
SELECT count(DISTINCT module_at_prod_id) FROM products;
SELECT count(DISTINCT group_at_prod_id) FROM products;


## Part A-5
Select count(TC_id) from purchases where coupon_value_at_TC_prod_id >0 or deal_flag_at_TC_prod_id>0;


## part B-3-1
Drop table if exists TC_month;
Create temporary table TC_month 
 Select purchases.quantity_at_TC_prod_id, purchases.TC_id, purchases.total_price_paid_at_TC_prod_id, trips.hh_id, trips.TC_date from purchases
 inner join trips
 on trips.TC_id=purchases.TC_id;

Drop table if exists TC_month2003;
Create temporary table TC_month2003
select hh_id, quantity_at_TC_prod_id, TC_id, total_price_paid_at_TC_prod_id/quantity_at_TC_prod_id as price_per_item, TC_date from TC_month
where year(TC_date)="2003"; 
SELECT * FROM TC_month2003;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM TC_month2003 GROUP BY hh_id) as a;
select sum(quantity_at_TC_prod_id), month(TC_date) from TC_month2003 group by month(TC_date);
select sum(quantity_at_TC_prod_id), date(TC_date) from TC_month2003 group by date(TC_date);
select avg(quantity_at_TC_prod_id), month(TC_date) from TC_month2003 group by month(TC_date);

Drop table if exists TC_month2004;
Create temporary table TC_month2004
select hh_id, quantity_at_TC_prod_id, TC_id, total_price_paid_at_TC_prod_id/quantity_at_TC_prod_id as price_per_item, TC_date from TC_month
where year(TC_date)="2004"; 
SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=1;

select sum(quantity_at_TC_prod_id), month(TC_date) from TC_month2004 group by month(TC_date);
select avg(quantity_at_TC_prod_id), month(TC_date) from TC_month2004 group by month(TC_date);


##part B-3-2
select count(TC_id), month(TC_date)from TC_month2004 group by month(TC_date); 
select count(TC_id), month(TC_date)from TC_month2003 group by month(TC_date);

SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=1) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=2) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=3) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=4) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=5) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=6) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=7) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=8) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=9) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=10) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=11) as a GROUP BY hh_id) as b;
SELECT avg(c) FROM (SELECT hh_id, count(DISTINCT TC_id) as c FROM (SELECT hh_id, TC_id, TC_date from TC_month2004 where month(TC_date)=12) as a GROUP BY hh_id) as b;


##part C-2
SELECT avg(quantity_at_TC_prod_id), avg(price_per_item), month(TC_date) from TC_month2003 group by month(TC_date);
SELECT avg(quantity_at_TC_prod_id), avg(price_per_item), month(TC_date) from TC_month2004 group by month(TC_date);


##Part C-3-2
DROP TABLE IF EXISTS Private_label;
Create temporary table Private_label
Select * from products where brand_at_prod_id="CTL BR" ;

DROP TABLE IF EXISTS Private_label_and_total1; 
Create temporary table Private_label_and_total1
select private_label.prod_id, trips.TC_id,purchases.quantity_at_TC_prod_id,purchases.total_price_paid_at_TC_prod_id,trips.TC_date,trips.TC_total_spent from private_label
inner join purchases 
on purchases.prod_id=private_label.prod_id
inner join trips
on trips.TC_id=purchases.TC_id
where year(TC_date)=2003;

select month(trips.TC_date),
   sum(Private_label_and_total1.total_price_paid_at_TC_prod_id),
            sum(trips.TC_total_spent),
            sum(Private_label_and_total1.total_price_paid_at_TC_prod_id)/sum(trips.TC_total_spent)
            from Private_label_and_total1 
Inner join trips
on trips.TC_id= Private_label_and_total1.TC_id
group by month(TC_date);

DROP TABLE IF EXISTS Private_label_and_total2;
Create temporary table Private_label_and_total2
select private_label.prod_id, trips.TC_id,purchases.quantity_at_TC_prod_id,purchases.total_price_paid_at_TC_prod_id,trips.TC_date,trips.TC_total_spent from private_label
inner join purchases 
on purchases.prod_id=private_label.prod_id
inner join trips
on trips.TC_id=purchases.TC_id
where year(TC_date)=2004;

select month(trips.TC_date),
   sum(Private_label_and_total2.total_price_paid_at_TC_prod_id),
            sum(trips.TC_total_spent),
            sum(Private_label_and_total2.total_price_paid_at_TC_prod_id)/sum(trips.TC_total_spent)
            from Private_label_and_total2 
Inner join trips
on trips.TC_id= Private_label_and_total2.TC_id
group by month(TC_date);