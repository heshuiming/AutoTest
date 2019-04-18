# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
import unittest
from  framework.browser_engine import BrowserEngine
from logs.logger import Logger

logger = Logger(logger="BaiduSearch").getlog()

class BaiduSearch(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserEngine(self)
        self.driver = self.browser.open_browser(self)

    def tearDown(self):
        logger.info("Now,Close and quit the browser.")
        # print(self.driver)
        self.driver.quit()

    def test_baidu_search(self):
        try:
            self.driver.find_element_by_id("kw").send_keys("selenium")
            self.driver.find_element_by_id("su").click()
            logger.info("baidu send_keys selenium")
            assert 'selenium' in self.driver.title
            logger.info("OK")
        except Exception as e:
            logger.info("Test Fail:%s" % format(e))

if __name__ == '__main__':
    unittest.main()