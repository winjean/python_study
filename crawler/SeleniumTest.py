#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def openUrl():
    chrome_driver = r"C:\Users\pc\.conda\envs\study\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    options = Options()
    options.add_argument('User-Agent="Mozilla/5.0 '
                         '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/122.0.6253.3 Safari/537.36"')
    browser = webdriver.Chrome(executable_path=chrome_driver, options=options)
    browser.maximize_window()
    browser.get("https://10.20.4.51/ccp-web")

    # 用户名
    username = browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[2]/div/div/input")
    username.send_keys("test")
    sleep(1)

    # 密码
    password = browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[3]/div/div[1]/input")
    password.send_keys("12345678")
    sleep(1)

    # 验证码
    code = browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[2]/div[1]/div[1]/span[1]").text
    code = code + browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[2]/div[1]/div[1]/span[2]").text
    code = code + browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[2]/div[1]/div[1]/span[3]").text
    code = code + browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[2]/div[1]/div[1]/span[4]").text

    mask = browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/div[4]/div[1]/div/div/input")
    mask.send_keys(code)
    sleep(1)

    # 点击提交
    browser.find_element(By.XPATH, "/html/body/div/div/div/div/form/button").click()
    sleep(2)

    el = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/span/a/span[1]")
    ActionChains(browser).move_to_element(el).perform()
    sleep(1)

    browser.find_element(By.XPATH, "/html/body/div/div/div/div/div/ul/li[9]/a").click()
    sleep(50)

    browser.quit()


def main():
    openUrl()


if __name__ == '__main__':
    main()

