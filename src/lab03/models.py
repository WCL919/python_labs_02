# -*- coding: utf-8 -*-
from lab01.model import Student

# 子类1：本科生 BachelorStudent
class BachelorStudent(Student):
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

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Тип: Бакалавр\n"
                f"Курс: {self._course}\n"
                f"Стипендия: {'Есть' if self._scholarship else 'Нет'}\n"
                f"Размер стипендии: {self.get_scholarship_amount()} руб.")

    def get_rating(self):
        final = self.get_final_grade()
        if final >= 90:
            return "Отлично (бакалавр)"
        elif final >= 75:
            return "Хорошо (бакалавр)"
        elif final >= 60:
            return "Удовлетворительно (бакалавр)"
        else:
            return "Неудовлетворительно (бакалавр)"

    def get_student_type(self):
        return "Бакалавр"

# 子类2：研究生 MasterStudent
class MasterStudent(Student):
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
        return f"Тема проекта: {self._project_topic}, Научный руководитель: {self._supervisor}"

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Тип: Магистрант\n"
                f"Научный руководитель: {self._supervisor}\n"
                f"Тема проекта: {self._project_topic}")

    def get_rating(self):
        final = self.get_final_grade()
        if final >= 85:
            return "Отлично (магистрант)"
        elif final >= 70:
            return "Хорошо (магистрант)"
        elif final >= 60:
            return "Удовлетворительно (магистрант)"
        else:
            return "Неудовлетворительно (магистрант)"

    def get_student_type(self):
        return "Магистрант"

# 子类3：博士生 PhDStudent
class PhDStudent(Student):
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

    def get_dissertation_progress(self):
        return f"Диссертация: {self._dissertation_topic}, Кафедра: {self._department}, Статус: В процессе"

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Тип: Аспирант\n"
                f"Кафедра: {self._department}\n"
                f"Тема диссертации: {self._dissertation_topic}")

    def get_rating(self):
        final = self.get_final_grade()
        if final >= 80:
            return "Отлично (аспирант)"
        elif final >= 70:
            return "Хорошо (аспирант)"
        else:
            return "Удовлетворительно (аспирант)"

    def get_student_type(self):
        return "Аспирант"