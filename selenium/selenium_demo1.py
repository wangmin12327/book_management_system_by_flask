import logging
import sys

from selenium import webdriver

from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from log_utils import logger


class base:
    """
    基础类：包含使用selenium框架的前置条件和销毁进程
    """

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()


# Demo1: selenium web浏览器控制
def open_browser():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开浏览器，调用get方法时，需要传入url
    driver.get("https://www.ceshiren.com")
    # 等待2秒
    time.sleep(2)

    # 刷新浏览器
    driver.refresh()
    time.sleep(2)

    # 通过get方法，从测试人页面跳转到百度首页
    driver.get("https://www.baidu.com")
    time.sleep(2)

    # 退回到上一步网页,即测试人网页
    driver.back()
    time.sleep(2)

    # 最大化浏览器
    driver.maximize_window()
    time.sleep(5)

    # 最小化浏览器(隐藏网页)
    driver.minimize_window()
    time.sleep(5)


if __name__ == "__main__":
    open_browser()


# Demo2: HTML铺垫
# <a href = "https://ceshiren.com/" class="link">链接</a>
# 标签：<a>
# 属性：<href>
# 类属性：class

# Demo3: selenium 元素定位的格式
#     driver.find_element(By.定位方式, '定位元素对应的值').响应函数()

# Demo4: selenium 通过CLASS_NAME定位
def class_name_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开百度网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的类名CLASS_NAME，查找“新闻(mnav)”选项,并实现点击操作
    driver.find_element(By.CLASS_NAME, 'mnav').click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    class_name_position_method()


# Demo5: selenium 通过CSS_SELECTOR定位
def css_selector_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开百度网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的css选择器表达式，查找“文库(#s-top-left > a:nth-child(8))”选项,并实现点击操作
    driver.find_element(By.CSS_SELECTOR, '#s-top-left > a:nth-child(8)').click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    css_selector_position_method()


# Demo6: selenium 通过id定位
def id_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的id属性值查找“百度一下(su)”按钮,并实现点击操作
    driver.find_element(By.ID, 'su').click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    id_position_method()


# Demo7: selenium 通过LINK_TEXT定位
def link_text_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的link text 文本链接，查找“hao123(hao123)”选项,并实现点击操作
    driver.find_element(By.LINK_TEXT, "hao123").click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    link_text_position_method()


# Demo8: selenium 通过name定位
def name_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的name属性值查找“更多(tj_briicon)”选项,并实现点击操作
    driver.find_element(By.NAME, 'tj_briicon').click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    name_position_method()


# Demo9: selenium 通过PARTIAL_LINK_TEXT定位
def partial_link_text_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的partial link text 部分文本链接,如果多个元素匹配，则只会选择第一个元素，查找“hao123(hao123)”选项,并实现点击操作
    driver.find_element(By.LINK_TEXT, "hao123").click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    partial_link_text_position_method()


# Demo10: selenium 通过TAG_NAME定位
def tag_name_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('https://cn.bing.com/?mkt=zh-cn')
    # 强等3秒
    time.sleep(3)
    # 通过元素的本身标签名称,查找“图片(a)”选项,并实现点击操作
    driver.find_element(By.TAG_NAME, "a").click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    tag_name_position_method()


# Demo11: selenium 通过Xpath定位
def xpath_position_method():
    # 实例化chromedriver对象
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('https://www.baidu.com')
    # 强等3秒
    time.sleep(3)
    # 通过元素的xpath路径，查找“网盘(/html/body/div[2]/div[1]/div[3]/a[7])”选项,并实现点击操作
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[3]/a[7]').click()
    # 强等5秒
    time.sleep(5)


if __name__ == '__main__':
    xpath_position_method()


# Demo12: 强制等待、隐式等待和显示等待
def wait_sleep():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错
    # 报错：no such element: Unable to locate element: {"method":"xpath","selector":"//*[text()='个人中心']"}
    # 原因：页面未加载完成就去查找元素，此时这个元素还没加载出来

    # 解决方案： 在报错位置前添加强制等待 time.sleep()，强制线程休眠
    time.sleep(5)
    # 强制等待的问题： 1、不能确定元素加载的时间，可能会因为等待时间过长影响用例的执行效率
    #               2、不确定元素的加载时间，可能会因为等待时间过短，而导致代码依然会报错

    # 隐式等待解决的问题：难以确定元素加载的具体等待时间。
    # 解决方案：在元素定位之前添加隐式等待 driver.implicitly_wait()
    # 原理：设置一个
    # 隐式等待只能解决元素查找问题，不能解决元素不可交互的问题（不能控制css/js调用过程中花费的这段时间）
    driver.implicitly_wait(5)

    # 显示等待（可以解决元素交互问题, 即能控制css/js调用过程中花费的这段时间）
    # 元素可以找到，但是点击效果没有触发（原因：可能是元素交互出现问题）
    # 页面元素加载为异步加载，通常html先加载，css和js其后
    # 隐式等待只关注元素能不能找到，不关注元素能不能点击或者进行其他的交互
    # WebDriverWait(driver实例,最长等待时间，轮询时间).until(结束条件)
    # 第一个参数是driver,第二个参数是最长等待时间，util方法内需结合expected_conditions或者自己封装的方法进行使用
    # expected_conditions的参数传入的都是一个元组, 即多一个括号()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "success_btn")))
    driver.find_element(By.XPATH, "//*[text()='个人中心']")


if __name__ == '__main__':
    wait_sleep()


# Demo13: selenium 常见控件交互方法
def element_interaction():
    """
    元素的操作， 点击/输入/清空
    :return:
    """
    # 1. 实例化driver类
    driver = webdriver.Chrome()
    # 2. 打开一个网页
    driver.get("https://www.sogou.com/")
    # 3. 定位到输入框进行输入操作
    driver.find_element(By.ID, "query").send_keys("霍格沃茨测试开发")
    # 强制等待2秒
    time.sleep(2)
    # 4. 对输入框清空
    driver.find_element(By.ID, "query").clear()
    time.sleep(2)
    # 5. 再次输入
    driver.find_element(By.ID, "query").send_keys("霍格沃茨测试开发2")
    # 6. 点击搜索
    driver.find_element(By.ID, "stb").click()
    time.sleep(2)


if __name__ == "__main__":
    element_interaction()


# Demo14: selenium 获取元素属性信息
def element_get_attr():
    # 1. 实例化driver
    driver = webdriver.Chrome()
    # 2. 打开网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 3. 定位一个元素对象
    web_element = driver.find_element(By.ID, "locate_id")
    # 4. 打印这个元素的文本信息(text)
    # 断点打在想看的对象的下一行
    print(web_element)
    # 5. 获取元素的文本信息
    # 不是每个元素都含有文本信息的
    print(web_element.text)
    # 6. 获取html元素的属性值(get_attribute)
    res = web_element.get_attribute("class")
    print(res)
    time.sleep(5)


if __name__ == "__main__":
    element_get_attr()


# Demo15: selenium 自动化测试定位策略

# Demo16: selenium css高级定位方式
# 绝对定位( > 表示父子关系，层级关系明确，在定位过程中容易因为前端代码更改而产生定位失败)
# $("#ember63 > td.main-link.clearfix.topic-list-data > span > span > a")

# 相对定位(没有层级关系，可维护性更强，语法简洁)
# $("#ember63 [title='新话题']")
def css_position_method():
    driver = webdriver.Chrome()
    driver.get("https://ceshiren.com/")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".d-button-label").click()
    time.sleep(3)
    webdriver.Chrome().quit()


if __name__ == "__main__":
    css_position_method()


# Demo17: selenium xpath高级定位方式
# 先通过xpath高级定位语法，定位到元素的xpath相对路径，然后结合selenium进行定位
def xpath_position_method():
    driver = webdriver.Chrome()
    driver.get("https://ceshiren.com/")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='d-button-label']").click()
    time.sleep(3)
    webdriver.Chrome().quit()


if __name__ == "__main__":
    xpath_position_method()


# Demo18: selenium 显示等待原理
def web_sleep_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")

    # 注意until(expected_conditions.element_to_be_clickable((...)))此处参数要求为元组类型
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn'))).click()
    webdriver.Chrome().quit()


if __name__ == '__main__':
    web_sleep_until()


# Demo19: selenium 显示等待-封装等待条件
def muliti_click(target_element, next_element):
    """
    封装显示等待的等待条件：
        解决的问题：有的按钮点击一次没有反应，可能要点击多次，比如企业微信的添加成员
        解决的方案：一直点击按钮，直到下个页面出现，封装成显示等待的一个条件
    target_element: 点击的目标按钮
    next_element: 下一个页面的某个元素
    :return:
    """

    def inner(driver):
        driver.find_element(*target_element).click()
        # 结合WebDriverWait函数的源码分析：
        # 1、结果找到了，return 找到的webelement对象
        # 2、结果没找到，return driver.find_element(*next_element) 报错，但是会在until源码中捕获到异常，并抛出异常，
        # 继续循环执行_predicate函数，直到return driver.find_element(*next_element)执行成功
        return driver.find_element(*next_element)

    return inner


def wait_until():
    """
    问题：使用官方提供的expected condition已经无法满足需求
    解决方案：使用自己封装等待条件实现显示等待
    需求：一直点击按钮，直到下一个页面出现为止
    :return:
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    WebDriverWait(driver, 10, 2).until(
        muliti_click((By.ID, "primary_btn"), (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")))
    time.sleep(5)


if __name__ == '__main__':
    wait_until()


# Demo20: 多窗口处理(driver.switch_to.window())
class TestWindows:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_window(self):
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "登录").click()

        print(self.driver.current_window_handle)

        self.driver.find_element(By.LINK_TEXT, "立即注册").click()

        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        time.sleep(5)
        self.driver.find_element(By.NAME, "userName").send_keys("username")
        self.driver.find_element(By.NAME, "phone").send_keys("12345677777")

        time.sleep(5)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.NAME, "userName").send_keys("username")
        self.driver.find_element(By.XPATH, "//*[@id='TANGRAM__PSP_11__password']").send_keys("password")
        self.driver.find_element(By.XPATH, "//*[@id='TANGRAM__PSP_11__isAgree']").click()
        self.driver.find_element(By.XPATH, "//*[@id='TANGRAM__PSP_11__submit']").click()


# Demo21: 多网页frame处理(driver.switch_to.frame())
class TestFrame:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")

    def teardown_method(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element(By.XPATH, "//*[@id='droppable']").text)

        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()

        print(self.driver.find_element(By.XPATH, "//*[@id='submitBTN']").text)


# Demo22: selenium 高级控件交互方法
# 键盘事件: 使用shift实现大小写
# 键盘事件: 输入后回车
# 键盘事件: 复制粘贴
# 鼠标事件: 双击
# 鼠标事件: 拖动元素
# 鼠标事件: 指定位置(例: 悬浮在下拉框的小三角位置处)
# 鼠标事件: 滚轮/滚动操作-滚动到元素

class TestKeyboard:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_shift(self):
        """
        # 键盘事件: 使用shift实现大小写

        1、访问 https://ceshiren.com/
        2、点击搜索按钮
        3、输入搜索的内容，输入的同时按着shift键
        :return:
        """
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # key_down 代表按下某个键位, Keys.SHIFT表示按shift键, ele表示目标元素
        # sendkeys 表示输入内容
        # perform 表示执行此链式操作
        ActionChains(self.driver) \
            .key_down(Keys.SHIFT, ele) \
            .send_keys("selenium") \
            .perform()
        time.sleep(3)

    def test_enter_send_keys(self):
        """
        # 键盘事件: 输入后回车
        :return:
        """
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys("霍格沃茨开发")
        # 第一种回车方式： 定位元素.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
        time.sleep(3)

        # 第二种回车方式：使用ActiChains: key_down(Keys.ENTER)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(3)

    def test_copy_and_paste(self):
        """
        # 键盘事件: 复制粘贴
        1、访问 https://ceshiren.com/
        2、点击搜索按钮
        3、输入搜索的内容，同时按住ctrl键 + shift键 + 左方向键，实现选中光标左边的第一个字符
        4、按住 ctrl键 + c键，实现复制选中的内容， 按住v键，实现粘贴复制的内容
        :return:
        """
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.CSS_SELECTOR, "#search-button").click()
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # 先根据操作系统的类型判断复制功能的键盘事件选哪种：mac(darwin)操作系统, 使用Keys.COMMAND; windos操作系统使用Keys.CONTROL
        command_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        # key_down 代表按下某个键位, Keys.SHIFT表示按shift键, ele表示目标元素
        # sendkeys 表示输入内容
        # Keys.ARROW_LEFT 表示按左方向键，出现几个Keys.ARROW_LEFT，表示光标向左移动几个键位
        # command_control 表示Keys.CONTROL, Ctrl键
        # send_keys("xvvv")  表示x键按一下，v键按三下(即表示剪切一次，粘贴三次)
        # key_up(command_control) 表示松开Ctrl键
        ActionChains(self.driver) \
            .key_down(Keys.SHIFT, ele) \
            .send_keys("selenium") \
            .key_down(Keys.ARROW_LEFT) \
            .key_down(Keys.ARROW_LEFT) \
            .key_down(command_control).send_keys("xvvv").key_up(command_control) \
            .perform()
        time.sleep(3)

    def test_double_click(self):
        """
        # 鼠标事件: 双击
        1、访问 https://vip.ceshiren.com/#/ui_study/frame；
        2、定位到 “点击两次响应”的元素,并赋值给一个元素对象ele；
        3、通过ActionChains实现双击
        :return:
        """
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        ele = self.driver.find_element(By.ID, "primary_btn")
        ActionChains(self.driver).double_click(ele).perform()
        time.sleep(3)

    def test_drag_and_drop(self):
        """
        # 鼠标事件: 拖动元素
        1、访问 https://vip.ceshiren.com/#/ui_study/action_chains；
        2、获取起始元素位置
        3、获取目标元素位置
        4、通过ActiChains实现拖拽操作
        :return:
        """
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        start_ele = self.driver.find_element(By.ID, "item1")
        target_ele = self.driver.find_element(By.ID, "item3")
        ActionChains(self.driver).drag_and_drop(start_ele, target_ele).perform()
        time.sleep(3)

    def test_move_to_element(self):
        """
        # 鼠标事件: 把光标移动到指定位置(例: 悬浮在下拉框的小三角位置处)
        1、访问 https://vip.ceshiren.com/#/ui_study/action_chains2；
        2、定位到目标元素
        3、通过ActionChains实现将光标移动到指定位置的操作
        :return:
        """
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        ele = self.driver.find_element(By.CLASS_NAME, "menu")
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[contains(text(), '测开班')]").click()
        time.sleep(3)

    def test_scroll_to_element(self):
        """
        # 鼠标事件: 滚轮/滚动操作-滚动到元素
        1、访问 https://ceshiren.com/；
        2、定位到目标元素
        3、通过ActionChains实现通过鼠标滚轮滚动到目标元素位置
        :return:
        """
        self.driver.get("https://ceshiren.com/")
        ele = self.driver.find_element(By.XPATH, "//*[@id='ember47']/td[1]/span/a")
        # 第一种方式：通过scroll_to_element(ele)实现
        ActionChains(self.driver).scroll_to_element(ele).perform()
        # 第二种方式：通过scroll_by_amount(ele)实现
        ActionChains(self.driver).scroll_by_amount(0, 3000).perform()
        time.sleep(10)


# Demo22: 文件上传、弹框处理
class TestFileUp(base):
    def test_file_upload(self):
        """
        利用input标签可以直接使⽤send_keys(⽂件地址)上传⽂件的特性，进行本地文件上传
        1、访问 https://pic.sogou.com/
        2、访问文件上传界面
        3、用xpath定位到文件上传的input标签处，直接使⽤send_keys(⽂件地址)方式，上传⽂件
        :return:
        """
        self.driver.get("https://pic.sogou.com/")
        self.driver.find_element(By.CLASS_NAME, "camera-ico").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@accept='image/*']").send_keys(r"D:\开发项目\selenium\1.png")
        time.sleep(3)

    def test_alert(self):
        """
        弹框处理
        1、访问 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        2、操作窗口右侧页面，将元素1拖拽到元素2
        3、点击显示出来的弹框中的"确定"
        4、点击运行
        5、关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')

        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        time.sleep(2)
        print("点击alert 确认")
        self.driver.switch_to.alert.accept()  # 点击弹框中的确认按钮
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        time.sleep(3)


# Demo23: 自动化关键数据记录
# 行为日志记录
# 截图记录
# page source记录
class TestDataRecord:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sogou.com")
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    # def test_log_data(self):
    #     """
    #     # 行为日志记录
    #     1、进入搜狗首页
    #     2、输入霍格沃茨测试开发，进行搜索操作
    #     3、获取搜索结果（对应测试用例的实际结果）
    #     :return:
    #     """
    #     search_content = "霍格沃兹测试开发学社"
    #     self.driver.find_element(By.ID, "query").send_keys(search_content)
    #     logger.debug(f"搜索的信息为{search_content}")
    #     self.driver.find_element(By.ID, "stb").click()
    #     search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
    #     logger.info(f"实际结果为{search_res.text},预期结果为{search_content}")
    #     assert search_res.text == search_content

    def test_screen_data_record(self):
        """
        # 截图记录
        1、进入搜狗首页
        2、输入霍格沃茨测试开发，进行搜索操作
        3、获取搜索结果（对应测试用例的实际结果）
        4、对断言结果截图记录
        :return:
        """
        search_content = "霍格沃兹测试开发学社"
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.ID, "stb").click()
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"实际结果为{search_res.text},预期结果为{search_content}")
        # 截图记录,双重保障
        self.driver.save_screenshot("search_res.png")
        assert search_res.text == search_content

    def test_page_source_data_record(self):
        search_content = "霍格沃兹测试开发学社"
        self.driver.get("https://www.sogou.com/")
        # 获取page_source
        with open("page_source.html", "w", encoding="utf8") as f:
            f.write(self.driver.page_source)
        # 输入霍格沃茨测试开发，进行搜索操作,此处有错误，在报错前添加page_source,获取源码，帮助定位问题
        self.driver.find_element(By.ID, "query1").send_keys(search_content)

