# !/usr/bin/env python3
# -*- coding: utf-8 -*-


class Human(object):
    def speak(self, word):
        print('Human:' + word)


class Student(Human):

    def __init__(self, name, score, idcard):
        self.name = name
        self.score = score
        # 私有属性，访问限制
        # 以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
        self.__idcard = idcard

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
