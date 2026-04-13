# -*- coding: utf-8 -*-
# ================= 修复导入问题 =================
import sys
from pathlib import Path

# 获取当前文件所在目录 (src/lib/lab02)
current_dir = Path(__file__).parent
# 获取项目根目录 (src/lib)
root_dir = current_dir.parent
# 将根目录添加到系统路径，让Python能找到lab01的文件
sys.path.append(str(root_dir))

# 现在用绝对路径导入，100%成功，再也不会报错
from lab01.model import Student
# =================================================
class StudentCollection:
    """
    Контейнерный класс для управления коллекцией студентов
    """
    def __init__(self):
        # 3级要求：内部用列表存储学生对象
        self._items = []

    # 3级要求：添加学生（带类型校验+去重）
    def add(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError("Можно добавлять только объекты класса Student")
        # 4级要求：禁止添加重复学生
        if student in self._items:
            raise ValueError("Этот студент уже существует в коллекции")
        self._items.append(student)

    # 3级要求：删除学生
    def remove(self, student: Student) -> None:
        if student not in self._items:
            raise ValueError("Студент не найден в коллекции")
        self._items.remove(student)

    # 3级要求：获取所有学生
    def get_all(self) -> list[Student]:
        return self._items.copy()  # 返回副本，防止外部修改内部列表

    # 4级要求：按姓名查找学生
    def find_by_name(self, name: str) -> list[Student]:
        return [s for s in self._items if s.name == name]

    # 4级要求：按班级查找学生
    def find_by_group(self, group: str) -> list[Student]:
        return [s for s in self._items if s.group == group]

    # 4级要求：按最终成绩查找（找所有优秀学生）
    def find_by_min_grade(self, min_grade: float) -> list[Student]:
        return [s for s in self._items if s.get_final_grade() >= min_grade]

    # 4级要求：实现__len__，支持len(collection)
    def __len__(self) -> int:
        return len(self._items)

    # 4级要求：实现__iter__，支持for循环遍历
    def __iter__(self):
        return iter(self._items)

    # 5级要求：实现__getitem__，支持索引访问 collection[0]
    def __getitem__(self, index: int) -> Student:
        return self._items[index]

    # 5级要求：按索引删除学生
    def remove_at(self, index: int) -> Student:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    # 5级要求：按姓名排序
    def sort_by_name(self) -> None:
        self._items.sort(key=lambda s: s.name)

    # 5级要求：按最终成绩排序（从高到低）
    def sort_by_final_grade(self, reverse: bool = True) -> None:
        self._items.sort(key=lambda s: s.get_final_grade(), reverse=reverse)

    # 5级要求：集合运算：获取所有优秀学生
    def get_excellent_students(self) -> list[Student]:
        return [s for s in self._items if s.is_excellent()]

    # 5级要求：集合运算：获取指定班级所有学生
    def get_students_by_group(self, group: str) -> list[Student]:
        return self.find_by_group(group)

    # 魔法方法：打印集合信息
    def __str__(self):
        return f"StudentCollection(количество студентов: {len(self)})"

    def __repr__(self):
        return f"StudentCollection({self._items})"