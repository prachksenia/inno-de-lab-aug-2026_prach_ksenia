-- Homework 4, Task 4: DML

-- Проверка: состояние до изменений
SELECT * FROM employees;
SELECT * FROM employeeprojects;

-- 1. Увеличить Salary всех сотрудников отдела HR на 10%
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'HR';

-- 2. Department = 'Senior IT' для всех с Salary > 70000
UPDATE employees
SET department = 'Senior IT'
WHERE salary > 70000.00;

-- 3. Удалить сотрудников без проектов (NOT EXISTS)
DELETE FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employeeprojects ep
    WHERE ep.employeeid = e.employeeid
);

-- 4. Транзакция: новый проект + 2 сотрудника
BEGIN;

INSERT INTO projects (projectname, budget, startdate, enddate)
VALUES ('Data Analytics Platform', 120000.00, '2024-01-01', '2024-12-31');

INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
VALUES
    (2, currval('projects_projectid_seq'), 100),  -- Bob Johnson
    (4, currval('projects_projectid_seq'), 80);   -- Diana Prince

COMMIT;

-- Проверка результата
SELECT * FROM employees;
SELECT * FROM projects ORDER BY projectid;
SELECT ep.*, e.firstname, e.lastname, p.projectname
FROM employeeprojects ep
JOIN employees e ON e.employeeid = ep.employeeid
JOIN projects p ON p.projectid = ep.projectid
ORDER BY ep.projectid, ep.employeeid;

SELECT * FROM employees;