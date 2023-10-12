--  a SQL script that creates a table users
CREATE TABLE users( id int NOT NULL AUTO_INCREMENT, email varchar(255), name varchar(255), PRIMARY KEY (ID), UNIQUE (email) );
