# Homework 7, Task 1: User record normalization

# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# Разбиваем строку на отдельные элементы по разделителю ";"
raw_elements = raw_user_record.split(";")

# Очищаем каждый элемент от лишних пробелов по краям
cleaned_elements = [item.strip() for item in raw_elements]

# Распаковываем очищенные элементы по переменным
uid_raw, name_raw, city_raw, status_raw = cleaned_elements

# Применяем префикс "UID-" с помощью f-строки
uid = f"UID-{uid_raw}"

#  Преобразуем имя (заменяем "_" на пробел и делаем каждое слово с заглавной буквы)
name = name_raw.replace("_", " ").title()

# Приводим название города к верхнему регистру
city = city_raw.upper()

# Приводим статус пользователя к нижнему регистру
status = status_raw.lower()

#  Объединяем обработанные элементы в строку с разделителем |
result = " | ".join([uid, name, city, status])

# Выводим результат на экран
print(f"Нормализованная запись: {result}")