# Homework 9, Task 2: Advanced OOP with inheritance and polymorphism

import importlib
import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Импортируем класс Trainee из модуля с цифрой в названии
trainee_module = importlib.import_module("homework_9.01_trainee_lms")
Trainee = trainee_module.Trainee


class HardworkingTrainee(Trainee):
    """Стажер-трудоголик, получающий больше баллов за домашние задания."""

    def do_homework(self) -> None:
        """Increases score by 2."""
        self.score += 2


class AuditTrainee(Trainee):
    """Вольнослушатель, который всегда считается прошедшим курс."""

    def is_passing(self) -> bool:
        """Проверяет статус прохождения курса.

        Returns:
            bool: Всегда True для вольнослушателя.
        """
        return True


class Cohort:
    """Учебная группа для управления стажерами."""

    def __init__(self, title: str, trainees: list[Trainee] | None = None) -> None:
        """Инициализирует учебную группу.

        Args:
            title (str): Название группы.
            trainees (list[Trainee] | None, optional): Начальный список учащихся.
        """
        self.title: str = title
        self.trainees: list[Trainee] = trainees if trainees is not None else []

    def add_trainee(self, trainee: Trainee) -> None:
        """Добавляет учащегося в группу.

        Args:
            trainee (Trainee): Объект стажера.
        """
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Проводит лекцию для всех учащихся в группе."""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Возвращает список учащихся, успешно проходящих курс.

        Returns:
            list[Trainee]: Список прошедших курс стажеров.
        """
        return [trainee for trainee in self.trainees if trainee.is_passing()]


# Тестирование работы группы и наследования
if __name__ == "__main__":
    # 1. Создаем учащихся разных типов
    std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
    hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
    audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

    # 2. Создаем группу и добавляем студентов
    cohort = Cohort("Python Advanced")
    cohort.add_trainee(std_trainee)
    cohort.add_trainee(hard_trainee)
    cohort.add_trainee(audit_trainee)

    # 3. Проводим лекцию для всей группы
    cohort.conduct_lecture()

    # 4. ДЗ для трудоголика (+2 балла)
    hard_trainee.do_homework()

    # 5. Вывод результатов
    passing_students = cohort.get_passing_students()
    print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
    for student in cohort.trainees:
        print(
            f"{student.name} {student.surname} | "
            f"Баллы: {student.score} | Проходит: {student.is_passing()}"
        )

    print("\nУспешно зачислены на следующий модуль:")
    for student in passing_students:
        print(f"- {student.name} {student.surname}")