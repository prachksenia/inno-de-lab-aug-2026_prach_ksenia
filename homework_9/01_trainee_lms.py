# Homework 9, Task 1: Trainee LMS module with encapsulation and validation


class Trainee:
    """Класс для отслеживания успеваемости стажера."""

    def __init__(
        self,
        name: str,
        surname: str,
        score: int = 0,
        passing_grade: int = 10,
    ) -> None:
        """Инициализирует объект стажера.

        Args:
            name (str): Имя стажера.
            surname (str): Фамилия стажера.
            score (int, optional): Начальный балл. По умолчанию 0.
            passing_grade (int, optional): Проходной балл. По умолчанию 10.
        """
        self.name: str = name
        self.surname: str = surname
        self.passing_grade: int = passing_grade
        self.score = score

    @property
    def score(self) -> int:
        """Возвращает текущий балл стажера.

        Returns:
            int: Текущее количество баллов.
        """
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """Устанавливает балл стажера с проверкой типа и значения.

        Args:
            value (int): Новое значение балла.

        Raises:
            ValueError: Если тип value не int или value < 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1."""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1."""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1."""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1."""
        self.score -= 1

    def is_passing(self) -> bool:
        """Проверяет, набрал ли стажер проходной балл.

        Returns:
            bool: True, если score >= passing_grade, иначе False.
        """
        return self.score >= self.passing_grade


# Тестирование класса Trainee
if __name__ == "__main__":
    print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

    # 1. Создание стажера
    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

    # 2. Выполнение ДЗ и проверка статуса
    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 3. Пропуск лекции и проверка статуса
    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # 4. Проверка валидации отрицательного значения
    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")