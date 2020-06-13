# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: animal.py
import yaml


class Animal(object):
    """
    类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    """
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.sound = None
        
    def can_makes_sound(self):
        self.sound = 'default'
        return self.sound
    
    def can_run(self):
        pass
        

class Cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = 'short'
        self.sound = None
        self.skill = {'catch_mouse': True}
        
    def can_catch_mouse(self):
        if self.skill['catch_mouse']:
            print(f'{self.name},{self.color},{self.age},{self.gender},{self.hair}捉到了老鼠')

    def can_makes_sound(self):
        self.sound = '喵喵叫'
        return self.sound


class Dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = 'long'
        self.sound = None
        self.skill = {'care_home': True}
    
    def can_care_home(self):
        if self.skill['care_home']:
            print(f'{self.name},{self.color},{self.age},{self.gender},{self.hair}')
    
    def can_makes_sound(self):
        self.sound = '汪汪叫'
        return self.sound


if __name__ == '__main__':
    """
    创建一个猫猫实例
    - 调用捉老鼠的方法
    - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    创建一个狗狗实例
    - 调用【会看家】的方法
    - 打印【狗狗的姓名，颜色，年龄，性别，毛发】
    """
    with open('config.yaml') as file:
        config = yaml.load(file)
    cat_attributes = config['cat']
    dog_attributes = config['dog']
    cat = Cat(cat_attributes['name'], cat_attributes['color'], cat_attributes['age'], cat_attributes['gender'])
    cat.can_catch_mouse()
    dog = Dog(dog_attributes['name'], dog_attributes['color'], dog_attributes['age'], dog_attributes['gender'])
    dog.can_care_home()
