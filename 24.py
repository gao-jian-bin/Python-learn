#wenjian
class Phone:
    ID = '父亲:20231121'

    name = '父亲:xiaomi-13'

    def call_5g(self):
        print('5g is staring')

class MyPhone(Phone):
    ID = '子:20231122'
    def __private(self):
        print(f'{self.ID}')

    def call_5g(self):
        print(f"厂商是{Phone.ID}")
        Phone.call_5g(self = None)

myphone = MyPhone()
myphone.call_5g()


