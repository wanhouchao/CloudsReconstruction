from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait  # 等待库
from selenium.webdriver.support import expected_conditions as EC  # 等待的条件
from selenium.webdriver.common.by import By  # 元素查找方式精简的写法
from selenium import webdriver


class SeleniumFramework:
    def __init__(self, Type='web', br_name='ge', deviceName='iPhone X'):  # 魔法构建 传入参数
        '''选择浏览器,默认谷歌浏览器，默认iPhone X'''
        # Clear_environment()  # 清理测试环境
        if Type == 'web':
            if br_name in ['google', 'ge', 'chrome']:
                self.driver = webdriver.Chrome()
            elif br_name in ['ff', 'Firefox', 'firefox']:
                self.driver = webdriver.Firefox()
            elif br_name in ['Ie', 'ie']:
                self.driver = webdriver.Ie()
            else:
                self.driver = webdriver.Chrome()
        elif Type == 'wap':
            self.options = webdriver.ChromeOptions()
            mobileEmulation = {'deviceName': deviceName}
            self.options.add_experimental_option('mobileEmulation', mobileEmulation)
            self.driver = webdriver.Chrome(options=self.options)
        else:
            print('兄弟不要瞎玩！！！')

    def Open_url(self, url):
        '''访问网页'''
        self.driver.maximize_window()  # win最大化
        self.driver.get(url)  # 打开url
        # self.driver.minimize_window()
        self.driver.implicitly_wait(5)  # 智能等待5s

    def __Wite_element(self, string_ele):
        """增加框架稳定性  每次操作元素之前都先智能等待一下元素在页面上是否可见"""
        if string_ele.find('=') == -1:
            raise ('元素的方式错误，无法解析！')  # raise手动触发异常
        else:
            # t1 = time.time()
            type = string_ele.split("=", 1)[0]
            element = string_ele.split("=", 1)[1]

            if type.lower() == 'id':
                # WebDriverWait(self.驱动器, 等待时间10).until(EC.visibility_of_element_located可((By.ID, element)))
                # 期望检查一个元素是否存在于页面的dom上，并且是可见的。visibility_of_element_located
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, element)))  # 默认轮询0.5秒
            elif type.lower() == 'name':
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, element)))
            elif type.lower() == 'css':
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            elif type.lower() == 'xpath':
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))
            elif type.lower() == 'class':
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, element)))
            elif type.lower() == 'text':
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, element)))
            else:
                raise ('元素的方式错误，无法解析')
            # print("%s 元素等待%s 秒！" % (string_ele, time.time() - t1))

    def __FindElement(self, string_ele):
        '''分析传入字符串传到对应的方式里面去,找元素
        例如：id name xpyth css  calssname text
        传入形式如：id=user name=pwd xpyth=/hrnl/body/div css=input[type="password"]
        '''
        # 处理传入的字符串 按照=号切割
        # time.sleep(1)
        self.__Wite_element(string_ele)
        if str(string_ele).find('=') == -1:
            raise ('元素输入错误，找不到元素')  # raise 手动出发异常
        else:
            ele_list = str(string_ele).split('=', 1)  # 按照第一个=号切割 例如：['xpyth','/hrnl/body/div']
            # print(ele_list[0])
            if ele_list[0] == 'id':
                return self.driver.find_element_by_id(ele_list[1])
            elif ele_list[0].lower() == 'name':
                return self.driver.find_element_by_name(ele_list[1])
            elif ele_list[0].lower() == 'css':
                return self.driver.find_element_by_css_selector(ele_list[1])
            elif ele_list[0].lower() == 'classname':
                return self.driver.find_elements_by_class_name(ele_list[1])
            elif ele_list[0].lower() == 'xpath':
                return self.driver.find_element_by_xpath(ele_list[1])
            elif ele_list[0].lower() == 'text':
                return self.driver.find_element_by_link_text(ele_list[1])
            else:
                raise ('找不到这个元素')

    def Click(self, string_ele):
        '''点击元素'''
        ele = self.__FindElement(string_ele)
        ele.click()

    def Clear(self, string_ele):
        '''清除输入框中内容'''
        ele = self.__FindElement(string_ele)
        ele.clear()

    def Write(self, string_ele, val):
        '''在输入框写入val'''
        ele = self.__FindElement(string_ele)
        ele.send_keys(val)

    def Switch_to(self, Iframe):
        '''切入框架'''
        self.driver.switch_to.frame(Iframe)

    def Text_up(self, string_ele):
        '''提取文本'''
        ele = self.__FindElement(string_ele)
        return ele.text

    def Roll(self, string_ele):
        '''滚动元素到可视位置'''
        ele = self.__FindElement(string_ele)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def Default_content(self):
        '''退出框架'''
        self.driver.switch_to.default_content()

    def Switch_to_window(self):
        '''切换到最新窗口'''
        win_list = self.driver.window_handles
        self.driver.switch_to.window(win_list[-1])

    def Close_win(self):
        '''关闭当前窗口'''
        self.driver.close()

    def Out(self):
        '''退出浏览器'''
        self.driver.quit()

    def ARROW_UP(self):
        '''滚动条向上输入2个arrow_up'''
        self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_UP)
        self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_UP)

    def NotSelect(self, string_ele_div, string_ele_li):
        '''处理不是Select下拉框'''
        # 找到下拉列表
        self.__Wite_element(string_ele_div)
        ele_div = self.__FindElement(string_ele_div)
        self.ARROW_UP()
        # 点击列表
        ele_div.click()
        # 找到选择的元素
        self.__Wite_element(string_ele_li)
        ele_li = self.__FindElement(string_ele_li)
        # 点击元素
        ele_li.click()
        time.sleep(0.5)

    def SelectVisibleText(self, string_ele, text):
        '''select下拉框处理之文本'''
        ele = self.__FindElement(string_ele)
        Select(ele).select_by_visible_text(text)

    def SelectVisibleIndex(self, string_ele, index):
        '''select下拉框处理之下标'''
        # ele = self.__FindElement(string_ele)
        Select(self.driver.find_element_by_xpath(string_ele)).select_by_index(index)

    def SelectVisibleValue(self, elestring, value):
        '''select下拉框处理之之值'''
        ele = self.__FindElement(elestring)
        Select(ele).select_by_value(value)

    def MouseMove(self, elestring):
        ele = self.__FindElement(elestring)
        ActionChains(self.driver).move_to_element(ele).perform()

    def FindElement(self, string_ele):
        '''分析传入字符串传到对应的方式里面去,找元素
        例如：id name xpyth css  calssname text
        传入形式如：id=user name=pwd xpyth=/hrnl/body/div css=input[type="password"]
        '''
        # 处理传入的字符串 按照=号切割
        # time.sleep(1)
        if str(string_ele).find('=') == -1:
            raise ('元素输入错误，找不到元素')  # raise 手动出发异常
        else:
            ele_list = str(string_ele).split('=', 1)  # 按照第一个=号切割 例如：['xpyth','/hrnl/body/div']
            # print(ele_list[0])
            if ele_list[0] == 'id':
                return self.driver.find_element_by_id(ele_list[1])
            elif ele_list[0].lower() == 'name':
                return self.driver.find_element_by_name(ele_list[1])
            elif ele_list[0].lower() == 'css':
                return self.driver.find_element_by_css_selector(ele_list[1])
            elif ele_list[0].lower() == 'classname':
                return self.driver.find_elements_by_class_name(ele_list[1])
            elif ele_list[0].lower() == 'xpath':
                return self.driver.find_element_by_xpath(ele_list[1])
            elif ele_list[0].lower() == 'text':
                return self.driver.find_element_by_link_text(ele_list[1])
            else:
                raise ('找不到这个元素')

    def Submit(self, elestring):
        ele = self.__FindElement(elestring)
        ele.submit()


if __name__ == '__main__':  # 调试函数，当别人调用本页面时这下面的不会被运行
    # 数据库数据
    sql = "SELECT epsfrontserver.device_rfid_article_record.office_name,epsfrontserver.device_rfid_article_record.article_rfid,epsfrontserver.device_rfid_article_record.article_name ,epsfrontserver.device_rfid_article_record.position_name ,epsfrontserver.device_rfid_article_record.robot_name ,epsfrontserver.device_rfid_article_record.create_date FROM epsfrontserver.device_rfid_article_record WHERE epsfrontserver.device_rfid_article_record.create_date LIKE '2019-09-06%' ORDER BY epsfrontserver.device_rfid_article_record.create_date DESC;"
    db = Mysqldb(epsfrontserverServer, epsfrontserverUser, epsfrontserverPwd, epsfrontserverDatabase)
    MYSQL_data = db.Execute(sql)

    # Clear_environment()  # 清理测试环境
    br = SeleniumFramework()
    br.Open_url(Robot_url)
    # login
    br.Write('css=input[placeholder="用户名"]', Robot_user)
    br.Write('css=input[placeholder="密码"]', Robot_password)
    br.Click('css=button[class="btn btn-primary px-4"]')
    # 点击首页
    br.Click('css=a[href="#/"]')
    # 点击菜单
    br.Click('css=button[class="navbar-toggler sidebar-toggler d-md-down-none"]')
    # 进入机器人管理--》rfid物品管理记录 # print(br.Text_up('xpath=//span[contains(.,"11545")]'))
    br.Click('xpath=//li[contains(.," 机器人管理")]')
    br.Click('css=a[href="#/device/rfidArticleRecord"]')
    # 选择高值耗材医院1号
    br.Click('xpath=//li[contains(.,"高值耗材医院1号")]')
    br.Click('css=select[class="form-control-sm"]')
    br.Click('xpath=//option[contains(.,"50")]')
    # 取数据# 全局路径 print(br.Text_up('xpath=/html/body/div[1]/div/main/div/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]'))
    list = []
    for j in range(1, 51):
        for i in range(2, 13):
            a = br.Text_up('xpath=//table[contains(.,"物品RFID编码")]/tbody/tr[%s]/td[%s]' % (j, i))  # 相对路径
            list.append(a)
    data = CutList(list, 11)
    # print(data)
    list = []
    for i in data:
        list.append(i[0])
        list.append(i[1])
        list.append(i[2])
        list.append(i[3])
        list.append(i[-1])
    web_data = CutList(list, 5)
    print(web_data)
    print(MYSQL_data)
    br.Out()
