import random
from statistics import mean
from typing import List

from task3 import GreetMan


class StudentMan(GreetMan):
    def __init__(self, first_name: str, last_name: str, age: int, grades: List[float] = []) -> None:
        super().__init__(first_name, last_name, age)
        self.grades = grades

    def __str__(self) -> str:
        return f'Имя: {self.first_name}, Фамилия: {self.last_name}, Возраст: {self.age}, Средний балл: {self.get_mean_grade()}'

    def get_mean_grade(self) -> float:
        if len(self.grades) == 0:
            return 0
        return mean(self.grades)


if __name__ == "__main__":
    # Задание 4
    N_STUDENTS = 4
    N_GRADES = 10
    AVAILABLE_GRADES = [2, 3, 4, 5]
    RANDOM_GRADES = [[random.sample(AVAILABLE_GRADES, 1)[0]
                      for _ in range(N_GRADES)] for _ in range(N_STUDENTS)]
    students = [StudentMan(f'Name_{idx}', f'Last_Name_{idx}', idx, grades)
                for idx, grades in enumerate(RANDOM_GRADES)]
    # Задание 5
    sorted_students = sorted(
        students, key=lambda student: student.get_mean_grade(), reverse=True)

    for student in sorted_students:
        print(student)
