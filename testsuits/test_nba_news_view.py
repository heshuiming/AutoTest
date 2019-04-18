# !/usr/bin/python
# -*- coding:utf-8 -*-

from pageobjects.news_sport_home import NewsSportHome
from pageobjects.baidu_homepage import BaiduHomePage
from framework.browser_engine import BrowserEngine
from logs.logger import Logger
import time
import unittest

logger = Logger(logger="ViewNBANews").getlog()

# 百度新闻、NBA 实现类
class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self) # 赋值浏览器对象
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit() # 退出浏览器

    def test_view_nba_views(self):
        try:
            # 初始化百度首页，并点击新闻链接
            baiduhome = BaiduHomePage(self.driver) # 百度首页界面实例化
            baiduhome.click_sports_link()
            logger.info("baiduNewHome Journalism")
            assert "百度新闻——全球最大的中文新闻平台" in self.driver.title
            logger.info("OK")
            baiduhome.new_type_search("selenium")
            baiduhome.new_btn_click()
        except Exception as e:
            logger.error("baiduNewHome Error:%s" %e)


if __name__ == '__main__':
    unittest.main()

