import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from lab03.models import BachelorStudent, MasterStudent, PhDStudent
from lab05.collection import StudentCollection
from lab05.strategies import *

# 4分要求：工厂函数，生成带参数的过滤函数
def make_min_grade_filter(min_grade):
    """工厂函数：生成一个过滤函数，筛选平均分≥min_grade的学生"""
    def filter_func(student):
        return student.get_final_grade() >= min_grade
    return filter_func

def main():
    print("=== Лабораторная работа №5: Функции как аргументы, стратегии и делегаты ===")

    # 1. 创建学生集合
    group = StudentCollection()
    group.add(BachelorStudent("Иванов", "БИВТ-25-8", 95, 90, 3, True))
    group.add(MasterStudent("Сидоров", "БИВТ-24-1", 88, 92, "Иванов", "ИИ"))
    group.add(PhDStudent("Кузнецов", "БИВТ-23-1", 85, 88, "ИТ", "МО"))
    group.add(BachelorStudent("Петрова", "БИВТ-25-8", 78, 82, 2, True))
    print("Исходный список студентов:")
    for s in group.get_all():
        print(f"- {s.name}, балл: {s.get_final_grade()}")

    # ===================== 3分：排序策略 =====================
    print("\n=== 3 балла: Сортировка по разным стратегиям ===")
    # 按姓名排序
    group.sort_by(sort_by_name)
    print("\nСортировка по имени:")
    for s in group.get_all():
        print(f"- {s.name}")

    # 按平均分降序排序
    group.sort_by(sort_by_final_grade, reverse=True)
    print("\nСортировка по баллу (убывание):")
    for s in group.get_all():
        print(f"- {s.name}, балл: {s.get_final_grade()}")

    # 按学生类型排序
    group.sort_by(sort_by_type)
    print("\nСортировка по типу студента:")
    for s in group.get_all():
        print(f"- {s.name} ({type(s).__name__})")

    # ===================== 3分：过滤策略 =====================
    print("\n=== 3 балла: Фильтрация по разным стратегиям ===")
    # 筛选优秀学生
    excellent = group.filter_by(filter_excellent)
    print(f"Отличники ({len(excellent)} чел.):")
    for s in excellent:
        print(f"- {s.name}")

    # 筛选本科生
    bachelors = group.filter_by(filter_bachelor)
    print(f"\nБакалавры ({len(bachelors)} чел.):")
    for s in bachelors:
        print(f"- {s.name}")

    # ===================== 4分：map和工厂函数 =====================
    print("\n=== 4 балла: Использование map и фабрики функций ===")
    # map：把学生转成姓名列表
    names = group.apply(map_to_name)
    print("Имена всех студентов:", names)

    # 工厂函数：生成平均分≥85的过滤条件
    filter_85 = make_min_grade_filter(85)
    students_85 = group.filter_by(filter_85)
    print(f"Студенты с баллом ≥85 ({len(students_85)} чел.):")
    for s in students_85:
        print(f"- {s.name}, балл: {s.get_final_grade()}")

    # ===================== 5分：链式操作 =====================
    print("\n=== 5 баллов: Цепочка операций (filter → sort → map) ===")
    # 1. 筛选优秀学生 → 2. 按姓名排序 → 3. 只保留姓名
    result = group.filter_by(filter_excellent)
    result.sort(key=sort_by_name)
    result_names = [map_to_name(s) for s in result]
    print("Цепочка filter→sort→map результат:", result_names)

if __name__ == "__main__":
    main()