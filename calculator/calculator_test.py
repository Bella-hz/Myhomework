# ! /usr/bin/env python
# coding = utf-8
# __author__ = 'wyn'
# Filename: calculator_test.py
from pytest import approx
import pytest
import yaml
import os


work_path = os.path.abspath(os.path.dirname(__file__))
testdata_file = os.path.join(work_path, 'calculator_testdata.yaml')
with open(testdata_file) as file:
    testdata = yaml.safe_load(file)


class TestCal:
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    @pytest.mark.usefixtures('cmd_option')
    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['add'])
    def test_add(self, create_cal, a, b, result, cmd_option):
        print(f'{a}+{b}={result}')
        print(f"当前环境{cmd_option}")
        assert create_cal.add(a, b) == approx(result)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['sub'])
    def test_sub(self, create_cal, a, b, result):
        print(f'{a}-{b}={result}')
        assert create_cal.sub(a, b) == approx(result)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['mul'])
    def test_mul(self, create_cal, a, b, result):
        print(f'{a}*{b}={result}')
        assert create_cal.mul(a, b) == approx(result)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.parametrize(('a', 'b', 'result'), testdata['div'])
    def test_div(self, create_cal, a, b, result):
        print(f'{a}/{b}={result}')
        assert create_cal.div(a, b) == approx(result)
