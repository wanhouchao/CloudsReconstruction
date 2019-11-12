from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction  # 手指点击事件
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Auto_testing_comm_platform.Config.TestEnv import *


class APPIUM:
    def __init__(self, desired_caps):
        '''连接app'''
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


    # def OpenApp(self, desired_caps):
    #     self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #     self.driver.implicitly_wait(5)  # 智能等待
    #     # self.driver.hide_keyboard()  # 隐藏键盘


    def __Find_ele(self, string_ele):
        self.driver.implicitly_wait(5)
        # self.driver.hide_keyboard()  # 隐藏键盘
        if str(string_ele).find('=', 1) == -1:
            raise ('元素的方式错误，无法解析')
        elif str(string_ele).split('=', 1)[0] == 'id':
            try:
                return self.driver.find_element_by_id(str(string_ele).split('=', 1)[1])
            except BaseException as e:
                print(e)
        elif str(string_ele).split('=', 1)[0] == 'xpath':
            try:
                return self.driver.find_element_by_xpath(str(string_ele).split('=', 1)[1])
            except BaseException as e:
                print(e)
        else:
            raise ('元素的方式错误，无法解析')

    def Click(self, string_ele):
        ele=self.__Find_ele(string_ele)
        ele.click()

    def Write(self, string_ele, value):
        ele = self.__Find_ele(string_ele)
        # ele.click()
        # ele.clear()
        ele.send_keys(value)

    def Out(self):
        self.driver.quit()

    def Text_up(self, string_ele):
        ele = self.__Find_ele(string_ele)
        return ele.text

    def TapClick(self, X, Y):
        '''x\y是元素坐标'''
        TouchAction(self.driver).tap(x=X, y=Y).perform()

    def GetSize(self):
        '''获取屏幕的大小'''
        size = self.driver.get_window_size()
        return size

    def allow(self,message):
         # 获取toast提示框内容
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
        print(toast_element.text)
        return toast_element.text

    def SwipeUp(self, t=500, n=1):
        """向上屏幕滑动"""
        size = self.GetSize()
        x1 = size["width"] * 0.5  # x坐标
        y1 = size["height"] * 0.75  # 起点 y坐标
        y2 = size["height"] * 0.25  # 终点 y 坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def SwipeDown(self, t=500, n=1):
        """向下屏幕滑动"""
        size = self.GetSize()
        x1 = size["width"] * 0.5  # x1 坐标
        y1 = size["height"] * 0.25  # 起点y1坐标
        y2 = size["height"] * 0.75  # 终点y2坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def SwipeLeft(self, t=500, n=1):
        """向左屏幕滑动"""
        size = self.GetSize()
        x1 = size["width"] * 0.75  # 起点x1坐标
        y1 = size["height"] * 0.5  # y1 坐标
        x2 = size["width"] * 0.25  # 终点x2坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def SwipeRight(self, t=500, n=1):
        """向右屏幕滑动"""
        size = self.GetSize()
        x1 = size["width"] * 0.25  # 起点x1坐标
        y1 = size["height"] * 0.5  # y1坐标
        x2 = size["width"] * 0.75  # 终点x2坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def OpenApp(self, desired_caps):
        pass


if __name__ == '__main__':
    # desired_caps = {
    #     "platformName": "Android",
    #     "platformVersion": "5.1.1",
    #     "deviceName": "127.0.0.1:21503",
    #     "appActivity": "com.uzmap.pkg.LauncherUI",
    #     "appPackage": "com.tuoluocaijing",
    #     # "unicodeKeyboard": "True",# 使用unicode输入法
    #     # "resetKeyboard": "True",# 重置输入法到初始状态
    #     # "noReset": "True"# 启动app时不要清除app里的原有的数据
    # }
    # desired_caps = {
    #     "platformName": "Android",
    #     "platformVersion": "5.1.1",
    #     "deviceName": "127.0.0.1:21503",
    #     # "appPackage": "com.example.administrator.websc",
    #     "appPackage": "com.tal.kaoyan",
    #     # "appActivity": "com.app.ui.activity.LoginActivity",
    #     "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    #     "unicodeKeyboard": True,
    #     "resetKeyboard": True,
    #     # "noReset": "True"
    # }
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:21503",
        "appPackage": "com.tuoluocaijing",
        "appActivity": "com.uzmap.pkg.LauncherUI",
        # "unicodeKeyboard": 'true',
        # "resetKeyboard": true,
        "noReset": 'true'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.find_element_by_xpath('//*[@text="进入应用"]').click()
    # sleep(3)
    # print(driver.contexts)
    #
    # driver._switch_to.context('NATIVE_APP')
    # print('切换成功')
    # p = driver.page_source
    # with open('1111.html', 'wb') as f:
    #     f.write(p.encode('utf-8'))
    sleep(2)
    driver.find_element_by_xpath('//*[@text="交易所简史，一场暂时看不到尽头的战争"]').click()