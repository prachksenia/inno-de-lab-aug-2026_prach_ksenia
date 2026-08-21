-- Homework 4
DROP TABLE IF EXISTS employeeprojects, projects, employees CASCADE;

CREATE TABLE employees (
    employeeid SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

CREATE TABLE projects (
    projectid SERIAL PRIMARY KEY,
    projectname VARCHAR(100) NOT NULL,
    budget DECIMAL(12, 2),
    startdate DATE,
    enddate DATE
);

CREATE TABLE employeeprojects (
    employeeid INT,
    projectid INT,
    hoursworked INT,
    PRIMARY KEY (employeeid, projectid),
    FOREIGN KEY (employeeid) REFERENCES employees(employeeid),
    FOREIGN KEY (projectid) REFERENCES projects(projectid)
);

INSERT INTO employees (firstname, lastname, department, salary) VALUES
('Alice', 'Smith', 'HR', 60000.00),
('Bob', 'Johnson', 'IT', 75000.00),
('Charlie', 'Brown', 'Finance', 62000.00),
('Diana', 'Prince', 'IT', 80000.00),
('Eve', 'Davis', 'HR', 58000.00);

INSERT INTO projects (projectname, budget, startdate, enddate) VALUES
('Website Redesign', 150000.00, '2023-01-15', '2023-06-30'),
('Mobile App Development', 200000.00, '2023-03-01', '2023-10-31'),
('Internal Tools Upgrade', 80000.00, '2023-05-10', '2023-09-15');

INSERT INTO employeeprojects (employeeid, projectid, hoursworked) VALUES
(2, 1, 160),
(4, 1, 120),
(2, 2, 200),
(1, 3, 80),
(3, 3, 100);