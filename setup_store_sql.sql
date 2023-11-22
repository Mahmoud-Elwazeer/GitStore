--  prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS gitstore_db;

CREATE USER IF NOT EXISTS 'moharm'@'localhost' 
IDENTIFIED BY 'pass15420';

GRANT SELECT 
ON `performance_schema`.* 
TO 'moharm'@'localhost';

GRANT ALL PRIVILEGES 
ON `gitstore_db`.*
TO 'moharm'@'localhost';
FLUSH PRIVILEGES;



-- GRANT ALL PRIVILEGES ON *.* TO 'moharm'@'localhost' WITH GRANT OPTION;