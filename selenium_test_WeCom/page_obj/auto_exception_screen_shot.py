import os
import time

import allure


def auto_save_exception_screen_shot(func):
    """
        自动保存异常截图
        :return:
        """

    def inner(*args, **kwargs):
        """
        内函数，实现封装处理异常捕获到的代码
        :param args: 不定长参数，是个元组； 其中，args[0] 是实例对象，相当于 self
        :param kwargs:
        :return:
        """
        # 初始化赋值
        try:
            # 当被装饰的函数发生异常，就捕获并保存数据记录
            func(*args, **kwargs)
        except Exception as e:
            print("此处发生了异常")
            driver = args[0].driver
            # 截图
            time_tamp = time.time()
            image_path = f"../test_case/image_path/image_{time_tamp}.png"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            driver.save_screenshot(image_path)
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            # page_source
            time_tamp = time.time()
            page_source_path = f"../test_case/page_source/page_source_{time_tamp}.html"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            ele = driver.current_url
            driver.get(ele)
            with open(page_source_path, "w", encoding="utf8") as f:
                f.write(driver.page_source)
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            # 抛出异常
            raise e

    # 返回内函数对象
    return inner
