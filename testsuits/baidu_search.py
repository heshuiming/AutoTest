# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
import csv
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomePage
from logs.logger import Logger
# 实现类
logger = Logger(logger="BaiduSearch").getlog()
class BaiduSearch(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self) # 读取浏览器类型

    def tearDown(self):
        self.driver.quit()

    # 百度查询：selenium
    def test_baidu_search(self):
        try:
            homepage = BaiduHomePage(self.driver)
            homepage.type_search("selenium")  # 调用方法，向文本框输入内容
            homepage.send_submit_btn()  # 调用方法，点击页面按钮
            time.sleep(2)
            homepage.get_windows_img()
            try:
                assert "selenium" in homepage.get_url_title() # 调用页面对象继承基类中的获取页面标题方法
                logger.info("Test Pass")
            except Exception as e:
                logger.error("Test Fail:%s" % e)
        except Exception as e:
            logger.error("Test Fail:%s" %e)
            # 百度查询：python

    def test_baidu_search2(self):
        try:
            homepage = BaiduHomePage(self.driver)
            homepage.type_search("python")  # 调用方法，输入文本
            homepage.send_submit_btn()  # 调用方法，点击按钮
            time.sleep(2)
            homepage.get_windows_img()
            try:
                assert "python" in homepage.get_url_title()  # 调用页面对象继承基类中的获取页面标题方法
                logger.info("Test Pass")
            except Exception as e:
                logger.error("Test Fail:%s" % e)
        except Exception as e:
            logger.error("Test Fail:%s" % e)

    def test_baidu_search3(self):
        global search_add
        homepage = BaiduHomePage(self.driver)
        search_list = csv.reader(open("C://Users//DELL//Desktop//test_data.txt",'r'))
        for search_word in search_list:
            search_add = {'search' : search_word[0]}

        homepage.type_search(search_add)
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_img()

if __name__ == '__main__':
    unittest.main()



