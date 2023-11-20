--  prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS gitstore_db;

CREATE USER IF NOT EXISTS 'moharm'@'localhost' 
IDENTIFIED BY 'root@15420';

GRANT SELECT 
ON `performance_schema`.* 
TO 'moharm'@'localhost';

GRANT ALL PRIVILEGES 
ON `gitstore_db`.*
TO 'moharm'@'localhost';
