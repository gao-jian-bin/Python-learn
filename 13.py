my_dic = {
    "gao":{
        'math':90,
        'chinese':70,
        'english':85
    },
    "xiao":{

        'chinese':74,
        'english':95,
        'math':88,
        'japanese':64
    },
    4:{
        'math':-1,
        'chinese':100
    }
}

my_dic['qing'] = {'english':99, 'maeh':8888}
print(my_dic)
my_dic['gao'] = {}
print(my_dic)
my_dic['qing'].pop('english')
print(my_dic)
print(type(my_dic.keys()))
print('_________________-----------')
g = 0
for i in my_dic.keys():
    g += 1
    print(i)
    print(type(i))
    print(g)
print('------------------')
print(len(my_dic))
print('------------------')
print(my_dic.get('qing').get('maeh'))
print(len(my_dic['xiao']))