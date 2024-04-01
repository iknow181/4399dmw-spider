import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.touch_actions import TouchActions

def get_driver():
    # 指定调用某个地方的chrome
    options = webdriver.ChromeOptions()
    # chromium浏览器的主程序位置
    location = r"D:\study\Python\project\test\chrome-win\chrome.exe"
    # 设置手机型号
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # 指定调用某个地方的chrome
    options = webdriver.ChromeOptions()
    # 使用某个手机型号浏览
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    # 关闭w3c模式！！！非常重要，否则无法点击
    options.add_experimental_option('w3c', False)
    # 在options增加读取位置
    options.binary_location = location
    # 指定chromedriver路径
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    return driver


def main():
    driver = get_driver()
    # 使用get方法打开一个网站
    driver.get('https://www.4399dmw.com/donghua/')
    time.sleep(5)

    # 点击鼠标操作
    action = TouchActions(driver)
    action.tap_and_hold(75, 125).release(75, 125).perform()

    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
