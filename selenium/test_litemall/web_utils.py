"""封装一直点击的显示等待条件"""
from log_utils import logger


def click_exception(by, element, max_attempts=5):
    def _inner(driver):
        # 多次点击按钮
        actul_attempts = 0  # 实际点击次数
        while actul_attempts < max_attempts:
            actul_attempts += 1
            # 进行点击操作
            try:
                # 如果点击报错，则直接执行except逻辑，并且继续循环
                # 如果没有报错，则直接return循环结束
                driver.find_element(by, element).click()
                return True

            except Exception:
                logger.debug("点击时出现了一次异常")

    return _inner
