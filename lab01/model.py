class Student:
    def __init__(self, name, group, exam_grade, hw_grade):
        self.name = name
        self.group = group
        self.exam_grade = exam_grade
        self.hw_grade = hw_grade

    def get_final_grade(self):
        return (self.exam_grade + self.hw_grade) / 2

    def get_rating(self):
        final = self.get_final_grade()
        if final >= 90:
            return "Отлично"
        elif final >= 75:
            return "Хорошо"
        elif final >= 60:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    def __str__(self):
        return (f"Студент: {self.name}, Группа: {self.group}\n"
                f"Экзамен: {self.exam_grade}, Д/з: {self.hw_grade}\n"
                f"Итог: {self.get_final_grade():.1f} — {self.get_rating()}")