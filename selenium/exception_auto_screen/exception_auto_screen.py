# 目标1：实现代码异常的时候，截图/打印page_source
# 实现方法：try/catch 配合截图/ page_source操作
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


# ====问题1：异常处理会影响用例本身的结果(本该执行失败的用例，由于捕获了异常，导致执行成功)
# 解决方案： 在exception之后再把异常抛出(raise Exception)
# ====问题2：异常捕获处理代码和业务代码无关，不能耦合
# 解决方案：使用装饰器装饰用例或者相关方法封装异常捕获处理代码
# 1、先把装饰器的架子搭好
# 2、把相关逻辑嵌套进来
# ====问题3： 被装饰的函数test_baidu()还没执行, 就先调用了装饰器ui_exception_record，此时还没有self.driver,导致args[0]还获取不到self
# 解决方案：获取self.driver的操作，放在装饰器中被装饰的函数之后

# ====问题4：隐藏的小bug，一旦被装饰方法有返回值，会丢失返回值
# 解决方案：给被装饰器装饰的方法添加return返回值
def ui_exception_record(func):
    def inner(*args, **kwargs):
        """
        内函数，实现封装异常捕获处理的代码
        :param args: 不定长参数，是个元组，args[0] 是 TestBaidu类的实例对象，相当于self
        :param kwargs:
        :return:
        """
        # 获取TestBaidu类中被装饰方法的self，也就是实例对象,args[0]相当于self，args[0].driver = self.driver
        # 前提条件： TestBaidu类中的driver变量是一个实例变量 self.driver
        try:
            # 当被装饰方法/函数发生异常，就捕获并做数据记录
            func(*args, **kwargs)
        except Exception:
            # ====问题3： 被装饰的函数test_baidu()还没执行, 就先调用了装饰器ui_exception_record，此时还没有self.driver,导致args[0]还获取不到self
            # 解决方案一：获取self.driver的操作，放在装饰器中被装饰的函数func(*args, **kwargs)之后
            driver = args[0].driver
            # 出现异常情况
            # print("出现异常情况")
            # 截图操作
            timestamp = int(time.time())
            image_path = f"../images/image_{timestamp}.PNG"
            driver.save_screenshot(image_path)

            # page_source操作
            page_source_path = f"../page_source/page_source_{timestamp}.HTML"
            with open(page_source_path, "w", encoding="utf8") as f:
                f.write(driver.page_source)

            # 将截图放到allure报告中
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            # 将page_source放到allure报告中
            # 如果想要HTML格式展示在报告中，则使用HTML
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            # 如果想要TEXT格式展示在报告中，则使用TEXT
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)

        # 待截图和page_source数据保存完成后，抛出异常，此时用例会按正常情况，执行失败
        raise Exception

    # 返回内函数对象
    return inner


class TestBaidu:
    def setup_class(self):
        # 解决方案二：在前置条件中对self.driver进行实例化操作
        self.driver = webdriver.Chrome()

    @ui_exception_record
    def find(self):
        return self.driver.find_element(By.ID, "su1")

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.find().click()
        # self.driver.find_element(By.ID, "su1")
