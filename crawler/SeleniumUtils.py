#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# 声明浏览器
# 字符串前加上r告诉编译器不要进行转义操作
chrome_driver = r"D:\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
options = Options()

options.add_argument('User-Agent="Mozilla/5.0 '
                     '(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/74.0.3729.169 Safari/537.36"')
# options.add_argument('--headless')   # 无界面化.
# options.add_argument('--disable-gpu')    # 配合上面的无界面化.
options.add_argument('--start-maximized')   # 设置窗口大小, 窗口大小会有影响.
# options.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
browser = webdriver.Chrome(executable_path=chrome_driver, options=options)
browser.maximize_window()


url = 'http://10.20.4.61:8080/isnp-web/#/login'
# url = 'http://10.20.4.61:8080/isnp-web/#/dashboardSub'
# 打开浏览器预设网址
browser.get(url)
browser.execute_script('sessionStorage.setItem("Isnp-Token","eyJhbGciOiJIUzI1NiJ9.'
                       'eyJqdGkiOiJCMDgxMEUyMTlEMkE0MzhDQUMzMjJGNzg3NTZFRTE0QyIsInN1YiI6IntcInVpZFwiOlwiMVwiLFwibmFtZ'
                       'VwiOlwiYWRtaW5cIixcInVuaXRJZFwiOlwiMVwifSIsImlhdCI6MTU5MDY0MjgzOH0.'
                       'CelgZ6UsaU5bDpZVcDWW9ncxMMhrcysym_heHTmsGps");')
browser.refresh()


# inputs = browser.find_elements_by_class_name('el-input__inner')
# print(type(inputs))
# inputs[0].send_keys("admin")
# inputs[1].send_keys("123456")
# 发送controller键
# inputs[0].send_keys(Keys.CONTROL, "c")

# 创建动作链对象.
# click(on_element=None) : 左键单击传入的元素，如果不传入的话，点击鼠标当前位置。
# context_click(on_element=None): 右键单击。
# double_click(on_element=None) : 双击。
# click_and_hold(on_element=None): 点击并抓起
# drag_and_drop(source, target) : 在source元素上点击抓起，移动到target元素上松开放下。
# drag_and_drop_by_offset(source, xoffset, yoffset):在source元素上点击抓起，移动到相对于source元素偏移xoffset和yoffset的坐标位置放下。
# send_keys(*keys_to_send): 将键发送到当前聚焦的元素。
# send_keys_to_element(element, *keys_to_send): 将键发送到指定的元素。
# reset_actions(): 清除已经存储的动作

# actions = ActionChains(browser)
# 在element元素上点击抓起，移动到target元素上松开放下。 类似鼠标.
# actions.drag_and_drop(element, target)
# 执行动作.
# actions.perform()


# print(browser.page_source)

sleep(10)

# 关闭浏览器当前窗口
# browser.close()

# 退出webdriver并关闭所有窗口
browser.quit()

