# -*- coding: utf-8 -*-
# 导入类型工具：泛型、类型变量、列表、可选值、函数类型、协议
from typing import Generic, TypeVar, List, Optional, Callable, Protocol

# -------------------------- 泛型类型定义 --------------------------
# T 代表任意类型（用于泛型集合）
T = TypeVar('T')
# R 代表转换后的类型（用于 map 方法）
R = TypeVar('R')
# D 代表满足 Displayable 协议的类型（用于限制泛型范围）
D = TypeVar('D', bound='Displayable')

# -------------------------- 协议定义（5分要求） --------------------------
# 可显示协议：只要类实现了 display() 方法，就自动满足这个协议
class Displayable(Protocol):
    def display(self) -> str: ...

# -------------------------- 泛型集合类（核心） --------------------------
# 通用泛型集合，移植了 ЛР2 所有方法 + 完整类型注解
class TypedCollection(Generic[T]):
    # 初始化空列表存储元素
    def __init__(self) -> None:
        self._items: List[T] = []

    # 添加元素：禁止重复
    def add(self, item: T) -> None:
        if item in self._items:
            raise ValueError("Элемент уже существует")  # 元素已存在
        self._items.append(item)

    # 删除指定元素
    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Элемент не найден")  # 元素不存在
        self._items.remove(item)

    # 获取所有元素（返回副本，防止外部修改）
    def get_all(self) -> List[T]:
        return self._items.copy()

    # 清空集合
    def clear(self) -> None:
        self._items.clear()

    # -------------------------- 从 ЛР2 移植的方法 --------------------------
    # 按名字查找（要求对象有 name 属性）
    def find_by_name(self, name: str) -> List[T]:
        return [i for i in self._items if hasattr(i, 'name') and i.name == name]

    # 按班级查找
    def find_by_group(self, group: str) -> List[T]:
        return [i for i in self._items if hasattr(i, 'group') and i.group == group]

    # 按最低平均分查找
    def find_by_min_grade(self, min_grade: float) -> List[T]:
        return [i for i in self._items if hasattr(i, 'get_final_grade') and i.get_final_grade() >= min_grade]

    # 获取集合长度（支持 len()）
    def __len__(self) -> int:
        return len(self._items)

    # 支持迭代遍历（for ... in ...）
    def __iter__(self):
        return iter(self._items)

    # 支持下标访问 collection[0]
    def __getitem__(self, index: int) -> T:
        return self._items[index]

    # 根据索引删除元素
    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Неверный индекс")  # 索引越界
        return self._items.pop(index)

    # 按名字排序
    def sort_by_name(self) -> None:
        self._items.sort(key=lambda x: x.name if hasattr(x, 'name') else "")

    # 按最终成绩排序（默认从高到低）
    def sort_by_final_grade(self, reverse: bool = True) -> None:
        self._items.sort(key=lambda x: x.get_final_grade() if hasattr(x, 'get_final_grade') else 0, reverse=reverse)

    # 获取所有优秀学生（全部科目≥85）
    def get_excellent_students(self) -> List[T]:
        return [i for i in self._items if hasattr(i, 'is_excellent') and i.is_excellent()]

    # 按班级获取学生（别名方法）
    def get_students_by_group(self, group: str) -> List[T]:
        return self.find_by_group(group)

    # -------------------------- 4分要求的高阶方法 --------------------------
    # 通用查找：返回第一个满足条件的元素
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    # 通用过滤：返回所有满足条件的元素
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    # 通用映射：把每个元素转换成另一种类型（T→R）
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]

    # 通用自定义排序
    def sort_by(self, key_func: Callable[[T], any], reverse: bool = False) -> None:
        self._items.sort(key=key_func, reverse=reverse)

    # 打印对象时显示的内容
    def __str__(self) -> str:
        return f"TypedCollection(элементов: {len(self)})"

# -------------------------- 带协议限制的集合（5分） --------------------------
# 只能存放实现了 Displayable 协议的对象
class DisplayableCollection(TypedCollection[D]):
    # 批量调用 display() 方法打印所有元素
    def display_all(self) -> None:
        for idx, item in enumerate(self._items, 1):
            print(f"{idx}. {item.display()}")