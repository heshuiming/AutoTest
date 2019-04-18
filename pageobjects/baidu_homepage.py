# !/usr/bin/python
# -*- coding:utf-8 -*-

""""""
import time
from unit.base_page import BasePage

"""
 页面类，主要存放页面的元素定位和简单的操作函数.
 页面类主要是元素定位和页面操作写成函数，以供测试类使用
 集成 BasePage 二次封装通用类
 通常 1个页面为一个类
"""
# 百度首页类
class BaiduHomePage(BasePage):
    # 百度首页
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"


# --------------------------------------------------------
    # 文本内容输入
    def type_search(self,text):
        # self.find_element(self.input_box)
        self.send_keys(self.input_box,text['search']) # 传递文本框 id 和 内容

    # 按钮点击
    def send_submit_btn(self):
        self.click(self.search_submit_btn) # 传递百度一下按钮 xpath

# --------------------------------------------------------


    # 点击体育新闻入口  百度新闻入口
    sports_link = "link_text=>新闻"
    input_box2 = "id=>ww"
    search_submit_btn2 = "id=>s_btn_wr"

    # 跳转体育新闻界面
    def click_sports_link(self):
        self.click(self.sports_link)
        time.sleep(2)

    # 新闻界面文本框输入
    def new_type_search(self):
        self.clear(self.input_box2)

    # 新闻界面搜索按钮点击
    def new_btn_click(self):
        self.click(self.search_submit_btn2)

# -----------------------------------------------------------



