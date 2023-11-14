# #
# #
# # def outter(word):
# #
# #
# #     def inner(mesg):
# #         print(f"<{word}>{mesg}<{word}>")
# #
# #
# #     return inner
# #
# #
# #
# # test = outter(f'煎饼科技')
# # test('煎饼科技欢迎你')
# def deposite(init_acot=0):
#
#     def deposite1(num, pos:bool=True):
#         nonlocal init_acot
#         if pos:
#             init_acot += num
#             print(f'success+{num},you have {init_acot} now')
#         else:
#             init_acot -= num
#             print(f'success-{num},you have {init_acot} now')
#
#     return deposite1
# a = deposite()
# a(100,True)
# a(100,True)
# a(100,True)
# a(100,False)
# #闭包
#
class tool:
    pass


too1 = tool()