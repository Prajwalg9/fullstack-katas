create database if not exists Students;
Use Students;

-- drop database Students;

CREATE TABLE IF NOT EXISTS Students(
	Student_id INT PRIMARY KEY AUTO_INCREMENT,
    First_name VARCHAR(100),
    Last_name VARCHAR(100),
    Age TINYINT,
    Email VARCHAR (100),
    DOB DATE,
    Join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE Students
modify Email varchar(100) unicode;


SELECT * FROM Students;

INSERT INTO Students(First_name, Last_name, Age, Email, DOB)
VALUES ("Nikhil","Gavali",16,"nikhilgg99@gmail.com","20-09-02");

-- drop table Students;

-- truncate table Students;


