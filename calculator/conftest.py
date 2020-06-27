# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: conftest.py
from calculator.calculator import Calculate
import pytest
import os


@pytest.fixture()
def create_cal():
    cal = Calculate()
    print('开始计算')
    yield cal
    print('计算结束')


def pytest_addoption(parser):
    my_group = parser.getgroup('hogwarts')
    my_group.addoption("--env", default='test', dest='env', help='set your run env')


@pytest.fixture(scope='session')
def cmd_option(request):
    my_env = request.config.getoption("--env", default='test')
    if my_env == 'test':
        os.environ['ENV'] = 'test'
        print("获取test数据")
    elif my_env == 'dev':
        os.environ['ENV'] = 'dev'
        print("获取dev数据")
    elif my_env == 'st':
        os.environ['ENV'] = 'st'
        print("获取st数据")
    return my_env
