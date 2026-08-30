# Homework 8, Task 3: Safe return processing with try-except-finally

from typing import Any, Optional, Tuple

DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
        film_title: str, days_overdue: Any, fine_rate: float
) -> Optional[Tuple[float, float]]:
    """Безопасно рассчитывает штраф за просрочку и индекс оборачиваемости.

    Обрабатывает типы ошибок:
        - TypeError: переданы некорректные типы данных (например, список или словарь).
        - ValueError: строку не удалось преобразовать в вещественное число.
        - ZeroDivisionError: просрочка равна 0, деление на ноль невозможно.

    Args:
        film_title (str): Название фильма.
        days_overdue (Any): Количество дней просрочки (сырые данные любого типа).
        fine_rate (float): Ставка штрафа за один день просрочки.

    Returns:
        Optional[Tuple[float, float]]: Кортеж (total_fine, return_index) в случае успеха,
            или None, если возникла ошибка.
    """
    try:
        numeric_days = float(days_overdue)
        if numeric_days == 0:
            raise ZeroDivisionError("float division by zero")

        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{film_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_title}': {e}")
        return None
    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Некоректная строка с днями просрочки для '{film_title}': {e}")
        return None
    except ZeroDivisionError as e:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_title}': {e}")
        return None
    finally:
        print("Проверка транзакции возврата завершена")


# Тестирование обработки ошибок
if __name__ == "__main__":
    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
    test_cases = [
        ("Matrix", 5, 1.5),
        ("Inception", "пять", 2.0),
        ("Avatar", 0, 2.5),
        ("Interstellar", [3], 3.0),
    ]

    for title, days, rate in test_cases:
        calculate_overdue_fine(title, days, rate)