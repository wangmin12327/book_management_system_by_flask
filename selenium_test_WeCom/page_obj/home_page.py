"""首页，进入通讯录页"""
from time import sleep

import allure
from selenium.webdriver.common.by import By
from page_obj.base_page import BasePage


class HomePage(BasePage):
    """首页点击通讯录，进入到通讯录页"""
    __CONTACTS = (By.XPATH, "//*[text()='通讯录']")

    def go_to_contacts(self):
        """
        点击通讯录，进入到通讯录页
        :return:
        """
        with allure.step("用例步骤1：在首页点击通讯录按钮，进入到通讯录页面，并截图成功"):
            self.webdriver_wait_until_element_find(self.__CONTACTS)
            self.do_find(self.__CONTACTS).click()
            sleep(3)
            self.get_screen_shot()

        from page_obj.contacts_page import Contacts
        return Contacts(self.driver)
