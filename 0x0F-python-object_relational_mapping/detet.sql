-- DROP DATABASE hbtn_0e_0_usa

/*
SHOW DATABASES;
DROP DATABASE hbtn_0e_6_usa;
SELECT '----------------------------------------';
SHOW DATABASES;
*/

USE hbtn_0e_6_usa;
show tables;
SELECT * FROM states;
/* FROM states WHERE id = 9 AND name = 'Louisiana';*/
DELETE FROM states WHERE name = 'Nevada';
SELECT * FROM states;
/*
cat detet.sql | sudo mysql -hlocalhost -uroot
*/