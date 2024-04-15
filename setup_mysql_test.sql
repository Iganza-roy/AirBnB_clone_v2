-- Create database if it does not exist
-- Create a non-existing user and set password
-- Grant all privileges on db to user
-- Grant SELECT privileges on schema to user

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
