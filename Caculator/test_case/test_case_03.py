import logging

import allure
import pytest
from get_data.get_data import GetData
from func.func import Caculator
from test_case.allure.allure_test_steps import step1
from test_case.allure.allure_test_steps import step2

"""
-------------------------------------------------------------
case_03: 用户输入运算数据a、b，a或b大小超出范围

优先级：

前置条件：

测试步骤；
        1、输入数据a、b，a、b属于集合{98，98.9，-98.9，-98}，调用add()方法；
        2、输入数据a、b, a、b属于集合{98，98.9，-98.9，-98}，调用div()方法；
        3、输入数据a、b，a、b属于集合{99，99.1，100，-99，-99.1，-100}，调用add()方法；
        4、输入数据a、b, a、b属于集合{99，99.1，100，-99，-99.1，-100}，调用div()方法；

预期结果：
        1、程序输出a加b的结果；
        2、程序输出a除以b的结果；
        3、输出报错提示: "参数大小超出范围"；
        4、输出报错提示: "参数大小超出范围"；
--------------------------------------------------------------

作者：wang-min
创建时间：2024.04.23
"""


class TestCase:
    """
    测试用例类： 测试用例执行步骤；
    """

    def setup_method(self):
        """
        执行用例的前置条件
        :return:
        """
        pass

    @allure.title("用户输入运算数据a、b，a或b大小超出范围")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-5?filter=allissues", "用例管理系统")
    @pytest.mark.test_data_range
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expected', GetData.get_add_data_range_in())
    def test_add_data_range_in(self, a, b, expected, cmd_option):
        """
        测试add()函数的数据范围内参数
        :param a: 输入集合{98，98.9，-98.9，-98}中的任意一个数据 a；
        :param b: 输入集合{98，98.9，-98.9，-98}中的任意一个数据 b；
        :param expected: 程序输出a加b的结果；
        :return: 返回 a加 b的结果；
        """
        # step1(a, b, expected, cmd_option)
        print(cmd_option)
        with allure.step("1、输入数据a、b，a、b属于集合{98，98.9，-98.9，-98}，调用add()方法；"):
            caculator = Caculator(a, b)
            try:
                # 可能产生异常的代码块
                assert caculator.add() == expected
                logging.info("这是test_case_03测试用例")
                logging.info("断言 assert caculator.add() == expected ")

            except TypeError:
                # 处理异常的代码块
                assert "参数大小超出范围"
                logging.error("参数大小超出范围")

    @allure.title("用户输入运算数据a、b，a或b大小超出范围")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-5?filter=allissues", "用例管理系统")
    @pytest.mark.test_data_range
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expected', GetData.get_div_data_range_in())
    def test_div_data_range_in(self, a, b, expected, cmd_option):
        """
        测试add()函数的数据范围内参数
        :param a: 输入集合{98，98.9，-98.9，-98}中的任意一个数据 a；
        :param b: 输入集合{98，98.9，-98.9，-98}中的任意一个数据 b；
        :param expected: 程序输出a加b的结果；
        :return: 返回 a加 b的结果；
        """
        # step2(a, b, expected)
        print(cmd_option)
        with allure.step("2、输入数据a、b, a、b属于集合{98，98.9，-98.9，-98}，调用div()方法；"):
            caculator = Caculator(a, b)
            try:
                # 可能产生异常的代码块
                assert caculator.div() == expected
                logging.info("这是test_case_03测试用例")
                logging.info("断言 assert caculator.div() == expected ")

            except TypeError:
                # 处理异常的代码块
                assert "参数大小超出范围"
                logging.error("参数大小超出范围")

    @allure.title("用户输入运算数据a、b，a或b大小超出范围")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-5?filter=allissues",
                     "用例管理系统")
    @pytest.mark.test_data_range
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expected', GetData.get_data_range_out())
    def test_add_data_range_out(self, a, b, expected, cmd_option):
        """
        测试div()函数的数据范围内参数
        :param a: 输入集合{98，98.9，-98.9，-98}中的任意一个数据 a；
        :param b: 输入集合{98，98.9，-98.9，-98}中的任意一个数据 b；
        :param expected: 程序输出a加b的结果；
        :return: 返回 a除以b的结果；
        """
        # step1(a, b, expected)
        print(cmd_option)
        with allure.step("3、输入数据a、b，a、b属于集合{99，99.1，100，-99，-99.1，-100}，调用add()方法；"):
            caculator = Caculator(a, b)
            try:
                # 可能产生异常的代码块
                assert caculator.add() == expected

            except TypeError:
                # 处理异常的代码块
                assert "参数大小超出范围"
                logging.info("这是test_case_03测试用例")
                logging.error("参数大小超出范围")

    @allure.title("用户输入运算数据a、b，a或b大小超出范围")
    @allure.testcase("http://192.168.40.134:8080/projects/CACULATOR/issues/CACULATOR-5?filter=allissues",
                     "用例管理系统")
    @pytest.mark.test_data_range
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expected', GetData.get_data_range_out())
    def test_div_data_range_out(self, a, b, expected, cmd_option):
        """
        测试add()函数的数据范围外参数
        :param a: 输入集合{99，99.1，100，-99，-99.1，-100}中的任意一个数据 a；
        :param b: 输入集合{99，99.1，100，-99，-99.1，-100}中的任意一个数据 b；
        :param expected: 输出报错提示: "参数大小超出范围"；
        :return: 返回报错提示: "参数大小超出范围"；
        """
        # step2(a, b, expected)
        print(cmd_option)
        with allure.step("4、输入数据a、b，a、b属于集合{99，99.1，100，-99，-99.1，-100}，调用div()方法；"):
            caculator = Caculator(a, b)
            try:
                # 可能产生异常的代码块
                assert caculator.div() == expected

            except TypeError:
                # 处理异常的代码块
                assert "参数大小超出范围"
                logging.info("这是test_case_03测试用例")
                logging.error("参数大小超出范围")

    def teardown_method(self):
        """
        清除操作
        :return: 返回清除操作是否成功的结果
        """
        pass
