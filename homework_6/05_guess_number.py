# Homework 6, Task 5: Guess the number

from random import randint

secret_number = randint(1, 20)
attempts = 5

print(f"Я загадал число от 1 до 20, у тебя есть {attempts} попыток, чтобы отгадать")

while attempts > 0:
    guess = int(input(f"Попытка {6 - attempts}. Введи своё число: "))

    if guess == secret_number:
        print("Ты угадал! Отличная работа!")
        break
    elif guess > secret_number:
        print("Слишком много!")
    else:
        print("Слишком мало!")

    attempts -= 1
    print(f"Осталось {attempts} попыток.")

