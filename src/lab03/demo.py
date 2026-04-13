# -*- coding: utf-8 -*-
import sys
from pathlib import Path

current_dir = Path(__file__).parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

# 关键修复：全部统一用 lab01 里的真正 Student
from lab01.model import Student
from lab02.collection import StudentCollection
from models import BachelorStudent, MasterStudent, PhDStudent

def main():
    print("=== Лабораторная работа №3: Наследование и иерархия классов ===")
    print("\n=== 1. Создание объектов разных типов ===")
    
    bach1 = BachelorStudent("Иванов И.И.", "БИВТ-25-8", 95, 90, 3, True)
    bach2 = BachelorStudent("Петрова П.П.", "БИВТ-25-8", 78, 82, 2, True)
    mast1 = MasterStudent("Сидоров С.С.", "БИВТ-24-1", 88, 92, "Иванов И.И.", "Искусственный интеллект")
    phd1 = PhDStudent("Кузнецов А.В.", "БИВТ-23-1", 85, 88, "Кафедра ИТ", "Машинное обучение")

    print("\n=== 2. Вывод объектов ===")
    print("--- Бакалавр Иванов ---")
    print(bach1)
    print("\n--- Магистрант Сидоров ---")
    print(mast1)
    print("\n--- Аспирант Кузнецов ---")
    print(phd1)

    print("\n=== 3. Вызов новых методов дочерних классов ===")
    print(f"Стипендия Иванова: {bach1.get_scholarship_amount()} руб.")
    print(f"Проект Сидорова: {mast1.get_project_details()}")
    print(f"Диссертация Кузнецова: {phd1.get_dissertation_progress()}")

    print("\n=== 4. Проверка типов через isinstance() ===")
    print(f"Иванов является Student? {isinstance(bach1, Student)}")
    print(f"Иванов является BachelorStudent? {isinstance(bach1, BachelorStudent)}")
    print(f"Иванов является MasterStudent? {isinstance(bach1, MasterStudent)}")
    print(f"Сидоров является Student? {isinstance(mast1, Student)}")

    print("\n=== 5. Полиморфное поведение: вызов get_rating() ===")
    students = [bach1, bach2, mast1, phd1]
    for s in students:
        print(f"{s.name} ({s.get_student_type()}): {s.get_rating()}")

    print("\n=== 6. Интеграция с коллекцией из ЛР-2 ===")
    group = StudentCollection()
    group.add(bach1)
    group.add(bach2)
    group.add(mast1)
    group.add(phd1)
    print(f"Количество студентов в коллекции: {len(group)}")

    print("\n=== 7. Фильтрация по типу студентов ===")
    bachelors = [s for s in group if isinstance(s, BachelorStudent)]
    print(f"Бакалавры в коллекции ({len(bachelors)} чел.):")
    for s in bachelors:
        print(f"- {s.name}")

    masters = [s for s in group if isinstance(s, MasterStudent)]
    print(f"\nМагистранты в коллекции ({len(masters)} чел.):")
    for s in masters:
        print(f"- {s.name}")

    print("\n=== 8. Унифицированный вызов метода get_student_type() ===")
    for s in group:
        print(f"{s.name}: {s.get_student_type()}")

if __name__ == "__main__":
    main()