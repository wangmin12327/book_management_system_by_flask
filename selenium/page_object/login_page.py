"""登录页"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from log_utils import logger
from page_object.base_page import BasePage
from test_litemall.web_utils import click_exception


class LoginPage(BasePage):
    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN_LOGIN = (By.XPATH, "//*[@id='app']/div/form/button")

    """登录页面，用户登录"""
    def login(self):
        """
        1、访问 https://litemall.hogwarts.ceshiren.com/
        2、找到账号输入框,清除默认账号,输入账号
        3、找到密码输入框,清除默认密码,输入密码
        4、找到登录按钮,点击登录
        :return: 跳转到首页
        """
        self.do_send_keys("manage", self.__INPUT_USERNAME)
        self.do_send_keys("manage123", self.__INPUT_PASSWORD)
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_LOGIN))
        logger.info("用户登录成功!")

        from page_object.home_page import HomePage
        return HomePage(self.driver)
