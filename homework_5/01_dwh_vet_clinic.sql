-- Homework 5: Data Warehouse — Vet Clinic (Star Schema)
-- Бизнес-процесс: учёт и анализ ветеринарных приёмов
-- Grain: одна строка = один ветеринарный приём

-- DROP (для повторного запуска) 

DROP TABLE IF EXISTS fact_appointments CASCADE;
DROP TABLE IF EXISTS dim_appointment_status CASCADE;
DROP TABLE IF EXISTS dim_veterinarian CASCADE;
DROP TABLE IF EXISTS dim_pet CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;

-- DIMENSIONS

CREATE TABLE dim_date (
    date_sk        SERIAL PRIMARY KEY,
    source_date_id DATE NOT NULL UNIQUE,
    year           INT NOT NULL,
    quarter        INT NOT NULL,
    month          INT NOT NULL,
    day            INT NOT NULL,
    day_of_week    VARCHAR(10) NOT NULL
);

CREATE TABLE dim_pet (
    pet_sk          SERIAL PRIMARY KEY,
    source_pet_id   VARCHAR(50) NOT NULL,
    pet_name        VARCHAR(100) NOT NULL,
    species         VARCHAR(50) NOT NULL,
    birth_date      DATE,
    owner_full_name VARCHAR(200) NOT NULL
);

CREATE TABLE dim_veterinarian (
    veterinarian_sk SERIAL PRIMARY KEY,
    source_vet_id   VARCHAR(50) NOT NULL,
    full_name       VARCHAR(100) NOT NULL,
    specialization  VARCHAR(100),
    license_number  VARCHAR(50)
);

CREATE TABLE dim_appointment_status (
    appointment_status_sk SERIAL PRIMARY KEY,
    status_code           VARCHAR(20) NOT NULL UNIQUE,
    status_description    VARCHAR(100) NOT NULL
);

--  FACT TABLE 

CREATE TABLE fact_appointments (
    appointment_sk        SERIAL PRIMARY KEY,
    date_sk               INT NOT NULL REFERENCES dim_date(date_sk),
    pet_sk                INT NOT NULL REFERENCES dim_pet(pet_sk),
    veterinarian_sk       INT NOT NULL REFERENCES dim_veterinarian(veterinarian_sk),
    appointment_status_sk INT NOT NULL REFERENCES dim_appointment_status(appointment_status_sk),
    service_cost          DECIMAL(10, 2) NOT NULL,
    visit_duration_minutes INT NOT NULL
);

--  Тестовые данные 

INSERT INTO dim_date (source_date_id, year, quarter, month, day, day_of_week) VALUES
('2024-03-15', 2024, 1, 3, 15, 'Friday'),
('2024-03-16', 2024, 1, 3, 16, 'Saturday'),
('2024-04-01', 2024, 2, 4, 1, 'Monday'),
('2024-04-02', 2024, 2, 4, 2, 'Tuesday');

INSERT INTO dim_pet (source_pet_id, pet_name, species, birth_date, owner_full_name) VALUES
('P-001', 'Barsik', 'Cat', '2020-05-10', 'Ivanova Anna'),
('P-002', 'Sharik', 'Dog', '2019-08-22', 'Petrov Petr'),
('P-003', 'Kesha', 'Bird', '2021-01-15', 'Sidorova Maria');

INSERT INTO dim_veterinarian (source_vet_id, full_name, specialization, license_number) VALUES
('V-01', 'Dr. Smirnov', 'Surgery', 'LIC-1001'),
('V-02', 'Dr. Kozlova', 'Therapy', 'LIC-1002');

INSERT INTO dim_appointment_status (status_code, status_description) VALUES
('scheduled', 'Appointment is scheduled'),
('completed', 'Appointment is completed'),
('cancelled', 'Appointment is cancelled');

INSERT INTO fact_appointments (date_sk, pet_sk, veterinarian_sk, appointment_status_sk, service_cost, visit_duration_minutes) VALUES
(1, 1, 2, 2, 2500.00, 30),
(1, 2, 1, 2, 4000.00, 45),
(2, 3, 2, 2, 1500.00, 20),
(3, 2, 1, 1, 0.00, 0),
(4, 1, 2, 3, 0.00, 0),
(4, 2, 2, 2, 3500.00, 40);

--  ANALYTICAL QUERIES 

-- Q1: Сколько приёмов было по каждому статусу?
SELECT
    das.status_code,
    das.status_description,
    COUNT(*) AS appointments_count
FROM fact_appointments fa
JOIN dim_appointment_status das ON fa.appointment_status_sk = das.appointment_status_sk
GROUP BY das.status_code, das.status_description
ORDER BY appointments_count DESC;

-- Q2: Какая выручка по месяцам?
SELECT
    dd.year,
    dd.month,
    SUM(fa.service_cost) AS monthly_revenue
FROM fact_appointments fa
JOIN dim_date dd ON fa.date_sk = dd.date_sk
GROUP BY dd.year, dd.month
ORDER BY dd.year, dd.month;

-- Q3: Кто из ветеринаров провёл больше всего приёмов?
SELECT
    dv.full_name,
    COUNT(*) AS appointments_count
FROM fact_appointments fa
JOIN dim_veterinarian dv ON fa.veterinarian_sk = dv.veterinarian_sk
GROUP BY dv.full_name
ORDER BY appointments_count DESC;

-- Q4: Средняя стоимость приёма по видам животных (species)?
SELECT
    dp.species,
    ROUND(AVG(fa.service_cost), 2) AS avg_service_cost
FROM fact_appointments fa
JOIN dim_pet dp ON fa.pet_sk = dp.pet_sk
GROUP BY dp.species
ORDER BY avg_service_cost DESC;

-- Q5: В какие дни недели больше всего завершённых приёмов?
SELECT
    dd.day_of_week,
    COUNT(*) AS completed_appointments
FROM fact_appointments fa
JOIN dim_date dd ON fa.date_sk = dd.date_sk
JOIN dim_appointment_status das ON fa.appointment_status_sk = das.appointment_status_sk
WHERE das.status_code = 'completed'
GROUP BY dd.day_of_week
ORDER BY completed_appointments DESC;