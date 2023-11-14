class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass

class Teacher(Person):
    pass


class Factory(Person):
    def get_person(self, _type):
        if _type == 'w':
            return Worker()
        elif _type == 's':
            return Student()
        else:
            return Teacher()


factory = Factory()
worker = factory.get_person('w')
student = factory.get_person('s')
teacher = factory.get_person('t')





