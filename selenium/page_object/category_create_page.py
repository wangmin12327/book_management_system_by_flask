"""商品上架页"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from log_utils import logger
from page_object.base_page import BasePage
from test_litemall.web_utils import click_exception


class CategoryCreatePage(BasePage):
    __INPUT_NUMBER = (By.CSS_SELECTOR, "[for='goodsSn']+.el-form-item__content .el-input__inner")
    __INPUT_NAME = (By.CSS_SELECTOR, "[for='name']+.el-form-item__content .el-input__inner")
    __CLICK_UP_LOAD = (By.XPATH, "//*[text()='上架']")
    """商品上架页,填写商品信息"""

    def create_category(self, category_num, category_name):
        """
        商品上架页,填写商品信息
        1、填写“商品编号”
        2、填写“商品名称”
        3、点击“上架”按钮
        :return:跳转到商品列表页
        """
        logger.info("填写商品信息")
        self.do_send_keys(f"{category_num}", self.__INPUT_NUMBER)
        self.do_send_keys(f"{category_name}", self.__INPUT_NAME)
        # 由于这里需要传两个参数：by,element,因此需要对__CLICK_UP_LOAD进行解包，加上*号
        WebDriverWait(self.driver, 10).until(click_exception(*self.__CLICK_UP_LOAD))
        logger.info("跳回到商品列表页")

        from page_object.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
