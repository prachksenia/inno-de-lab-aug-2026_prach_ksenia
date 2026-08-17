-- Homework 4, Task 1: DML

-- 1. Вставить двух новых сотрудников (отдел НЕ IT)
INSERT INTO employees (firstname, lastname, department, salary) VALUES
('Anna', 'Ivanova', 'HR', 55000.00),
('Petr', 'Petrov', 'Finance', 59000.00);

-- 2. Выбрать всех сотрудников
SELECT * FROM employees;

-- 3. FirstName и LastName только отдел IT
SELECT firstname, lastname
FROM employees
WHERE department = 'IT';

-- 4. Обновить Salary Alice Smith до 65000.00
UPDATE employees
SET salary = 65000.00
WHERE firstname = 'Alice' AND lastname = 'Smith';

-- 5. Удалить Eve Davis
DELETE FROM employees
WHERE firstname = 'Eve' AND lastname = 'Davis';

-- 6. Проверить все изменения
SELECT * FROM employees;