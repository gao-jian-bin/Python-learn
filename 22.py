class InfoStud():
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress

    def __str__(self):
        print(f"name is {self.name},age:{self.age}")


    def __lt__(self, other):
        pass


    # def __lt__(self, other):
    #     print (self.age < other.age)

    # def __ge__(self, other):
    #     return self.name >= other.name


stu1 = InfoStud('gao', 122, 000)
stu2 = InfoStud('jian', 123, 000)
stu1.__str__()
stu1.__lt__(stu2)
print(stu1.__ge__(stu2))
a = 1
b = 1
print(a == b)
# print(stu1 < stu2)
# print(stu1 < stu2)
# print(stu1 >= stu2)
# print(stu)
# print(str(stu))
# print(type(stu))


# for i in range(1,11):
#     print(f"当前录入第{i}位学生信息，共需要录入10位")
#     stu = InfoStud(name = str(input(f'输入第{i}位学生的姓名:')), age = int(input(f'输入第{i}位学生的年龄:')), adress = str(input(f'输入第{i}位学生的地址:')))
#
#     # stu.name = name#str(input(f'输入第{i}位学生的姓名:'))
#     # stu.age = age#int(input(f'输入第{i}位学生的年龄:'))
#     # stu.adress = str(input(f'输入第{i}位学生的地址:'))
#     print(f"学生{i}的信息录入完成，【姓名:{stu.name},年龄:{stu.age},地址:{stu.adress}】")
#
#
