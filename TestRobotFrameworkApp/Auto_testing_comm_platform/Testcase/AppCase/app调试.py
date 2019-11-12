from time import sleep
from appium import webdriver
from Auto_testing_comm_platform.Config.TestEnv import *
from appium.webdriver.common.touch_action import TouchAction


class APPIUM:
    def __init__(self, desired_caps):
        '''连接app'''
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # self.driver.hide_keyboard()  # 隐藏键盘

    def __Find_ele(self, string_ele):
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
        self.__Find_ele(string_ele).click()

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

    def GetSize(self):
        '''获取屏幕的大小'''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def SwipeUp(self):
        '''定义向上滑动方法'''
        width, height = self.GetSize()
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.8
        self.driver.swipe(x1, y1, x1, y2)

    def SwipeDown(self):
        '''定义向下滑动方法'''
        width, height = self.GetSize()
        x1 = width * 0.5
        y1 = height * 0.25
        y2 = height * 0.8
        self.driver.swipe(x1, y1, x1, y2)

    def SwipeLeft(self):
        '''定义向左滑动方法'''
        width, height = self.GetSize()
        x1 = width * 0.8
        x2 = width * 0.2
        y1 = height * 0.5
        self.driver.swipe(x1, y1, x2, y1)

    def SwipeRight(self):
        '''定义向右滑动方法'''
        width, height = self.GetSize()
        x1 = width * 0.2
        x2 = width * 0.8
        y1 = height * 0.5
        self.driver.swipe(x1, y1, x2, y1)


if __name__ == '__main__':
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "127.0.0.1:21503",
        # "appPackage": "com.example.administrator.websc",
        "appPackage": "com.tal.kaoyan",
        # "appActivity": "com.app.ui.activity.LoginActivity",
        "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
        # "noReset": "True"
    }

    driver = APPIUM(desired_caps)
    driver.SwipeLeft()
    driver.SwipeLeft()
    driver.SwipeLeft()
    driver.Click('id=com.tal.kaoyan:id/activity_splash_guidfinish')
    driver.Write('id=com.tal.kaoyan:id/login_email_edittext', 'wanhouchao10')
    driver.Write('id=com.tal.kaoyan:id/login_password_edittext', 'qwer1234')
    driver.Click('id=com.tal.kaoyan:id/login_login_btn')
    try:  # 广告弹窗
        driver.Click('id=com.tal.kaoyan:id/view_wemedia_cacel')
    except:
        pass
    sleep(5)
    driver.SwipeUp()
    driver.SwipeUp()
    driver.SwipeUp()
    sleep(5)
    driver.Out()

################################################华丽分割线###############################################################
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# el1 = driver.find_element_by_id("com.example.administrator.websc:id/et_login_account")
# el1.send_keys("robot1")
# el2 = driver.find_element_by_id("com.example.administrator.websc:id/et_login_password")
# el2.send_keys("123456")
# driver.find_element_by_xpath("//*[@text='登录']").click()
# sleep(10)
# driver.find_element_by_xpath("//*[@text='配送']").click()
# driver.find_element_by_xpath("//*[@text='1']").click()
# driver.find_element_by_xpath("//*[@text='2']").click()
# driver.find_element_by_xpath("//*[@text='3']").click()
# driver.find_element_by_xpath("//*[@text='4']").click()
# driver.find_element_by_xpath("//*[@text='1F']").click()
# driver.find_element_by_xpath("//*[@text='5F']").click()
# driver.find_element_by_xpath("//*[@text='充电点']").click()
# driver.find_element_by_xpath("//*[@text='出发']").click()
