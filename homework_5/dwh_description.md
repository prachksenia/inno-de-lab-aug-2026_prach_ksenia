# Homework 5: Data Warehouse — Ветеринарная клиника

**Выбранная предметная область:** ветеринарная клиника (на основе домашнего задания 2).

## 1. Бизнес-процесс для DWH

**Процесс:** учёт и анализ ветеринарных приёмов.

В операционной системе каждый приём фиксируется в таблице `appointments`: какой питомец, какой ветеринар, дата, диагноз, статус (`scheduled` / `completed` / `cancelled`).

Для хранилища данных нас интересует не редактирование одной записи, а аналитика:

- сколько приёмов было за период;
- какие ветеринары загружены больше всего;
- по каким видам животных чаще обращаются;
- как меняется выручка по месяцам;
- какие статусы приёмов преобладают.

**Источник данных для DWH:** таблицы OLTP `appointments`, `pets`, `owners`, `veterinarians` (загрузка через ETL/ELT).

## 2. Grain (зернистость)

**Одна строка в таблице фактов = один ветеринарный приём** (одна запись из `appointments` в исходной системе).

Одна строка факта описывает один конкретный приём: питомец X у ветеринара Y в дату Z со статусом и стоимостью.

## 3. Таблицы измерений

### dim_date — «Когда?»

| Поле | Описание |
|------|----------|
| date_sk | PK (суррогатный) |
| source_date_id | исходная дата из OLTP |
| year, quarter, month, day | для группировок |
| day_of_week | для анализа по дням недели |

### dim_pet — «Кому? (питомец)»

| Поле | Описание |
|------|----------|
| pet_sk | PK |
| source_pet_id | pets.pet_id из OLTP |
| pet_name | pets.name |
| species | pets.species |
| birth_date | pets.birth_date |
| owner_full_name | owners.first_name + last_name |

### dim_veterinarian — «Кто лечил?»

| Поле | Описание |
|------|----------|
| veterinarian_sk | PK |
| source_vet_id | veterinarians.veterinarian_id |
| full_name | имя + фамилия |
| specialization | veterinarians.specialization |
| license_number | veterinarians.license_number |

### dim_appointment_status — «Контекст приёма?»

| Поле | Описание |
|------|----------|
| appointment_status_sk | PK |
| status_code | scheduled / completed / cancelled |
| status_description | текстовое описание |

## 4. Таблица фактов

**Имя:** `fact_appointments`

Таблица фактов хранит измеряемые показатели приёма и ссылки (FK) на измерения.

В OLTP (`appointments`) нет поля «стоимость» — в DWH оно появляется при трансформации (ETL) как бизнес-метрика для аналитики.

| Поле | Тип | Роль | Откуда в OLTP |
|------|-----|------|----------------|
| appointment_sk | SERIAL | PK (суррогатный ключ DWH) | новый ключ в DWH |
| date_sk | INT FK | когда был приём | appointments.appointment_date |
| pet_sk | INT FK | какой питомец | appointments.pet_id → pets |
| veterinarian_sk | INT FK | какой ветеринар | appointments.veterinarian_id |
| appointment_status_sk | INT FK | контекст приёма (статус) | appointments.status |
| service_cost | DECIMAL | метрика: выручка за приём | ETL / расчёт |
| visit_duration_minutes | INT | метрика: длительность | ETL / расчёт |

## 5. Суррогатные ключи и source_id

| OLTP | DWH |
|------|-----|
| appointments | fact_appointments |
| appointment_date | dim_date |
| pets + owners | dim_pet (+ dim_owner в snowflake) |
| veterinarians | dim_veterinarian |
| appointments.status | dim_appointment_status |

## 6. Выбор схемы моделирования

Выбрана **Star Schema**. Таблица фактов `fact_appointments` связана напрямую с четырьмя измерениями. Данные владельца (`owner_full_name`) включены в `dim_pet` для упрощения аналитических запросов.

## 7. Пример аналитических вопросов

1. Сколько приёмов было по каждому статусу?
2. Какая выручка по месяцам?
3. Кто из ветеринаров провёл больше всего приёмов?
4. Средняя стоимость приёма по видам животных (species)?
5. В какие дни недели больше всего завершённых приёмов?