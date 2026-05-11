# -*- coding: utf-8 -*-
from container import TypedCollection, DisplayableCollection, Displayable

class Student(Displayable):
    def __init__(self, name: str, group: str, grades: list):
        self.name = name
        self.group = group
        self.grades = grades

    def get_final_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return all(g >= 85 for g in self.grades)

    def display(self):
        return f"Студент: {self.name}, группа: {self.group}, средний балл: {self.get_final_grade():.2f}"

    # 让打印对象时显示友好信息
    def __str__(self):
        return self.display()

    def __repr__(self):
        return self.display()

# ================= 运行测试 =================
if __name__ == "__main__":
    print("=== ЛР6 ===")

    # 3分演示：基础泛型集合
    print("\n--- 3 балла: Базовая работа TypedCollection ---")
    col = TypedCollection()
    col.add(Student("Иванов", "101", [90, 95, 88]))
    col.add(Student("Петров", "102", [85, 80, 92]))
    col.add(Student("Сидоров", "103", [50, 60, 70]))

    print("Все студенты:")
    for s in col.get_all():
        print(f"- {s}")

    print("\nПоиск по группе 101:")
    group_101 = col.find_by_group("101")
    for s in group_101:
        print(f"- {s}")

    # 4分演示：find / filter / map
    print("\n--- 4 балла: Методы find, filter, map ---")
    top_student = col.find(lambda s: s.get_final_grade() >= 90)
    print(f"Первый отличник: {top_student}")

    good_students = col.filter(lambda s: s.get_final_grade() >= 85)
    print(f"Студенты с баллом ≥85 ({len(good_students)} чел.):")
    for s in good_students:
        print(f"- {s}")

    student_names = col.map(lambda s: s.name)
    print("\nСписок имен студентов:", student_names)

    # 5分演示：Protocol
    print("\n--- 5 балла: Протокол и DisplayableCollection ---")
    d_col = DisplayableCollection()
    d_col.add(Student("Сидоров", "103", [50,60,70]))
    d_col.add(Student("Иванов", "101", [90,95,88]))
    print("Вывод через display_all():")
    d_col.display_all()

    print("\n=== УСПЕШНО! ===")