import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.touch_actions import TouchActions


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
    # driver.get('http://192.168.92.129/test/haha.html')
    # driver.get('https://www.4399dmw.com/search/dh-0-0-0-0-0-1-0/')

    time.sleep(5)




    time.sleep(10)
    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
