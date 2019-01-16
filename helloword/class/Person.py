# -*- coding:UTF-8 -*-

class Person:
    age = 0
    name = ""

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def say(self):
        print "我的名字叫：",self.name
        Person.age += 1