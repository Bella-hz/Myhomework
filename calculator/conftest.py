# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: conftest.py
import pytest
from calculator.calculator import Calculate


@pytest.fixture()
def create_cal():
    cal = Calculate()
    print('开始计算')
    yield cal
    print('计算结束')
