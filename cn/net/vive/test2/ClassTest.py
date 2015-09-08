# file:
# coding:utf-8

__author__ = 'robin'

from cn.net.vive.test2.MyClassType import MyClass
from cn.net.vive.test2.AnimalType import Animal
from cn.net.vive.test2.PersonType import Person
from cn.net.vive.test2.TeacherType import Teacher
from cn.net.vive.test2.StudentType import Student


def test():
    myClass = MyClass()
    animal = Animal()
    person = Person()
    student = Student()
    teacher = Teacher()

    print animal.f()
    # teacher.hello()
    student.readme()

