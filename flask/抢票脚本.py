from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#自定义一个函数
def CSS_SELECTOR_position_method():
#实例化chromedriver对象
    driver = webdriver.Chrome()
#打开网站
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=wf')#强等3秒
    time.sleep(3)
#显示等待
    driver.implicitly_wait(1000)
#通过元素的partial link text 部分文本链接,如果多个元素匹配，则只会选择第一个元素，查找“hao123”选项,并实现点击操作
    driver.find_element(By.CSS_SELECTOR, "#ticket_5l000G483161_02_10 > td.no-br").click()
#强等5秒
    time.sleep(5)

#class_name_position_method()函数作为脚本直接被调用，不能被其他脚本文件调用
if __name__ == '__main__':
    CSS_SELECTOR_position_method()