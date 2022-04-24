DROP TABLE IF EXISTS sport_classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    address VARCHAR(255),
    phone_number VARCHAR(255)
    );

CREATE TABLE sport_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(225),
    duration INT
    );

