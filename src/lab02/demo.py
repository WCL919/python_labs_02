from model import Student
from collection import StudentCollection

def main():
    # 1. 创建学生对象
    s1 = Student("Иванов И.И.", "БИВТ-25-8", 95, 90)
    s2 = Student("Петрова П.П.", "БИВТ-25-8", 70, 80)
    s3 = Student("Сидоров С.С.", "БИВТ-25-8", 50, 55)
    s4 = Student("Кузнецов А.В.", "БИВТ-25-9", 88, 92)

    # 2. 创建学生集合
    group = StudentCollection()
    print("=== Создана пустая коллекция ===")
    print(group)
    print(f"Количество студентов: {len(group)}")

    # 3. 向集合中添加学生（3级要求）
    print("\n=== Добавление студентов ===")
    group.add(s1)
    group.add(s2)
    group.add(s3)
    group.add(s4)
    print(f"Количество студентов после добавления: {len(group)}")
    print("\nВсе студенты в коллекции:")
    # 测试迭代功能 __iter__（4级要求）
    for student in group:
        print(student)
        print("-" * 40)

    # 4. 测试查找功能（4级要求）
    print("\n=== Тест поиска студентов ===")
    # 按姓名查找
    found = group.find_by_name("Иванов И.И.")
    print("Поиск по имени 'Иванов И.И.':")
    for s in found:
        print(s)
    # 按班级查找
    found_group = group.find_by_group("БИВТ-25-8")
    print(f"\nСтуденты группы БИВТ-25-8 ({len(found_group)} чел.):")
    for s in found_group:
        print(s.name)
    # 查找优秀学生
    excellent = group.find_by_min_grade(90)
    print(f"\nОтличники (средний балл ≥ 90): {[s.name for s in excellent]}")

    # 5. 测试删除学生（3级要求）
    print("\n=== Тест удаления студента ===")
    group.remove(s3)
    print(f"Количество студентов после удаления Сидорова: {len(group)}")
    print("\nОставшиеся студенты:")
    for s in group.get_all():
        print(s.name)

    # 6. 测试索引访问（5级要求）
    print("\n=== Тест индексации ===")
    print(f"Первый студент в коллекции: {group[0].name}")
    print(f"Второй студент в коллекции: {group[1].name}")

    # 7. 测试按索引删除（5级要求）
    print("\n=== Тест удаления по индексу ===")
    removed = group.remove_at(1)
    print(f"Удален студент по индексу 1: {removed.name}")
    print(f"Количество студентов: {len(group)}")

    # 8. 测试排序功能（5级要求）
    print("\n=== Тест сортировки по имени ===")
    group.sort_by_name()
    print("Студенты после сортировки по имени:")
    for s in group:
        print(s.name)

    print("\n=== Тест сортировки по итоговому баллу (от высокого к низкому) ===")
    group.sort_by_final_grade()
    for s in group:
        print(f"{s.name}: {s.get_final_grade():.1f}")

    # 9. 测试合法性校验（类型检查、重复检查）
    print("\n=== Тест ограничений ===")
    # 尝试添加非Student对象
    try:
        group.add("Не студент")
    except TypeError as e:
        print(f"Ошибка при добавлении не Student: {e}")
    # 尝试添加重复学生
    try:
        group.add(s1)
    except ValueError as e:
        print(f"Ошибка при добавлении дубликата: {e}")

    # 10. 测试集合相关操作（5级要求）
    print("\n=== Тест коллекционных операций ===")
    excellent_all = group.get_excellent_students()
    print(f"Отличники в коллекции: {[s.name for s in excellent_all]}")

if __name__ == "__main__":
    main()