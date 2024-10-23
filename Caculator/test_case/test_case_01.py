import logging

import pytest
import allure
from test_case.allure.allure_test_steps import step1
from test_case.allure.allure_test_steps import step2

from func.func import Caculator
from get_data.get_data import GetData

"""
-------------------------------------------------------------
test_case_01: 用户输入运算数据a、b, 程序输出正确的结果

优先级：

前置条件：

测试步骤；
        1、输入数据a、b, 调用add()方法；
        2、输入数据a、b, 调用div()方法；

预期结果：
        1、程序输出a加b的结果；
        2、程序输出a除以b的结果；
--------------------------------------------------------------

作者：wang-min
创建时间：2024.04.15
"""


class TestCase:
    """
    测试用例类： 测试用例执行步骤
    """

    def setup_method(self):
        """
        执行用例的前置条件
        :return:
        """
        pass

    @allure.title("用户输入运算数据a、b, 程序输出正确的结果")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-4?filter=allissues",
                     "用例管理系统")
    @pytest.mark.test_normal
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expected', GetData.get_add_data())
    def test_add(self, a, b, expected, cmd_option):
        """
        测试add()函数
        :param a: 用户输入的数据a
        :param b: 用户输入的数据b
        :param expected: 输出a加b的结果
        :return: 返回a加b的结果
        """
        # step1(a, b, expected)
        print(cmd_option)
        with allure.step("1、输入数据a、b, 调用add()方法；"):
            caculator = Caculator(a, b)
            try:
                # 可能产生异常的代码块
                assert caculator.add() == expected
                logging.info("这是test_case_01测试用例")
                logging.info("断言 assert caculator.add() == expected")

            except TypeError:
                # 处理异常的代码块
                assert "输入数据a、b不合法"

    @allure.title("用户输入运算数据a、b, 程序输出正确的结果")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-4?filter=allissues",
                     "用例管理系统")
    @pytest.mark.test_normal
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expected', GetData.get_div_data())
    def test_div(self, a, b, expected, cmd_option):
        # step2(a, b, expected)
        print(cmd_option)
        with allure.step("2、输入数据a、b, 调用div()方法；"):
            caculator = Caculator(a, b)
            try:
                # 可能产生异常的代码块
                assert caculator.div() == expected
                logging.info("这是test_case_01测试用例")
                logging.info("断言 assert caculator.div() == expected")

            except ZeroDivisionError:
                # 处理异常的代码块
                assert "除数不能为0"
                logging.info("这是test_case_01测试用例")
                logging.error("ZeroDivisionError: 除数不能为0")

            except TypeError:
                # 处理异常的代码块
                assert "输入数据a、b不合法"
                logging.info("这是test_case_01测试用例")
                logging.error("TypeError: 输入数据a、b不合法")

    def teardown_method(self):
        """
        清除操作
        :return: 返回清除操作是否成功的结果
        """
        pass
