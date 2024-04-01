import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# 键盘按键包
from selenium.webdriver.common.keys import Keys
# 鼠标按键包
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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

    # 拖拽操作
    first_tar = driver.find_element('xpath', '//p[contains(text(),"羊村守护者6之勇闯四季城")]')
    second_tar = driver.find_element('xpath', '//p[contains(text(),"小马宝莉我的可爱标志")]')
    action = ActionChains(driver)
    action.drag_and_drop(first_tar, second_tar).perform()

    # 鼠标点击像素操作
    # 获取原始鼠标位置
    original_position = driver.get_window_position()
    print(original_position)
    # 把鼠标移动到某个特定的地方，然后点击执行
    ActionChains(driver).move_by_offset(400, 400).click().perform()
    # 将鼠标移回原始位置
    ActionChains(driver).move_by_offset(original_position["x"], original_position["y"]).perform()

    # 如果碰到了下拉框
    # 使用select包裹起来xpth查找到的select元素
    select1 = Select(driver.find_element("xpath","//select[@class='year']"))
    # 选择值是1999
    select1.select_by_value("1999")

    # 新建标签页
    js = 'window.open("http://www.baidu.com")'
    driver.execute_script(js)

    # 切换选项卡
    driver.switch_to.window(driver.window_handles[1])
    # 切换到原来的
    driver.switch_to.window(driver.window_handles[0])

    # 看到当前有多少个窗口并且句柄是什么
    print(driver.window_handles)

    # 获取标签下的文字
    res = driver.find_elements("xpath", "//div[@class='u-ct']")
    for i in range(len(res)):
        title = res[i].find_element("xpath", "./p[@class='u-tt']").get_attribute('innerText')
        print(title)

    # 拖动滑块操作
    # 拖动滑块到底部
    js = "document.documentElement.scrollTop=10000"
    driver.execute_script(js)

    # 截图操作
    # 页面截图
    driver.get_screenshot_as_file('./abc.jpg')
    # 指定位置的截图
    pic = driver.find_element("xpath", "//div[@class='lst-item']/a[3]")
    pic.screenshot('./haha.png')

    # 浏览器操作
    # 后退
    driver.back()
    # 刷新
    driver.refresh()
    # 前进
    driver.forward()
    # 浏览器最大化
    driver.maximize_window()

    # 关闭webdriver
    driver.quit()
    pass


if __name__ == '__main__':
    main()
