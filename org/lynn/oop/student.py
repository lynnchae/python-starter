# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType


class Human(object):
    __slots__ = ('name')  # 用tuple定义允许绑定的属性名称，仅对当前类实例起作用，对继承的子类是不起作用

    def speak(self, word):
        print('Human:' + word)


class Student(Human):
    count = 0

    def __init__(self, name, score, idcard):
        self.name = name
        self.score = score
        # 私有属性，访问限制
        # 以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
        self.__idcard = idcard
        Student.count += 1

    def print_score(self):
        print('%s\'s score is %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_idcard(self):
        return self.__idcard

    def speak(self, word):
        print('Student loudly said:' + word)


class WhiteWalker(object):

    def speak(self, word):
        print('Whitewalker just screaming: ' + word)


def speak(Human, word):
    Human.speak(word)


jack = Student('jack', 89, 340000199101115678)

print(jack.get_grade())
print(jack.get_idcard())

human = Human()

# 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
whitewalker = WhiteWalker()
speak(human, 'hello i\'m a human')
speak(jack, 'hello i\'m a student')
speak(whitewalker, 'dfaerafdfiajfia')

# getattr()、setattr()以及hasattr()

print(dir(jack))

print(getattr(jack, 'name'))
print(hasattr(jack, 'name'))
print(Student.count)


def extendmethod(self):
    print('>>>extend method bind')


# 动态绑定方法

jack.extendmethod = MethodType(extendmethod, jack)

jack.extendmethod()

# 为所有实例对象绑定方法
Student.extendmethod = extendmethod

tom = Student('Tom', 92, 340000199102120987)
tom.extendmethod()

human.name='Lily'
human.age=19