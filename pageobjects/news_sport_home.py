# !/usr/bin/python
# -*- coding:utf-8 -*-

from unit.base_page import BasePage

class NewsSportHome(BasePage):
    # NBA 入口 xpath
    nba_link = "xpath=>//*[@id='channel-submenu']/div/span[2]/a[1]"

    # 跳转 NBA 界面
    def click_nba_link(self):
        self.click(self.nba_link)