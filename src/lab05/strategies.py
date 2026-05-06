from lab03.models import Student, BachelorStudent, MasterStudent, PhDStudent

# 排序策略（3个）

# 1. 按姓名排序
def sort_by_name(student: Student):
    return student.name

# 2. 按平均分排序
def sort_by_final_grade(student: Student):
    return student.get_final_grade()

# 3. 按学生类型排序（本科生→研究生→博士生）
def sort_by_type(student: Student):
    type_order = {
        BachelorStudent: 0,
        MasterStudent: 1,
        PhDStudent: 2
    }
    return type_order[type(student)]

# 过滤策略（2个以上）

# 1. 筛选平均分≥90的优秀学生
def filter_excellent(student: Student):
    return student.get_final_grade() >= 90

# 2. 筛选本科生
def filter_bachelor(student: Student):
    return isinstance(student, BachelorStudent)

# 3. 筛选有奖学金的学生
def filter_with_scholarship(student: Student):
    if isinstance(student, BachelorStudent):
        return student.scholarship
    return False

# 转换策略（给map用)

# 把学生对象转成姓名
def map_to_name(student: Student):
    return student.name

# 给所有学生成绩加5分
def map_grade_plus5(student: Student):
    student.exam_grade += 5
    student.hw_grade += 5
    return student