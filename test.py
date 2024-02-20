import os
import pytest

def test_aa():
    print("这是输出内容：test。。。。。")
#步骤1： 通过Pytest生成测试报告数据文件，这里带有--alluredir参数 ，生成的数据文件目录为allure-result中

pytest.main(['-s', '-v','./test.py', '--alluredir', 'allure-results'])
# 步骤2 ： 通过allure 读取数据源生成测试报告
"""
解释：
allure-result : 生成的json数据文件目录
"""
cmd = "allure generate allure-results -c"
os.system(cmd)
# print("这是输出内容")
