"""测试主页"""
import os
import sys

# 导入其他模块
from time import sleep
import allure
import pytest

# 将上级目录添加到搜索路径中
dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)

from page_obj.login_page import LoginPage
from page_obj.get_data import get_data


class TestWeCom:
    def setup_class(self):
        """
        复用 cookie 登录
        1、登录成功后，获取 cookies 信息
        2、将 cookies 存入本地文件
        3、从本地获取 cookies
        4、为 self.driver 实例植入 cookie
        5、退出
        6、复用 cookie 登录
        :return:
        """
        self.home = LoginPage().reuse_cookies_login()

    def teardown_class(self):
        """
        退出浏览器，销毁浏览器进程
        :return:
        """
        self.home.do_quit()

    @allure.title("用例标题：添加成员信息成功")
    @pytest.mark.parametrize("name, account, phone_number, business_mail",
                             get_data())
    def test_add_member(self, name, account, phone_number, business_mail):
        """
        添加成员信息
        1、输入 姓名、企业邮箱、手机号
        2、截图
        3、点击保存
        4、多断言：
          所有的成员姓名是否包含添加时输入的姓名；
          所有的成员手机号是否包含添加时输入的手机号；
          所有的成员邮箱是否包含添加时输入的邮箱。
        :return: 跳转到通讯录页
        """
        member_list = self.home.go_to_contacts(). \
            add_member(name, account, phone_number, business_mail)
        res = member_list.get_add_member_result()
        # 清除新增成员数据
        sleep(3)
        member_list.del_add_member_result()

        with allure.step("打印通讯录页面的所有成员及对应手机号、邮箱"):
            print(res)

        with allure.step("多断言：所有的成员姓名是否包含添加时输入的姓名;所有的成员手机号是否包含添加时输入的手机号;\
                        所有的成员邮箱是否包含添加时输入的邮箱。"):
            assert name in res
            sleep(3)
            assert phone_number in res
            sleep(3)
            assert business_mail in res
