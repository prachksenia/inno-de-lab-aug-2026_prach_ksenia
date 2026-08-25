# Homework 6, Task 6 (Optional): Simple calculator

first_number = float(input("Введите первое число: "))
second_number = float(input("Введите Второе число: "))
operation = input("Выберите операцию (+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        print("Ошибка: такая операция невозможна")
        result = None
    else:
        result = first_number / second_number
else:
    print("Ошибка: неизвестная операция")
    result = None
if result is not None:
    print(f"Результат: {result}")