# Homework 8, Task 1: Wholesale movie rental calculation

MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(
    quantity: int, rental_rate: float, discount: float = 0.0
) -> tuple[float, bool]:
    """Рассчитывает стоимость партии аренды и проверяет превышение лимита.

    Args:
        quantity (int): Количество дисков в партии.
        rental_rate (float): Стоимость аренды одного диска.
        discount (float, optional): Размер скидки (например, 0.10 для 10%). По умолчанию 0.0.

    Returns:
        tuple[float, bool]: Кортеж из двух элементов:
            - final_sum (float): Итоговая стоимость партии с округлением до 2 знаков.
            - is_limit_exceeded (bool): Флаг превышения лимита MAX_RENTAL_BATCH_LIMIT.
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded


# Тестирование функции
if __name__ == "__main__":
    batches = [
        ("Academy Dinosaur", 30, 2.99, 0.0),
        ("Affair Prejudice", 40, 4.99, 0.10),
        ("Agent Truman", 10, 1.99, 0.0),
        ("African Egg", 50, 3.50, 0.20),
    ]

    print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

    # Демонстрация вызова с позиционными аргументами
    title, q, r, d = batches[0]
    total, exceeded = calculate_rental_batch(q, r, d)
    print(f"Партия 1 ({title}): Сумма {total}$. Превышение лимита: {exceeded}")

    # Демонстрация вызова с именованными аргументами
    for idx, (title, q, r, d) in enumerate(batches[1:], start=2):
        total, exceeded = calculate_rental_batch(
            quantity=q, rental_rate=r, discount=d
        )
        print(f"Партия {idx} ({title}): Сумма {total}$. Превышение лимита: {exceeded}")