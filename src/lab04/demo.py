# -*- coding: utf-8 -*-
import sys
from pathlib import Path

current_dir = Path(__file__).parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from lab02.collection import StudentCollection
from models import BachelorStudent, MasterStudent, PhDStudent
from interfaces import Printable, Comparable, Exportable

def main():
    print("=== Лабораторная работа №4: Интерфейсы и абстрактные классы (5 баллов) ===")

    # 创建学生
    s1 = BachelorStudent("Иванов И.И.", "БИВТ-25-8", 95, 90, 3, True)
    s2 = MasterStudent("Сидоров С.С.", "БИВТ-24-1", 88, 92, "Иванов", "ИИ")
    s3 = PhDStudent("Кузнецов А.В.", "БИВТ-23-1", 85, 88, "ИТ", "МО")

    # 调用接口方法
    print("\n=== 3 балла: Вызов методов интерфейсов ===")
    print(s1.to_string())
    print(s2.to_string())
    print(s3.to_string())

    # 多态 + 通用函数
    print("\n=== 4 балла: Полиморфизм (общий метод) ===")
    def print_all(items: list[Printable]):
        for item in items:
            print(item.to_string())

    print_all([s1, s2, s3])

    # 集合 + 接口 + сравнение + экспорт
    print("\n=== 5 баллов: Коллекция + интерфейсы ===")
    col = StudentCollection()
    col.add(s1)
    col.add(s2)
    col.add(s3)

    # Сравнение
    print("\nСравнение баллов: s1 vs s2 =", s1.compare_to(s2))

    # Экспорт
    print("\nЭкспорт данных:")
    print(s1.export_info())
    print(s2.export_info())

    # Проверка интерфейсов
    print("\nПроверка реализации интерфейсов:")
    print("s1 is Printable:", isinstance(s1, Printable))
    print("s1 is Comparable:", isinstance(s1, Comparable))
    print("s1 is Exportable:", isinstance(s1, Exportable))

if __name__ == "__main__":
    main()