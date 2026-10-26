CREATE DATABASE student_management;

USE student_management;

CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    course_id INT,
    marks INT,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

INSERT INTO Department VALUES
(1, 'Computer Science'),
(2, 'Commerce');

INSERT INTO Course VALUES
(101, 'BCA', 1),
(102, 'BCom', 2);

INSERT INTO Student VALUES
(1, 'Arun', 101, 85),
(2, 'Anu', 101, 90);

SELECT * FROM Student;