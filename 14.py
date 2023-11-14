dic6 = {
    '王力红':{
        '部门':'科技部门',
        '工资':3000,
        '级别':1
    },
    '周杰伦':{
        '部门':'市场部门',
        '工资':5000,
        '级别':2
    },
    '林俊杰':{
        '部门':'市场部门',
        '工资':7000,
        '级别':3
    },
    '张学友':{
        '部门':'科技部门',
        '工资':4000,
        '级别':1
    },
    '刘德华':{
        '部门':'市场部门',
        '工资':6000,
        '级别':2
    }

}


print(f'全体员工的信息如下:{dic6}')
for i in dic6:
    if dic6[i]['级别'] == 1:
        dic6[i]['级别'] += 1
        dic6[i]['工资'] += 1000

print(f'修改后的信息为:{dic6}')
print('==============')
my_dict = {('name', 'last_name'): 'Alice Smith', ('age',): 30}
print(my_dict[('name', 'last_name')])
print('================')
name_key = ('name', 'last_name')
value = my_dict[name_key]
print(value)  # 输出 'Alice Smith'
