-- Homework 4, Task 2: DDL

-- 1. Создать таблицу Departments
CREATE TABLE departments (
    departmentid SERIAL PRIMARY KEY,
    departmentname VARCHAR(50) UNIQUE NOT NULL,
    location VARCHAR(50)
);

-- 2. Добавить столбец Email в Employees
ALTER TABLE employees ADD COLUMN email VARCHAR(100);

-- 3. Заполнить Email уникальными значениями для всех текущих сотрудников
UPDATE employees SET email = 'alice.smith@company.com'
WHERE firstname = 'Alice' AND lastname = 'Smith';

UPDATE employees SET email = 'bob.johnson@company.com'
WHERE firstname = 'Bob' AND lastname = 'Johnson';

UPDATE employees SET email = 'charlie.brown@company.com'
WHERE firstname = 'Charlie' AND lastname = 'Brown';

UPDATE employees SET email = 'diana.prince@company.com'
WHERE firstname = 'Diana' AND lastname = 'Prince';

UPDATE employees SET email = 'anna.ivanova@company.com'
WHERE firstname = 'Anna' AND lastname = 'Ivanova';

UPDATE employees SET email = 'petr.petrov@company.com'
WHERE firstname = 'Petr' AND lastname = 'Petrov';

-- 4. Добавить ограничение UNIQUE на Email
ALTER TABLE employees ADD CONSTRAINT uq_employees_email UNIQUE (email);

-- 5. Переименовать Location -> OfficeLocation в Departments
ALTER TABLE departments RENAME COLUMN location TO officelocation;

-- Проверка
SELECT * FROM departments;
SELECT employeeid, firstname, lastname, email FROM employees;