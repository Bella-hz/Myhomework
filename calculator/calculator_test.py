# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: calculator_test.py
import pytest
import yaml
import os

work_path = os.path.abspath(os.path.dirname(__file__))
testdata_file = os.path.join(work_path, 'calculator_testdata.yaml')
with open(testdata_file) as file:
    testdata = yaml.safe_load(file)


class TestCal:
    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['add'])
    def test_add(self, create_cal, a, b, result):
        if isinstance(a, int) and 1 == len({type(a), type(b), type(result)}):
            print(f'{a}+{b}={result}')
            assert create_cal.add(a, b) == result

    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['sub'])
    def test_sub(self, create_cal, a, b, result):
        if isinstance(a, int) and 1 == len({type(a), type(b), type(result)}):
            print(f'{a}-{b}={result}')
            assert create_cal.sub(a, b) == result

    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['mul'])
    def test_mul(self, create_cal, a, b, result):
        if isinstance(a, int) and 1 == len({type(a), type(b), type(result)}):
            print(f'{a}*{b}={result}')
            assert create_cal.mul(a, b) == result

    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['div'])
    def test_div(self, create_cal, a, b, result):
        if isinstance(a, int) and 1 == len({type(a), type(b), type(result)}):
            print(f'{a}/{b}={result}')
            assert create_cal.div(a, b) == result
