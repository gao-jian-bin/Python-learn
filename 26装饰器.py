#
#
# def outer(func):
#
#
#     def inner():
#         print('time to sleep')
#         func()
#         print('slept')
#
#     return inner
#
# @outer
# def sleep():
#     import time,random
#     print('sleeping')
#     time1 = random.randint(1,5)
#     time.sleep(time1)
#     print(f'using {time1} s')
# 3
#
#
#
#
#
#
#
#
#
#
#
#
# # fn = outer(sleep)
# # fn()
# sleep()
from my_package.single import tool1
a = tool1
b = tool1
print(a)
print(b)

from single import tool1
a = tool1
b = tool1
print(a)
print(b)