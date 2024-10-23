"""登录页，用户登录"""
from time import sleep

import allure

from page_obj.base_page import BasePage


class LoginPage(BasePage):
    """登录页，用户复用 cookie 登录"""
    def reuse_cookies_login(self):
        """
        复用 cookie 登录
        :return: 跳转到首页
        """
        with allure.step("前置条件：企业微信复用cookie登录成功，并截图和打印page_source"):
            # 获取 cookies
            self.get_cookies()
            # 植入cookies
            self.add_cookies()
            # 再次登录企业微信时，无需扫码，自动登录
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            sleep(3)
            # 截图
            self.get_screen_shot()

            sleep(3)
            # 打印page_source
            self.get_page_source()

        from page_obj.home_page import HomePage
        return HomePage(self.driver)
