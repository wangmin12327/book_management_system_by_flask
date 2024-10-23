"""通讯录页, 添加成员，获取添加结果"""
from time import sleep

import allure
from selenium.webdriver.common.by import By

from page_obj.base_page import BasePage

from log_utils import logger


class Contacts(BasePage):
    """通讯录页, 添加成员，获取添加结果"""
    __ADD_MEMBER = (By.XPATH, "//*[@class='js_party_info']//*[@class='js_has_member']//*[@class='qui_btn ww_btn "
                              "js_add_member']")
    __NAME = (By.XPATH, "//*[@placeholder='姓名']")
    __ACCOUNT = (By.XPATH, "//*[@placeholder='成员唯一标识，设定以后不支持修改']")
    __BUSINESS_MAIL = (By.ID, "memberAdd_mail")
    __PHONE_NUMBER = (By.ID, "memberAdd_phone")

    # 空格在CSS定位中表示的是后代的关系,在这里 @class 需要把所有的 空格 换成 . ,表示并列关系：
    __SAVE = (By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save")

    __name = (By.XPATH, "//*[@id='member_list']/tr[1]/td[2]")
    __phone_number = (By.XPATH, "//*[@id='member_list']/tr[1]/td[5]")
    __business_mail = (By.XPATH, "//*[@class='member_display_item member_display_item_Email'][2]/*[2]")

    __BACK = (By.XPATH, "//*[@class='ww_commonImg ww_commonImg_Back']")

    __CHECK_BOX = (By.XPATH, "//*[@id='member_list']//tr[1]//td[1]")

    __DEL = (By.XPATH, "//*[@class='qui_btn ww_btn js_delete']")
    __DO_DEL = (By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue']")

    # @auto_save_exception_screen_shot
    def add_member(self, name, account, phone_number, business_mail):
        """
        添加成员
        1、输入姓名、账号、企业邮箱、手机号
        2、截图
        3、点击保存
        :return: 跳转到通讯录页
        """
        with allure.step("用例步骤2：在通讯录页面点击添加成员按钮，进入到添加成员页面，填入成员的 姓名、账号、企业邮箱、手机号，点击保存，并截图和打印page_source"):
            # 点击添加成员按钮,进入到添加成员页面
            self.do_find(self.__ADD_MEMBER).click()
            # 输入姓名、账号、企业邮箱、手机号
            self.webdriver_wait_until_element_find(self.__NAME)
            self.do_send_keys(f"{name}", self.__NAME)
            self.do_send_keys(f"{account}", self.__ACCOUNT)
            self.do_send_keys(f"{phone_number}", self.__PHONE_NUMBER)
            self.do_send_keys(f"{business_mail}", self.__BUSINESS_MAIL)
            # 截图
            self.get_screen_shot()
            # 点击保存，用索引 [0] 表示选择第一个元素
            self.do_finds(self.__SAVE)[0].click()
            # 打印当前结果页面的page_source并截图
            self.get_page_source()
            return Contacts(self.driver)

    def get_add_member_result(self):
        """
        获取添加结果
        1、打印通讯录页面的新增成员姓名，对应手机号
        2、点击进入新增成员详细信息界面
        3、打印详细信息页面的邮箱
        :return:
        """
        add_name = self.do_find(self.__name).text
        sleep(3)
        add_phone_number = self.do_find(self.__phone_number).text
        sleep(3)
        self.do_find(self.__phone_number).click()
        add_business_mail = self.do_find(self.__business_mail).text
        logger.info(f"新增成员的姓名:{add_name}手机号码:{add_phone_number}邮箱:{add_business_mail}")
        return [add_name, add_phone_number, add_business_mail]

    def del_add_member_result(self):
        """
        清除测试数据
        1、点击返回按钮，返回到 Contacts 页面
        2、选中新增成员选项
        3、点击删除按钮
        4、点击提交删除按钮
        :return:
        """
        self.do_find(self.__BACK).click()
        self.do_find(self.__CHECK_BOX).click()
        self.do_finds(self.__DEL)[1].click()
        self.do_find(self.__DO_DEL).click()
        return Contacts(self.driver)
