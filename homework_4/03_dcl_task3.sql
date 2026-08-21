-- Homework 4, Task 3: DCL

CREATE ROLE hr_user WITH LOGIN PASSWORD 'hr_password123';

GRANT USAGE ON SCHEMA public TO hr_user;
GRANT SELECT ON employees TO hr_user;

-- Test 1: SELECT должен работать
SELECT * FROM employees;

-- Test 2: INSERT без прав → permission denied
INSERT INTO employees (firstname, lastname, department, salary)
VALUES ('Test', 'Fail', 'HR', 40000.00);

-- Выдать INSERT, UPDATE и права на sequence (admin)
GRANT INSERT, UPDATE ON employees TO hr_user;
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;

-- Test 3: INSERT и UPDATE должны работать (hr_user)
INSERT INTO employees (firstname, lastname, department, salary)
VALUES ('Test', 'Fail', 'HR', 40000.00);

UPDATE employees
SET salary = 41000.00
WHERE firstname = 'Test' AND lastname = 'Fail';

SELECT * FROM employees;

-- Удаление тестовых строк (admin)
DELETE FROM employees
WHERE firstname = 'Test' AND lastname = 'Fail';
