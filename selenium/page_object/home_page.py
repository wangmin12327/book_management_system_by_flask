"""首页"""
from time import sleep
from selenium.webdriver.common.by import By
from log_utils import logger
from page_object.base_page import BasePage


class HomePage(BasePage):
    __CLICK_MANAGE = (By.XPATH, "//*[text()='商品管理']")
    __CLICK_LIST = (By.XPATH, "//*[text()='商品列表']")

    """首页"""
    def go_category_List_page(self):
        """
        点击首页按钮，跳转到商品列表页
        1、点击首页按钮，弹出左侧导航栏;
        2、点击商品管理;
        3、点击商品列表;
        :return: 跳转到商品列表页面
        """
        logger.info("进入首页")
        self.do_find(self.__CLICK_MANAGE).click()
        self.wait_element_until_visible(self.__CLICK_LIST)
        self.do_find(self.__CLICK_LIST).click()
        sleep(3)
        logger.info("进入商品列表页面成功！")

        from page_object.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
