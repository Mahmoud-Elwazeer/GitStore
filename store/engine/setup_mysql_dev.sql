--  prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS store_dev_db;

CREATE USER IF NOT EXISTS 'store_dev'@'localhost' 
IDENTIFIED BY 'store_dev_pwd';

GRANT SELECT 
ON `performance_schema`.* 
TO 'store_dev'@'localhost';

GRANT ALL PRIVILEGES 
ON `store_dev_db`.*
TO 'store_dev'@'localhost';