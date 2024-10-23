"""小商城程序测试框架首页"""
import pytest
from log_utils import logger
from page_object.login_page import LoginPage


class TestLiteMall:
    def setup_class(self):
        """
        前置动作
        1、访问 https://litemall.hogwarts.ceshiren.com/
        2、找到账号输入框,清除默认账号,输入账号
        3、找到密码输入框,清除默认密码,输入密码
        4、找到登录按钮,点击登录
        :return:
        """
        """登录页面，用户登录"""
        logger.info("登录页面，用户登录")
        self.home = LoginPage().login()

    def teardown_class(self):
        """
        后置动作
        销毁浏览器进程
        :return:
        """
        self.home.do_quit()

    @pytest.mark.parametrize("category_num, category_name",
                             [["1450638", "王者农药01"], ["1450639", "王者农药02"]])
    def test_add_commodity(self, category_num, category_name):
        """
        新增商品
        1、点击首页
        2、点击商品管理
        3、点击商品列表
        4、点击添加按钮
        5、生成截图到allure测试报告中
        6、断言，商品列表中是否存在新添加的商品
        7、处理脏数据
        :return:
        """
        """首页，跳转到商品列表页"""
        """商品列表页，跳转到商品上架页"""
        """商品列表页，跳回到商品列表页"""
        list_page = self.home. \
            go_category_List_page(). \
            go_category_add_page(). \
            create_category(category_num, category_name)
        res = list_page.get_category_add_page_result()
        assert "创建成功" == res
        # 清理新增的数据
        list_page.delete_category(category_num)

    @pytest.mark.parametrize("category_num, category_name", [["1450640", "王者农药01"], ["1450641", "王者农药02"]])
    def test_delete_commodity(self, category_num, category_name):
        """
        删除商品
        1、点击商品管理
        2、点击商品列表
        3、点击删除按钮
        4、断言，商品列表中是否存在删除的商品
        5、生成截图到allure测试报告中
        :return:
        """
        res = self.home. \
            go_category_List_page(). \
            go_category_add_page(). \
            create_category(category_num, category_name). \
            delete_category(category_num). \
            get_category_del_page_result()
        assert "删除成功" == res
