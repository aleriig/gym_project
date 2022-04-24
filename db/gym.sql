DROP TABLE IF EXISTS booking_lists;
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

CREATE TABLE booking_lists (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id),
    sport_class_id SERIAL REFERENCES sport_classes(id)
);