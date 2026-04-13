# -*- coding: utf-8 -*-
class Student:
    # 类属性
    MIN_GRADE = 0  # 最低分数
    MAX_GRADE = 100  # 最高分数

    def __init__(self, name, group, exam_grade, hw_grade):
        # 私有属性
        self._name = name
        self._group = group
        # 通过setter初始化，自动触发数据校验
        self.exam_grade = exam_grade
        self.hw_grade = hw_grade

    # @property只读访问器
    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @property
    def exam_grade(self):
        return self._exam_grade

    # 带校验的setter
    @exam_grade.setter
    def exam_grade(self, value):
        # 类型校验：必须是数字
        if not isinstance(value, (int, float)):
            raise TypeError("Экзаменационные оценки должны быть числами.")
        # 范围校验：0到100
        if not (self.MIN_GRADE <= value <= self.MAX_GRADE):
            raise ValueError(f"Экзаменационная оценка должна быть в пределах от {self.MIN_GRADE} до {self.MAX_GRADE}.")
        self._exam_grade = value

    @property
    def hw_grade(self):
        return self._hw_grade

    @hw_grade.setter
    def hw_grade(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Домашнее задание оценивается цифрами.")
        if not (self.MIN_GRADE <= value <= self.MAX_GRADE):
            raise ValueError(f"Оценка за домашнее задание должна быть в пределах от {self.MIN_GRADE} до {self.MAX_GRADE}.")
        self._hw_grade = value

    # 核心业务方法1：计算最终平均分
    def get_final_grade(self):
        """Рассчитывает средний балл по экзаменам и домашним заданиям."""
        return (self._exam_grade + self._hw_grade) / 2

    # 核心业务方法2：根据平均分返回等级描述
    def get_rating(self):
        """Возвращает оценку качества («Отлично»/«Хорошо»/«Удовлетворительно»/«Неудовлетворительно»)"""
        final = self.get_final_grade()
        if final >= 90:
            return "Отлично"
        elif final >= 75:
            return "Хорошо"
        elif final >= 60:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    # 判断是否优秀
    def is_excellent(self):
        """Проверяет, является ли ученик отличным учеником (средний балл >= 90)."""
        return self.get_final_grade() >= 90

    # 魔法方法1：用户友好的字符串输出
    def __str__(self):
        """Отображает удобную информацию о студенте."""
        final = self.get_final_grade()
        return (f"Имя: {self._name}\n"
                f"Группа: {self._group}\n"
                f"Экзамены: {self._exam_grade}, ДЗ: {self._hw_grade}\n"
                f"Итоговый балл: {final:.1f} - {self.get_rating()}")

    # 魔法方法2：官方调试用字符串表示
    def __repr__(self):
        """Используется для официального отображения объекта при отладке."""
        return f"Student('{self._name}', '{self._group}', {self._exam_grade}, {self._hw_grade})"

    # 魔法方法3：对象比较逻辑
    def __eq__(self, other):
        """Проверяет равенство двух учеников по имени, группе и оценкам."""
        if not isinstance(other, Student):
            return False
        return (self._name == other._name and
                self._group == other._group and
                self._exam_grade == other._exam_grade and
                self._hw_grade == other._hw_grade)