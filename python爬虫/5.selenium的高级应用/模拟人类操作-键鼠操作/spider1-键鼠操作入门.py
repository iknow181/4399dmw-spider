import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 键盘按键包
from selenium.webdriver.common.keys import Keys
# 鼠标按键包
from selenium.webdriver.common.action_chains import ActionChains


def get_driver():
    # 指定调用某个地方的chrome
    options = webdriver.ChromeOptions()
    # chromium浏览器的主程序位置
    location = r"D:\study\Python\project\test\chrome-win\chrome.exe"
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

    # 键盘的组合键使用
    # 组合键输入
    driver.find_element('id', 'j-input').send_keys("AAAAAA")
    driver.find_element('id', 'j-input').send_keys(Keys.CONTROL, 'a')

    # 鼠标移动
    # 移动鼠标的位置
    action = ActionChains(driver).move_by_offset(50, 125).click()
    # 开始执行
    action.perform()
    # 鼠标移动回来并且执行
    ActionChains(driver).move_by_offset('-50', '-125').perform()

    # 鼠标悬停
    # 获取登录的位置，发现一个是link的，文字是text的element对象
    denglu = driver.find_element_by_link_text('登录')
    # 鼠标悬停
    ActionChains(driver).move_to_element(denglu).perform()

    # 鼠标点击的第一种方法
    # 找到logo的位置
    logo = driver.find_element("xpath", "//div[@class='banner_main']/a")
    # 执行点击
    ActionChains(driver).click(logo).perform()
    # 鼠标点击的第二种方法
    # 找到logo的位置
    logo = driver.find_element("xpath", "//div[@class='banner_main']/a")
    denglu = driver.find_element("xpath", "//a[contains(text(),'登录')]")
    # 点击执行
    action = ActionChains(driver).perform()
    action.click(logo)
    time.sleep(2)
    action.click(denglu)
    action.perform()

    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
