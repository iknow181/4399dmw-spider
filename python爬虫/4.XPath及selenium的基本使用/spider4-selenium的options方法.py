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
    # 设置手机型号
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    # 使用某个手机型号浏览
    options.add_experimental_option('mobileEmulation', mobileEmulation)

    # 使用静默模式（不跳出浏览器，还去操作）
    options.add_argument('headless')

    # 加代理 http https socks4 socks5
    options.add_argument('--proxy-server="socks4://1.2.3.4:54321"')

    # 更改浏览器语言
    options.add_argument("--lang=en-US")
    # 指定chromedriver路径
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)
    return driver


def main():
    driver = get_driver()
    # 使用get方法打开一个网站
    driver.get('https://www.4399dmw.com/donghua/')
    time.sleep(5)
    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
