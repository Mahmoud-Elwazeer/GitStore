--  prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS store_test_db;

CREATE USER IF NOT EXISTS 'store_test'@'localhost' 
IDENTIFIED BY 'store_test_pwd';

GRANT SELECT 
ON `performance_schema`.* 
TO 'store_test'@'localhost';

GRANT ALL PRIVILEGES 
ON `store_test_db`.*
TO 'store_test'@'localhost';