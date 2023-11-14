#
# def info_fun(name, age, gender='男'):
#     print(f'(the name is) {name}\n(the age is) {age}\n(the gender is) {gender}')
#
#
# info_fun(12, 21)
#
#
# def fun15(*i):
#     print(f'{i}', type(i))
#
#
# fun15(1, -1, 'gjb', [1, 2, 3], (4, 5, 6))
#
#
# def fun16(**j):
#     print(f'{j}, {type(j)}')
#
#
# fun16(name='xiao', _12=45, a=48)
# def fun1(a):
#     result = compute(1, 2)
#     print(result)
#
#
# def compute(x, y):
#     return (x + y)
#
# fun1(compute)
# print('------------')
# fun1(lambda x, y: x * y)
# print(lambda x, y: x * y)
import time

open('14.py', 'r', encoding='utf-8')
print(type(open('C:\\Users\\18204\\Desktop\\代码.txt', 'r', encoding='utf-8')))

print(open('C:\\Users\\18204\\Desktop\\代码.txt', 'r', encoding='utf-8'))
print('-----------')
f = open('C:\\Users\\18204\\Desktop\\代码.txt', 'w', encoding='utf-8')
# print(f.readlines())
# a = f.read()
# print(a)
# print(type(a))
f.write('nihaonihao')
f.flush()


