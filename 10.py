# tuple1 = (True, 1, "gaojianbin", 13,(2222),((13),(15)))
# tuple2 = ()
# tuple3 = (112)
# print(f"tuple1的内容是{tuple1},类型是{type(tuple1)}")
# print(f"tuple2的内容是{tuple2},类型是{type(tuple2)}")
# print(f"tuple3的内容是{tuple3},类型是{type(tuple3)}")
# print(tuple1.index(13))
# print(len(tuple1))
# index =0
# for index in range(len(tuple1)):
#     print(f"{tuple1[index]}\t",end=" ")
# tuple1 = (True, 1, "gaojianbin", 13,(2222),[(13),(15)])
# tuple1[-1][-2] = 14
# print(tuple1)






tup = ("蔡徐坤",11, 11, 11,["rap", "music", "basketball"])
print(tup.count(11))
print(tup.index(11))
print(tup[0])
del tup[-1][-1]
print(tup)
tup[-1].append("coding")
print(tup)

