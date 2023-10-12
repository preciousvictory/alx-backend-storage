--  a SQL script that creates a table users
DROP TABLE IF EXISTS users;
CREATE TABLE users( id int NOT NULL AUTO_INCREMENT PRIMARY KEY, email varchar(255) UNIQUE, name varchar(255) );
