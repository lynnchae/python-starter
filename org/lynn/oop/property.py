# !/usr/bin/env python3

class Student(object):

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @name.setter
    def name(self, value):
        self._name = value

    # 类似java中的toString方法
    def __str__(self):
        return 'Student object (name: %s)' % self._name


jack = Student()

jack.score = 91
print(jack.score)
jack.name = 'jack'
print(jack)
