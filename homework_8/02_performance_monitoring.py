# Homework 8, Task 2: Analytics performance monitoring

import time
from typing import Any, Callable

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable) -> Callable:
    """Декоратор для замера времени выполнения и логирования вызова функции.

    Args:
        func (Callable): Целевая функция, время выполнения которой нужно замерить.

    Returns:
        Callable: Обёрнутая функция с автоматическим логированием времени работы.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time
        print(
            f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' "
            f"выполнена за {execution_time:.{TIME_DECIMALS}f} сек."
        )
        return result

    return wrapper


@performance_logger
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """Сортирует список категорий по убыванию выручки.

    Args:
        data (list[dict[str, str | float]]): Список словарей с данными по категориям и выручке.

    Returns:
        list[dict[str, str | float]]: Отсортированный по убыванию total_sales список словарей.
    """
    return sorted(data, key=lambda item: item["total_sales"], reverse=True)


# Тестирование декоратора и функции
if __name__ == "__main__":
    test_data_1 = [
        {"category": "Action", "total_sales": 4311.85},
        {"category": "Animation", "total_sales": 4656.30},
        {"category": "Children", "total_sales": 3655.55},
    ]

    test_data_2 = [
        {"category": "Classics", "total_sales": 1200.10},
        {"category": "Comedy", "total_sales": 4000.00},
        {"category": "Documentary", "total_sales": 4000.00},
    ]

    test_data_3 = [
        {"category": "Drama", "total_sales": 500.00},
    ]

    tests = [test_data_1, test_data_2, test_data_3]

    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
    for idx, test in enumerate(tests, start=1):
        print(f"--- ТЕСТ {idx} ---")
        report = get_sorted_report(test)
        print("Топ категорий по выручке:")
        for item_idx, item in enumerate(report, start=1):
            print(f"  {item_idx}. {item['category']}: {item['total_sales']}")