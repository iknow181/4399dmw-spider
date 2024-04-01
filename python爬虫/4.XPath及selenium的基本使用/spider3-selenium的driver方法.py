import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


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

    # 根据id找到对应的目标，并且输入什么内容
    driver.find_element('id', "j-input").send_keys("大头")

    # 找到按钮
    driver.find_element("xpath", "//button[@class='banner__btn']").click()

    # 获取当前页面地址（尚未切换标签）
    print(driver.current_url)

    # 获取页面源码
    print(driver.page_source)

    # 获取当前页面cookie
    print(driver.get_cookies())

    # 刷新页面
    driver.refresh()

    # 点击下一页
    driver.find_element("xpath", "//a[contains(text(),'下一页')]").click()

    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
