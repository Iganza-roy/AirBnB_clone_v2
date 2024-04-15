-- Create database if it does not exist
-- Create a non-existing user and set password
-- Grant all privileges on db to user
-- Grant SELECT privileges on schema to user

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
