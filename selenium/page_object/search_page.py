# 创建新的search_page.py 页面
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Demo26: PageObject设计模式
# 改造前
# class TestSearch:
#     def test_search(self):
#         # 初始化浏览器
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://xueqiu.com/")
#         self.driver.implicitly_wait(3)
#
#         # 输入搜索关键词
#         self.driver.find_element(By.NAME, "q").send_keys("阿里巴巴-sw")
#         # 点击搜索按钮
#         self.driver.find_element(By.CSS_SELECTOR, "i.search").click()
#         # 获取搜索结果
#         name = self.driver.find_element(By.XPATH, "//table/strong").text
#         # 断言
#         assert name == "阿里巴巴-sw"


# 改造后


class SearchPage:
    """
    将元素操作的细节封装到公共方法中
    __SEARCH_INPUT：类属性，搜索输入框元素的属性
    __SEARCH_BUTTON：类属性，搜索按钮元素的属性
    __SPAN_STOCK：类属性，搜索结果列表元素的属性
    """
    __SEARCH_INPUT = (By.NAME, "q")
    __SEARCH_BUTTON = (By.CSS_SELECTOR, "i.search")
    __SPAN_STOCK = (By.XPATH, "//*[text()='阿里巴巴-sw']")

    def __init__(self):
        """
        初始化构造方法
        """
        # 实例化Chromedriver
        self.driver = webdriver.Chrome()
        # 隐式等待3秒
        self.driver.implicitly_wait(3)
        # 访问网页
        self.driver.get("https://xueqiu.com")
        sleep(5)

    def search_stock(self, stock_name: str):
        # 在同一个类中的方法中使用类属性时，需要 类名.类属性
        self.driver.find_element(*self.__SEARCH_INPUT).send_keys(stock_name)
        sleep(3)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        sleep(5)
        ele = self.driver.find_element(*self.__SPAN_STOCK).text
        return ele


