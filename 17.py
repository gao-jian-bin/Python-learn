# lambda x, y: x + y
# b = lambda 1, 2
# print(b)
# 创建 lambda 函数，接受两个参数并返回它们的和
# b = lambda x, y, c=0: x + y + c
# print(b(1,2,3))

# 使用 lambda 函数计算 1 + 2
# result = b(1, 2)
# print(result)  # 输出结果为 3

# try:
#     # print(gao)
#     1 / 0
# except (Exception) as e:
#
#     print(e)

#    print(type(e))
# print(Exception)
# print(dir(Exception))
try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError as e:
    print(f"File not found: {e}")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found")
except IOError:
    print("An I/O error occurred")
except Exception:
    print("An unexpected error occurred")
try:
    name-jia == 'gaoa'
except Exception as e:
    print({e})
print('---')
try:
    name-jia == 'gaoa'
except Exception:
    print({Exception})
'''
e的作用是对在异常类中匹配的异常实例进行接收
'''