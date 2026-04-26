# -*- coding: utf-8 -*-
from lab01.model import Student
from interfaces import Printable, Comparable, Exportable

# 本科生 —— 实现 3 个接口
class BachelorStudent(Student, Printable, Comparable, Exportable):
    def __init__(self, name, group, exam_grade, hw_grade, course, scholarship):
        super().__init__(name, group, exam_grade, hw_grade)
        self._course = course
        self._scholarship = scholarship

    @property
    def course(self):
        return self._course

    @property
    def scholarship(self):
        return self._scholarship

    def get_scholarship_amount(self):
        if not self._scholarship:
            return 0
        final = self.get_final_grade()
        if final >= 95:
            return 3000
        elif final >= 90:
            return 2000
        else:
            return 1500

    # 实现 Printable
    def to_string(self) -> str:
        return f"Бакалавр: {self.name}, курс {self.course}, балл: {self.get_final_grade()}"

    # 实现 Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, Student):
            raise TypeError("Сравнение только со Student")
        return int(self.get_final_grade() - other.get_final_grade())

    # 实现 Exportable
    def export_info(self) -> dict:
        return {
            "type": "Бакалавр",
            "name": self.name,
            "group": self.group,
            "final_grade": self.get_final_grade()
        }

    def __str__(self):
        return super().__str__() + f"\nТип: Бакалавр, Курс: {self._course}"

# 研究生 —— 实现 3 个接口
class MasterStudent(Student, Printable, Comparable, Exportable):
    def __init__(self, name, group, exam_grade, hw_grade, supervisor, project_topic):
        super().__init__(name, group, exam_grade, hw_grade)
        self._supervisor = supervisor
        self._project_topic = project_topic

    @property
    def supervisor(self):
        return self._supervisor

    @property
    def project_topic(self):
        return self._project_topic

    def get_project_details(self):
        return f"Проект: {self._project_topic}, руководитель: {self._supervisor}"

    # 实现 Printable
    def to_string(self) -> str:
        return f"Магистрант: {self.name}, руководитель: {self.supervisor}"

    # 实现 Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, Student):
            raise TypeError("Сравнение только со Student")
        return int(self.get_final_grade() - other.get_final_grade())

    # 实现 Exportable
    def export_info(self) -> dict:
        return {
            "type": "Магистрант",
            "name": self.name,
            "group": self.group,
            "final_grade": self.get_final_grade()
        }

    def __str__(self):
        return super().__str__() + f"\nТип: Магистрант"

# 博士生 —— 实现 3 个接口
class PhDStudent(Student, Printable, Comparable, Exportable):
    def __init__(self, name, group, exam_grade, hw_grade, department, dissertation_topic):
        super().__init__(name, group, exam_grade, hw_grade)
        self._department = department
        self._dissertation_topic = dissertation_topic

    @property
    def department(self):
        return self._department

    @property
    def dissertation_topic(self):
        return self._dissertation_topic

    # 实现 Printable
    def to_string(self) -> str:
        return f"Аспирант: {self.name}, кафедра: {self.department}"

    # 实现 Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, Student):
            raise TypeError("Сравнение только со Student")
        return int(self.get_final_grade() - other.get_final_grade())

    # 实现 Exportable
    def export_info(self) -> dict:
        return {
            "type": "Аспирант",
            "name": self.name,
            "department": self.department
        }

    def __str__(self):
        return super().__str__() + f"\nТип: Аспирант"