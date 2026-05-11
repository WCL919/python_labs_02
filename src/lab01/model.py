# -*- coding: utf-8 -*-
from typing import List, Optional


class Student:
    def __init__(self, name: str, group: str, grades: List[int]) -> None:
        self.name: str = name
        self.group: str = group
        self.grades: List[int] = grades

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades)

    def is_excellent(self) -> bool:
        return all(g >= 85 for g in self.grades)

    def get_final_grade(self) -> float:
        return self.get_average()

    def __str__(self) -> str:
        return f"Студент {self.name}, группа {self.group}, средний балл {self.get_average():.2f}"

    def __repr__(self) -> str:
        return f"Student({self.name!r}, {self.group!r}, {self.grades!r})"


class BachelorStudent(Student):
    def __init__(self, name: str, group: str, grades: List[int], scholarship: float) -> None:
        super().__init__(name, group, grades)
        self.scholarship: float = scholarship

    def get_scholarship(self) -> float:
        return self.scholarship

    def __str__(self) -> str:
        return (f"Бакалавр {self.name}, группа {self.group}, "
                f"стипендия {self.scholarship:.2f}, средний балл {self.get_average():.2f}")


class MagisterStudent(Student):
    def __init__(self, name: str, group: str, grades: List[int], theme: str) -> None:
        super().__init__(name, group, grades)
        self.theme: str = theme

    def get_theme(self) -> str:
        return self.theme

    def __str__(self) -> str:
        return (f"Магистрант {self.name}, группа {self.group}, "
                f"тема работы: {self.theme}, средний балл {self.get_average():.2f}")