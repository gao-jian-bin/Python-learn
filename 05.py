# i = 1
# while i <= 18:
#     j = 1
#     while j <= i:
#             print(f"{j} * {i} = {j * i}\t",end=" ")
#             j += 1
#     print()
#     i += 1
# i = 1
# max_value = 9 * 18  # 最大的算式结果
# max_digits = len(str(max_value))  # 最大结果的位数
#
# while i <= 18:
#     j = 1
#     while j <= i:
#         result = j * i
#         print(f"{j} * {i} = {result:{max_digits}}", end="\t")  # 使用最大位数来格式化对齐
#         j += 1
#     print()
#     i += 1

# name = "a itgaojainbin is a fantastic code"
# # num = 0
# # for i in name:
# #    if i == "a" :
# #        num += 1
# # print(f"there are(is) {num} a ")
# i = 1
# while i < 10:
#     for j in range(1,i+1):
#             print(f"{j} * {i} = {i * j}\t",end = " ")
#     i += 1
#     print()
n = int(input())
num1 = 0
num2 = 0
for _ in range(n):
    score = int(input())
    if score >= 60:
        num1 += 1
    if score >= 85:
        num2 += 1
print(str(round(num1*100/n))+'%')
print(str(round(num2*100/n))+'%')




















