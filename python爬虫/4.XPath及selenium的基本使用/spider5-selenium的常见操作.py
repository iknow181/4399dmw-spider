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



    # 选择多个元素爬取
    for page in range(22):
        print(f'现在开始爬第{page}页')
        res = driver.find_elements("xpath", "//div[@class='lst']/a/div/p")
        for i in range(len(res)):
            print(res[i].text)
        # 点击下一页
        driver.find_element('xpath', '//a[contains(text(), "下一页")]').click()

    # 获取目标元素的html代码
    html = driver.find_element('xpath', '//a[contains(text(),"下一页")]').get_attribute("outerHTML")
    print(html)

    # 获取目标的css属性
    html = driver.find_element('xpath', '//a[contains(text(),"下一页")]').value_of_css_property('backgroud-image')
    print(html)



    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
