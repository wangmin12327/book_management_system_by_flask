import time
from time import sleep

import allure
import self
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_select_down():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)  # 打开网址
    driver.get("https://www.taobao.com/")
    # 修改下拉框属性
    sleep(1)
    driver.execute_script('document.querySelector("#J_SiteNavMytaobao").'
                          'className="site-nav-menu site-nav-mytaobao '
                          'site-nav-multi-menu J_MultiMenu '
                          'site-nav-menu-hover"')
    driver.find_element(By.XPATH, "//*[text()='已买到的宝贝']").click()
    sleep(5)
    driver.quit()
