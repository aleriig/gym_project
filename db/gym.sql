DROP TABLE IF EXISTS sport_classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    adress VARCHAR(255),
    phone_number VARCHAR(255)
    );

CREATE TABLE sport_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    duration INT,
    member_id SERIAL REFERENCES members(id)
    );

