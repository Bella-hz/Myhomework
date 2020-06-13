# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: calculator.py


class Calculate:
    @classmethod
    def add(cls, a, b):
        return a + b
    
    @classmethod
    def sub(cls, a, b):
        return a - b
    
    @classmethod
    def mul(cls, a, b):
        return a * b
    
    @classmethod
    def div(cls, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return False
