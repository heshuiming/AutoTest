# !/usr/bin/python
# -*- coding:utf-8 -*-

from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import BaiduHomePage
import unittest

# unittest 之 addTest
class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 初始化访问百度首页
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = BaiduHomePage(self.driver)
        print(homepage)
        title = homepage.get_url_title()
        print(title)








