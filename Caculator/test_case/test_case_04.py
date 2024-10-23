import logging

import allure
import pytest
from get_data.get_data import GetData
from func.func import Caculator

from test_case.allure.allure_test_steps import step5

"""
-------------------------------------------------------------
case_04: 用户输入运算数据a、b，运算规则不合法

优先级：

前置条件：

测试步骤；
        1、输入数据a、b, b=0，调用div()方法；

预期结果：
        1、程序输出异常类型，并输出异常提示：除数不能为0；
--------------------------------------------------------------

作者：wang-min
创建时间：2024.04.23
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

    @allure.title("用户输入运算数据a、b，运算规则不合法")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-3?filter=allissues", "用例管理系统")
    @allure.issue("http://192.168.40.134:8080/projects/BUG/issues/BUG-2?filter=allopenissues", "Bug管理系统")
    @pytest.mark.xfail
    @pytest.mark.test_zero_division_error
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expected', GetData.get_zero_division_error())
    def test_zero_division_error(self, a, b, expected, cmd_option):
        """
        测试div()函数对除数为0的异常进行异常提示
        :param a: 模拟用户输入的数据 a
        :param b: 模拟用户输入的数据 b
        :param expected: 输出异常类型ZeroDivisionError，并输出异常提示：除数不能为0
        :return: 返回异常类型ZeroDivisionError，并输出异常提示：除数不能为0
        """
        # step5(a, b, expected)
        print(cmd_option)
        with allure.step("1、输入数据a、b, b=0，调用div()方法；"):
            caculator = Caculator(a, b)
            with open("../allure_print_screen/3.png", mode="rb") as f:
                file = f.read()
                allure.attach(file, "报错页面截图", attachment_type=allure.attachment_type.PNG)
            try:
                # 可能产生异常的代码块
                assert caculator.div() == expected
                logging.info("这是test_case_04测试用例")

            except ZeroDivisionError:
                # 处理异常的代码块
                logging.error("ZeroDivisionError: 除数不能为0")
                assert False, "ZeroDivisionError: 除数不能为0"

    def teardown_method(self):
        """
        清除操作
        :return: 返回清除操作是否成功的结果
        """
        pass
