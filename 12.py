my_list = ["科技大学", "软件工程", "科技大学", "gao", "jian", "bin"]
lis0 = ['gao']
print(type(lis0))
abc = set(lis0)
print(abc)
my_set2 = set()
for my_list1 in my_list:
    my_set2.add(my_list1)
print(my_set2)
my_set2 = (my_list)
print(my_set2)#lksandjfl;sa;fao;sfl;jojnn
name = "gao"
print(dir(list))
set1 = {1, 2, 8, 9}
print(type(set1))
print("---------------------------")
dict1 = {"gao":123, "jian":0, "gao":456, "bin":1, 7:"xqq"}
a = dict1["gao"]
print(a)
print("---------------------------")
for i in dict1:
    print(dict1[i])
print("---------------------------")

set2 = {7, 2, 2, 4, 5, 6, 7}
a = set1.union(set2)
print(a)
b = set1.difference(set2)
print(b)
c = set1.difference_update(set2)

print(set1)