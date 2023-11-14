import json

# json list
my_list = ['gao', '高', '3', 3.1415926]
my_list1 = [{'name': '建斌', 'age': 20}, {'name': '晴晴', 'age': 19}]
my_json2 = json.dumps(my_list1, ensure_ascii=False)
print(my_json2)
print(type(my_json2))
print(type(my_list))

my_json = json.dumps(my_list, ensure_ascii=False)
print(my_json)
print(type(my_json))

my_dic = {'name': '肖晴晴', 123: 1.414}
my_json1 = json.dumps(my_dic, ensure_ascii=False)
print(my_json1)
print('---------')

my_json3 = '{"name": "肖晴晴", "123": 1.414}'
my_json4 = json.loads(my_json3)
print(my_json4)

a = '[{"name": "建斌", "age": 20}, {"name": "晴晴", "age": 19}]'
b = json.loads(a)
print(b)
print(type(b))