# -*- coding: UTF-8 -*-


class Person:
    '''
    测试用person
    '''
    def __init__(self,name):
        self.name = name

    def sayHello(self):
        print 'hello,' + self.name

class Man(Person):
    '''
    测试用man
    '''
    def tellSex(self):
        print 'i am man'

if __name__ == '__main__':
    # person = Person('ycl')
    # person.sayHello()
    # print person.__doc__

    man = Man('long')
    man.sayHello()
    man.tellSex()
    print man.__doc__