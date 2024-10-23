"""基础页,在公共父类中封装driver对象"""
import time

import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""父类"""


class BasePage:
    # 先定义基地址
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/"

    def __init__(self, base_driver=None):
        """
        1、判断继承自己的子类 在调用自己的这个类中的 self.driver 时， 是否有自带实例化过的 base_driver参数传入，如果有则用子类的，
            如果没有则自己实例化一个driver对象；
        2、判断当前浏览器的url地址是不是http网页，如果不是则导航到基地址中
        :param base_driver:
        """
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            # 如果当前访问的浏览器url地址不是http网页，那么将导航到基地址中
            self.driver.get(self._BASE_URL)

    def do_find(self, by, locator=None):
        """
        获取单个元素
        1、如果是单个元素，则直接返回元素定位的结果
        2、如果是元组，则返回元组解包后的结果； 元组解包，例：
            tup = (1, 2, 3)
            a, b, c = tup
            print(a)  # 输出 1
            print(b)  # 输出 2
            print(c)  # 输出 3

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
        获取多个元素
        1、如果是单个元素，则直接返回元素定位的结果
        2、如果是元组，则返回元组解包后的结果；
        :param by:定位方式， 例：By.ID、By.NAME等
        :param locator: 元素节点
        :return: 返回一组符合定位规则的元素节点列表
        """
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        """
        输入框操作
        1、定位到输入框
        2、清除输入框中默认内容
        3、输入内容
        :param value: 输入内容
        :param by:定位方式， 例：By.ID、By.NAME等
        :param locator: 元素节点
        :return:
        """
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def get_screen_shot(self):
        """
        获取截图
        1、获取时间戳
        2、提前创建好截图存放路径image_path
        3、调用selenium生成截图方法，并将截图放到路径中
        4、将截图上传到allure生成的测试报告中
        :return:
        """
        time_tamp = int(time.time())
        image_path = f"./images/image_{time_tamp}.png"
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)

    def wait_element_until_visible(self, locator: tuple):
        """
        封装显示等待，等待条件为一直定位元素
        :param locator: (定位方式，元素节点)
        :return: 返回等待条件为真
        """
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def do_quit(self):
        """
        销毁chrome浏览器进程
        :return:
        """
        self.driver.quit()
