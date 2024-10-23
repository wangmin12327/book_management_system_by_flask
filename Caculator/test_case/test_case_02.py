import logging

import allure
import pytest
from get_data.get_data import GetData
from func.func import Caculator
from test_case.allure.allure_test_steps import step3
from test_case.allure.allure_test_steps import step4

"""
-------------------------------------------------------------
test_case_02: 用户输入运算数据a、b, a、b的数据类型不合法

优先级：

前置条件：

测试步骤；
        1、输入数据a、b, a、b为除int整型、float浮点型、double浮点型以外的其他数据类型,调用add()方法；
        2、输入数据a、b, a、b为除int整型、float浮点型、double浮点型以外的其他数据类型,调用div()方法；

预期结果：
        1、程序运行失败，并输出报错提示：输入的数据a、b数据类型不合法；
        2、程序运行失败，并输出报错提示：输入的数据a、b数据类型不合法；
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

    @allure.title("用户输入运算数据a、b, a、b的数据类型不合法")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-2?filter=allissues",
                     "用例管理系统")
    @allure.issue("http://192.168.40.134:8080/projects/BUG/issues/BUG-1?filter=allopenissues", "Bug管理系统")
    # @pytest.mark.xfail
    @pytest.mark.test_data_type_error
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expected', GetData.get_data_type_error())
    def test_add_data_type_error(self, a, b, expected, cmd_option):
        """
        测试add()函数对输入数据的数据类型报错提示
        :param a: 除int整型、float浮点型、double浮点型以外的其他数据类型
        :param b: 除int整型、float浮点型、double浮点型以外的其他数据类型
        :param expected: 输出报错提示: 输入的数据a、b数据类型不合法；
        :return: 返回报错提示：输入的数据a、b数据类型不合法；
        """
        # step3(a, b, expected)
        print(cmd_option)
        with allure.step("1、输入数据a、b, a、b为除int整型、float浮点型、double浮点型以外的其他数据类型,调用add()方法；"):
            caculator = Caculator(a, b)
            with open("../allure_print_screen/1.png", mode="rb") as f:
                file = f.read()
                allure.attach(file, "报错页面截图", attachment_type=allure.attachment_type.PNG)
            try:
                # 可能产生异常的代码块
                assert caculator.add() == expected
                logging.info("这是test_case_02测试用例")

            except TypeError:
                # 处理异常的代码块
                logging.error("TypeError: 输入的数据a、b数据类型不合法")
                assert False, "输入数据a、b不合法"

    @allure.title("用户输入运算数据a、b, a、b的数据类型不合法")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-2?filter=allissues",
                     "用例管理系统")
    @allure.issue("http://192.168.40.134:8080/projects/BUG/issues/BUG-1?filter=allopenissues", "Bug管理系统")
    # @pytest.mark.xfail
    @pytest.mark.test_data_type_error
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expected', GetData.get_data_type_error())
    def test_div_data_type_error(self, a, b, expected, cmd_option):
        """
        测试div()函数对输入数据的数据类型报错提示
        :param a: 除int整型、float浮点型、double浮点型以外的其他数据类型
        :param b: 除int整型、float浮点型、double浮点型以外的其他数据类型
        :param expected: 输出报错提示: 输入的数据a、b数据类型不合法；
        :return: 返回报错提示：输入的数据a、b数据类型不合法；
        """
        # step4(a, b, expected)
        print(cmd_option)
        with allure.step("1、输入数据a、b, a、b为除int整型、float浮点型、double浮点型以外的其他数据类型,调用add()方法；"):
            caculator = Caculator(a, b)
            with open("../allure_print_screen/2.png", mode="rb") as f:
                file = f.read()
                allure.attach(file, "报错页面截图", attachment_type=allure.attachment_type.PNG)
            try:
                # 可能产生异常的代码块
                assert caculator.div() == expected
                logging.info("这是test_case_02测试用例")

            except TypeError:
                # 处理异常的代码块
                logging.error("TypeError: 输入的数据a、b数据类型不合法")
                assert False, "输入数据a、b不合法"

    def teardown_method(self):
        """
        清除操作
        :return: 返回清除操作是否成功的结果
        """
        pass
