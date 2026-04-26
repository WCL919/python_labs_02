# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

# 接口 1：可打印
class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

# 接口 2：可比较
class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        pass

# 接口 3：可导出信息（5分要求）
class Exportable(ABC):
    @abstractmethod
    def export_info(self) -> dict:
        pass