# from main import test_b,test_a,print_hi
# print_hi(68)
# test_a(2,9)
# test_b(6,8)
# # if __name__ == '__main__':
# #     print(1)
# #
# # if __name__ == '__main__':
# #     print(2)
# # _name = 'gao'
# # nan = 'jian'
# # dic1 = {'1_name':'gao', 1:15, c:4656}
# # a = dic1.get(b)
# # print(a)
# """
# __这种函数__到底怎么用，什么意思
# """
# f = None
#
# try:
#     f = open("C:\\Users\\18204\\Desktop\\代码.txt", 'r',encoding='utf-8')
#     re = f.read()
#     print(re)
# except Exception as e:
#     print(f'error:{e}')
# finally:
#     if f:
#         f.close()
# f = open('gaojian', 'r', encoding='utf-8')
# f.read()
# print(f)
# print(type(f))

from my_package.file_util import *
from my_package.str_util import *
print_file_info("c:\\Users\\18204\\Desktop\\代码.txt")
append_to_file("c:\\Users\\18204\\Desktop\\代码.txt", '我测你们吗！')
str_reverse(['g', 'j', 'b', 'x', 'q', 'q'])
substr((1, 2, 3, 4, 5, 6, 'gao', 'jian'), 1,5)
