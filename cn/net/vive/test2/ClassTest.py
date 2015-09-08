# file:
# coding:utf-8

__author__ = 'robin'

import cn.net.vive.test2.ReverseType as ReverseType
ReverseType.test()



quit()

from cn.net.vive.test2.MyClassType import MyClass
from cn.net.vive.test2.AnimalType import Animal
from cn.net.vive.test2.PersonType import Person
from cn.net.vive.test2.TeacherType import Teacher
from cn.net.vive.test2.StudentType import Student


def test():
    myClass = MyClass()
    animal = Animal('cat')
    animal2 = Animal('pig')
    person = Person()
    student = Student()
    teacher = Teacher()

    print animal.name,animal2.name
    print animal.instances,animal2.instances
    animal.add_tricks('animal')
    animal2.add_tricks('animal2')
    print animal.tricks,animal2.tricks

    animal2.counter = 1
    while animal2.counter < 10:
        animal2.counter = animal2.counter * 2

    print animal2.counter
    print animal2.f()
    # 方式1
    af = animal2.f()
    print af
    # 方式2
    af2 = animal2.f
    print af2()
    # print animal2.list_keys()
    # teacher.hello()
    # student.readme()

