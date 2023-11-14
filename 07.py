# name = "nihaogaojianbin"
# print(len(name))



def hs(a):
    if a <= 37.5:
        print(f"欢迎，正常进入")
    else:
        print("对不起，您需要隔离")
#
#
# hs(38.4)
# def add(x,y,z):
#     """
#
#     :param x: 第一个参数值
#     :param y: 第二个参数值
#     :param z: 第三个参数值
#     :return: 返回三个数相加的结果
#     """
#     result = x + y + z
#     print(f"两数相加结果是{result:.100f}\n")
#     return result
#
# x = add(2.25343453463453453468343453543,5,4)
# print(type(x))
a = 0
def fun_a():
    print("_________a__________")
    global a
    return  fun_b()



def fun_b():
    """

    :return:
    """

    return print("_________b__________")
    fun_a()


b = fun_a()
# print(b)
c = fun_b()
print(a)


# num = 100
# def fun_c():
#     print(f"{num}")
#     fun_d()
#
# def fun_d():
#     global num
#     num = 200
#     print(num)
#
# fun_c()
# fun_d()
# print(num)