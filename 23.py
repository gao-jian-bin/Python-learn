class Phone:
    __current_statu = True

    def __5g_check(self):
        if self.__current_statu:
            print('5g启动!')
        else:
            print('开发5g中')

    def doit(self):
        self.__5g_check()


object
# Phone().doit()
name = 'gjb'
print(id(name))
print(id('gjb'))
print(id(Phone()))
print('---------')
a = int()

b = a('13')
print(b)
print(type(b))