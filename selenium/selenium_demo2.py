# Demo24: 复用浏览器
import time
from time import sleep

import allure
import self
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""
复用浏览器
1、实例化Options()
2、修改实例option属性为 debug 模式启动 ip+端口
3、实例化 driver，需添加 option 配置
:return:
"""


# # 定义配置的实例对象option
# option = Options()
# # 修改实例属性为 debug 模式启动的 ip+端口
# option.debugger_address = "localhost:9222"
# # 实例化 driver ，需添加 option 配置
# driver = webdriver.Chrome(options=option)
# # 访问企业微信
# driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
# # 点击添加成员的操作, 当此处出现问题需要调试时，不需要重新打开浏览器
# driver.find_element(By.XPATH, "//*[text()='添加成员']").click()
# sleep(3)
# # 添加成员姓名, 当此处出现问题需要调试时，不需要重新打开浏览器
# driver.find_element(By.XPATH, "//*[@class='ww_compatibleTxt_ipt' and @name='username']").send_keys('123')


# Demo25: cookie复用
# cookie: 用户身份信息保持
# class TestCookieLogin:
#     def setup_class(self):
#         """
#         前置条件：实例化Chromedriver
#         :return:
#         """
#         # 实例化Chromedriver
#         self.driver = webdriver.Chrome()
#
#     def test_get_cookies(self):
#         """
#         获取cookie信息，并且存入到本地
#         1、访问登录页
#         2、等登录成功后再获取cookie信息
#         3、将cookie信息存入一个可持久化存储的地方（文件or数据库）
#         :return:
#         """
#         # 访问企业微信登录页
#         self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
#         # 等待20秒，人工扫码操作
#         sleep(20)
#         # 等成功登陆后，获取cookie信息
#         cookie = self.driver.get_cookies()
#         print(cookie)
#         # 将cookie存入一个可持久存储的地方：文件或者数据库
#         # 打开文件的时候添加写入权限
#         with open("cookie.yaml", "w", encoding="utf8") as f:
#             # 第一个参数是要写入的数据
#             yaml.safe_dump(cookie, f)
#
#     def test_add_cookie(self):
#         """
#         植入cookie信息，不扫码也能直接登录界面
#         1、访问登录页：https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome
#         2、从本地保存的cookie信息导出
#         3、植入cookie到driver实例对象中
#         4、无需扫码也能自动登录成功
#         :return:
#         """
#         # 访问企业微信主页面
#         self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
#         # 定义cookie，cookie信息从已经写入的cookie文件中获取
#         cookie = yaml.safe_load(open("cookie.yaml"))
#         # 植入cookie
#         for c in cookie:
#             self.driver.add_cookie(c)
#         time.sleep(3)
#         # 再次访问企业微信页面，就无需扫码，自动登陆
#         self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")


# Demo 26: PageObject设计模式

# Demo 27: 异常自动截图
def ui_exception_record(func):
    def inner(*args, **kwargs):
        try:
            # 当整个被装饰方法/函数发生异常就被捕获并作数据记录
            func(*args, **kwargs)
        except:
            # 出现异常的处理
            print("出现异常啦")
            # 截图操作
            timestamp = int(time.time())
            # 提前创建好 images 路径
            image_path = f"./images/image_{timestamp}.PNG"
            # 截图
            self.driver.save_screenshot(image_path)
            # 将截图放到报告的数据中
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)

            # 提前创建好 page_source 路径
            timestamp = int(time.time())
            page_source_path = f"./page_source/page_source_{timestamp}.HTML"
            # 记录 page_source
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(self.driver.page_source)
            # 将 page_source 放到报告的数据中,如果想要 html源码格式 使用 text, 如果想要 网页格式 就用 html
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            # 将异常给抛回去
            raise Exception

    return inner


class TestBaidu:
    @ui_exception_record
    def test_baidu(self):
        """
        1、实现代码异常时，截图/打印page_source
        实现方法： try catch 配合截图/ page_source操作

        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "su1")

        self.driver.quit()
