-- Homework 4, Task 5: Functions and Views

-- 1. Функция CalculateAnnualBonus (Бонус = 10% от Salary)
CREATE OR REPLACE FUNCTION calculateannualbonus(
    p_employee_id INT,
    p_salary DECIMAL(10, 2)
)
RETURNS DECIMAL(10, 2)
LANGUAGE plpgsql
AS $$
DECLARE
    bonus DECIMAL(10, 2);
BEGIN
    bonus := p_salary * 0.10;
    RETURN bonus;
END;
$$;

-- 2. SELECT с функцией — бонус для каждого сотрудника
SELECT
    employeeid,
    firstname,
    lastname,
    salary,
    calculateannualbonus(employeeid, salary) AS annual_bonus
FROM employees;

-- 3. Представление IT_Department_View
CREATE OR REPLACE VIEW it_department_view AS
SELECT
    employeeid,
    firstname,
    lastname,
    salary
FROM employees
WHERE department = 'IT';

-- 4. SELECT из представления
SELECT * FROM it_department_view;
