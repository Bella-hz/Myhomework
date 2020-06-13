# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: exercise.py

# 有参数/无参数，有返回值和无返回值


def func1():
    print("这是一个无参数方法")
    print("同时这也是一个无返回值的方法,返回值为None")


def func2(param):
    print(f"这是一个有参数方法,输入参数为{param}")
    print("同时这也是一个有返回值的方法,返回值为输入的参数")
    return param
    

if __name__ == '__main__':
    print("下面我们来验证一下")
    "调用方法func1，没有输入参数可直接打印"
    result1 = func1()
    result2 = func2('这是个测试')
    assert result1 is None
    assert result2 == '这是个测试'

