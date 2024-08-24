CREATE DATABASE hospital;

USE hospital;

CREATE TABLE login(
user VARCHAR(50) NOT NULL,
last VARCHAR(50) NOT NULL,
email VARCHAR(100) PRIMARY KEY NOT NULL,
password VARCHAR(50) NOT NULL,
dates VARCHAR(50) NOT NULL,
PHno BIGINT NOT NULL
);

SELECT * FROM login;

CREATE TABLE patient(
patisno BIGINT PRIMARY KEY NOT NULL,
name VARCHAR(50) NOT NULL,
age INT NOT NULL,
ward VARCHAR(50) NOT NULL,
problem VARCHAR(50) NOT NULL,
PHno BIGINT NOT NULL
);


INSERT INTO patient
(patisno,name,age,ward,problem,PHno)
VALUES
(6,"rh",20,"icu","nil",334433),
(7,"rh",20,"gernal","nil",334433),
(8,"rh",20,"delux","nil",334433),
(9,"rh",20,"gernal","nil",334433),
(10,"rh",20,"icu","nil",334433),
(11,"rh",20,"delux","nil",334433),
(12,"rh",20,"gernal","nil",334433),
(13,"rh",20,"childrens","nil",334433),
(14,"rh",20,"childrens","nil",334433),
(15,"rh",20,"gernal","nil",334433),
(16,"rh",20,"childrens","nil",334433);


SELECT * FROM patient;

SELECT COUNT(ward) FROM patient WHERE ward = 'icu';

CREATE TABLE feedback(
email VARCHAR(100) PRIMARY KEY ,
phoneno VARCHAR(10) NOT NULL,
revew VARCHAR(300) NOT NULL
);
#DROP TABLE feedback;
SELECT * FROM feedback;


CREATE TABLE staff(
staffno BIGINT PRIMARY KEY NOT NULL,
name VARCHAR(50) NOT NULL,
age INT NOT NULL,
work VARCHAR(50) NOT NULL,
PHno VARCHAR(10) NOT NULL
);

DROP TABLE staff;
SELECT * FROM staff;






