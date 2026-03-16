from model import Student

def main():
    # 1. 创建合法的学生对象
    s1 = Student("Иванов И.И.", "БИВТ-25-8", 95, 90)
    s2 = Student("Петрова П.П.", "БИВТ-25-8", 70, 80)
    s3 = Student("Сидоров С.С.", "БИВТ-25-8", 50, 55)

    # 2. 打印学生信息（自动调用__str__方法）
    print(s1)
    print("-" * 40)
    print(s2)
    print("-" * 40)
    print(s3)
    print("-" * 40)

    # 3. 测试通过setter修改成绩
    print("\n=== Тест изменения оценки через setter ===")  #  
    try:
        # 合法修改成绩
        s1.exam_grade = 98
        print(f"Измененная оценка Иванова И.И. за экзамен: {s1.exam_grade}")  #  
        print(s1)
        # 非法修改（超出范围，触发异常）
        s1.exam_grade = 150
    except (ValueError, TypeError) as e:
        print(f"Ошибка поймана: {e}")  

    # 4. 测试对象比较
    print("\n=== Тест сравнения объектов ===")  
    s4 = Student("Иванов И.И.", "ИКБО-23-23", 98, 90)
    print(f"s1 и s4 равны? {s1 == s4}")  
    print(f"s2 и s3 равны? {s2 == s3}")  

    # 5. 测试新增业务方法is_excellent
    print("\n=== Тест проверки на отличника ===")  
    print(f"{s1.name} - отличник? {s1.is_excellent()}")  
    print(f"{s3.name} - отличник? {s3.is_excellent()}")  

    # 6. 访问类属性
    print("\n=== Доступ к атрибутам класса ===")  
    print(f"Минимальная оценка: {Student.MIN_GRADE}")  
    print(f"Максимальная оценка: {Student.MAX_GRADE}")  

    # 7. 测试非法创建对象（try/except异常处理）
    print("\n=== Тест некорректного создания объекта студента ===")  
    try:
        # 传入字符串类型成绩，触发类型错误
        bad_student = Student("Ошибка", "ИКБО-99-99", "не число", 80)
    except TypeError as e:
        print(f"Ошибка : {e}")

if __name__ == "__main__":
    main()