""" 基本类 """
import time
import os
from time import sleep

import allure
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# @auto_save_exception_screen_shot
class BasePage:
    """定义基地址"""
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"

    def __init__(self, base_driver=None):
        """
        初始化
        1、实例化 self.driver，并复用浏览器
        2、为每个页面设置 3 秒隐式等待
        3、最大化浏览器窗口
        4、访问基地址 (访问企业微信登录页)
        :param base_driver: 实例化类时，自带的实例化过的driver对象
        """
        if base_driver:
            self.driver = base_driver
        else:
            # 实例化 self.driver，并复用浏览器
            self.driver = webdriver.Chrome()
            self.reuse_browser()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            # 如果当前访问的浏览器url地址不是http网页，那么将导航到基地址中
            self.driver.get(self._BASE_URL)
        # 设置扫二维码登录的等待时间
        sleep(10)

    def reuse_browser(self):
        """
        复用浏览器
        1、实例化Options对象
        2、修改 option 的 debugger_address 属性："localhost:9222"
        3、实例化 driver，需添加 Chrome 的 option 配置
        :return:
        """
        # 实例化Options对象
        option = Options()
        # 修改 option 的 debugger_address 属性："localhost:9222", 这样可以使 localhost:9222 在 debug 模式下打开，便于调试
        option.debugger_address = "localhost:9222"
        # 实例化 driver，需添加 Chrome 的 option 配置
        self.driver = webdriver.Chrome(options=option)

    def get_cookies(self):
        """
        复用cookie
        1、登录成功后，获取 cookie 信息
        2、将 cookie 存入本地文件
        :return:
        """
        # 登录成功后，获取 cookie 信息
        cookies = self.driver.get_cookies()  # 返回一个装了多个 cookie 的列表
        # 将 cookie 存入本地文件
        with open("../data/cookies.yaml", "w", encoding="utf8") as f:
            # yaml.safe_dump , 将目标数据存放到指定文件
            yaml.safe_dump(cookies, f)

    def add_cookies(self):
        """
        植入 cookie
        1、从本地获取 cookies
        2、为 self.driver 实例植入 cookie
        3、退出
        4、复用 cookie 登录
        :return:
        """
        # 获取本地 cookies
        with open("../data/cookies.yaml", "r", encoding="utf8") as f:
            cookies = yaml.safe_load(open("../data/cookies.yaml"))
        # 植入 cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            print(cookie)

    def get_screen_shot(self):
        """
        截图
        1、设置截图保存路径,用带有时间戳的方式命名截图
        2、截图, 并将截图保存到本地文件中
        3、将截图导入到 allure 报告中
        :return:
        """
        time_tamp = time.time()
        image_path = f"../test_case/image_path/image_{time_tamp}.png"
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)

    def get_page_source(self):
        """
        获取page_source
        1、设置page_source本地保存路径，用带有时间戳的方式命名page_source
        2、访问到当前页面，并将 page_source 保存到本地文件中
        3、截图
        4、将 page_source 导入到 allure 报告中
        :return:
        """
        time_tamp = time.time()
        page_source_path = f"../test_case/page_source/page_source_{time_tamp}.html"
        ele = self.driver.current_url
        self.driver.get(ele)
        with open(page_source_path, "w", encoding="utf8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
        self.get_screen_shot()

    def do_find(self, by, locator=None):
        """
        定位界面某个元素节点
        1、如果传入的是元素节点，则直接传参
        2、如果传入的是带定位方式的元组，则先解包后传参
        :param by:定位方式， 例：By.ID、By.NAME等
        :param locator: 元素节点
        :return: 返回定位到的元素节点对象
        """
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        """
        定位界面多个元素节点
        1、如果传入的是元素节点，则直接传参
        2、如果传入的是带定位方式的元组，则先解包后传参
        :param by:定位方式， 例：By.ID、By.NAME等
        :param locator: 元素节点
        :return: 返回定位到的元素节点对象列表
        """
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        """
        输入框中输入信息
        1、定位到输入框的位置
        2、调用sendkeys()方法，输入信息
        :return:
        """
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def webdriver_wait_until_element_find(self, locator: tuple):
        """
        封装显示等待的等待条件：直到元素被找到，才能进行下一步操作
        :param locator: (定位方式，元素节点)
        :return: 返回等待条件结果为真
        """
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def do_quit(self):
        """
        退出浏览器，销毁浏览器进程
        :return:
        """
        self.driver.quit()
