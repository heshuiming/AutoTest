import time
import unittest
import csv
from framework.browser_engine import BrowserEngine
from pageobjects.crm_homepage import CrmHomePage
from pageobjects.agentManage_page import agentManagePage
from logs.logger import Logger
from pageobjects.MyResource.AlreadyStudent_page import AlreadyStudentPage
from pageobjects.marketActivityResource_page import MarketActivityResourcePage

logger = Logger(logger="CrmSearch").getlog()
class CrmSearch(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)  # 读取浏览器类型

    def test_case1(self):
        homepage = CrmHomePage(self.driver)
        ASpage = AlreadyStudentPage(self.driver)
        homepage.login(name="heshuiming@pxjy.com",pwd="heshuiming@123") #调用方法，传入用户名和密码
        homepage.login_btn() #调用方法，点击登录按钮
        time.sleep(5)

        homepage.skip_crm() #进入crm
        time.sleep(2)
        #窗口切换
        search_window = self.driver.current_window_handle
        time.sleep(2)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != search_window:
                self.driver.switch_to.window(handle)
                time.sleep(2)
        #点击已成学员
        homepage.alreadyStudent()
        time.sleep(3)
        ASpage.Search("余额-01","") #查询”余额-01“学员
        time.sleep(2)
        ASpage.Check()
        ASpage.get_windows_img()
        try:
            assert "资源详情" in ASpage.get_url_title()
            logger.info("Test Pass")
        except Exception as e:
            logger.info("Test Fial:%s"%e)

    def test_case2(self):
        homepage = CrmHomePage(self.driver)
        # publicPage = publicPraiseResourcePage(self.driver)

        homepage.login(name="heshuiming@pxjy.com",pwd="heshuiming@123") #调用方法，传入用户名和密码
        homepage.login_btn() #调用方法，点击登录按钮
        self.driver.implicitly_wait(10)

        homepage.skip_crm() #进入crm
        self.driver.implicitly_wait(10)
        #窗口切换
        search_window = self.driver.current_window_handle  #获取当前窗口
        time.sleep(2)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != search_window:
                self.driver.switch_to.window(handle)

        self.driver.implicitly_wait(10)
        homepage.MarketActivityResource()
        self.driver.implicitly_wait(10)
        myActivityResourcePage = MarketActivityResourcePage(self.driver)
        myActivityResourcePage.ConditionSearch(name='哈哈',pid='111',mobile='',activityName='',createName='')#传入条件搜索内容
        time.sleep(30)

    def test_case3(self):
        homepage = CrmHomePage(self.driver)
        agentManegePage = agentManagePage(self.driver)
        homepage.login(name='heshuiming@pxjy.com',pwd="heshuiming@123")
        homepage.AgentManager()
        self.driver.implicitly_wait(10)
        agentManegePage.ImportStudent_btn()
        # agentManegePage.ImportStudent()
        time.sleep(5)

    def test_cast4(self):
        homepage = CrmHomePage(self.driver)
        data = csv.reader(open("C://Users//DELL//Desktop//test1.csv", 'r'))
        dict = {}
        for user in data:
            print("-----1-----")
            dict['name'] = user[0]
            dict['pwd'] = user[1]
            # print(dict)
            homepage.login_btn(name=dict['name'],pwd=dict['pwd'])
            # continue
        time.sleep(10)

    def test_case5(self):
        homepage = CrmHomePage(self.driver)
        marketresourcepage = MarketActivityResourcePage(self.driver)
        homepage.login(name="heshuiming@pxjy.com",pwd="heshuiming@123") #登录并跳转
        self.driver.implicitly_wait(30)
        homepage.MarketActivityResource()
        self.driver.implicitly_wait(30)

        data = csv.reader(open("C://Users//DELL//Desktop//test1.csv",'r'))
        dict = {}
        for user in data:
            dict['add_name'] = user[0]
            dict['add_mobile'] = user[1]
            dict['add_activityName'] = user[2]
            marketresourcepage.NewAdd(add_name=dict['add_name'],add_mobile=dict['add_mobile'],add_activityName=dict['add_activityName'])
            self.driver.implicitly_wait(10)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__== '__main__':
    unittest.main()
