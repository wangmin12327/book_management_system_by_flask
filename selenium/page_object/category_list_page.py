"""商品列表页"""
from time import sleep
from selenium.webdriver.common.by import By
from log_utils import logger
from page_object.base_page import BasePage


class CategoryListPage(BasePage):
    __CLICK_ADD = (By.XPATH, "//*[@class='el-icon-edit']")
    __TIPS_CREATE = (By.XPATH, "//p[contains(text(),'创建成功')]")
    __TIPS_DEL = (By.XPATH, "//p[contains(text(),'删除成功')]")

    """商品列表页,点击添加"""
    def go_category_add_page(self):
        """
        商品列表页
        1、点击添加按钮,填入商品编号和商品名称
        :return:跳转到商品上架页
        """
        self.do_find(self.__CLICK_ADD).click()
        logger.info("进入商品上架页成功！")

        from page_object.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    def get_category_add_page_result(self):
        """
        商品列表页
        1、获取冒泡消息文本
        :return: 冒泡消息文本
        """
        ele = self.wait_element_until_visible(self.__TIPS_CREATE)
        logger.info(f"冒泡消息是：{ele.text}")
        self.get_screen_shot()
        return "创建成功"

    def delete_category(self, category_num):
        """
        商品列表页，删除商品条目
        1、点击删除按钮，删除商品条目
        :return:跳回到商品列表页
        """
        sleep(3)
        self.do_find(By.XPATH, f"//*[text()='{category_num}']/../..//*[text()='删除']").click()
        return CategoryListPage(self.driver)

    def get_category_del_page_result(self, ):
        """
        商品列表页
        1、获取冒泡消息文本
        :return: 冒泡消息文本
        """
        ele = self.wait_element_until_visible(self.__TIPS_DEL)
        logger.info(f"冒泡消息是：{ele.text}")
        self.get_screen_shot()
        return "删除成功"
