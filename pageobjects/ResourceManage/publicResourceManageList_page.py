from unit.base_page import BasePage
from  time import sleep

#公共资源池管理
class PublicResourceManageListPage(BasePage):
    # 咨询类别
    consultation_1 = "xpath=>//label[contains(text(),'咨询类型')]/../a[contains(text(),'雅思')]"  # 雅思
    consultation_2 = "xpath=>//label[contains(text(),'咨询类型')]/../a[contains(text(),'北美')]"  # 北美
    consultation_8 = "xpath=>//label[contains(text(),'咨询类型')]/../a[contains(text(),'大客户')]"  # 大客户
    consultation_11 = "xpath=>//label[contains(text(),'咨询类型')]/../a[contains(text(),'加拿大留学')]"  # 加拿大留学
    consultation_12 = "xpath=>//label[contains(text(),'咨询类型')]/../a[contains(text(),'澳大利亚留学')]"  # 澳大利亚留学
    def Consultation(self, consultation):
        if consultation == 1:
            self.click(self.consultation_1)
        elif consultation == 2:
            self.click(self.consultation_2)
        elif consultation == 8:
            self.click(self.consultation_8)
        elif consultation == 11:
            self.click(self.consultation_11)
        elif consultation == 12:
            self.click(self.consultation_12)
        else:
            print("请给出正确的咨询方向！")

    # 来源
    source_type_0 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'客服')]"  # 客服
    source_type_1 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'销售')]"  # 销售
    source_type_2 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'市场活动')]"  # 市场活动
    source_type_3 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'渠道')]"  # 渠道
    source_type_4 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'TMK')]"  # Tmk
    source_type_6 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'新媒体')]"  # 新媒体
    source_type_7 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'其他学校')]"  # 其他学校
    source_type_8 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'口碑资源')]"  # 口碑资源
    source_type_9 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'搜课')]"  # 搜课
    def Source(self, type):
        if type == 1:
            self.click(self.source_type_0)
        elif type == 2:
            self.click(self.source_type_1)
        elif type == 3:
            self.click(self.source_type_2)
        elif type == 4:
            self.click(self.source_type_3)
        elif type == 5:
            self.click(self.source_type_4)
        elif type == 6:
            self.click(self.source_type_6)
        elif type == 7:
            self.click(self.source_type_7)
        elif type == 8:
            self.click(self.source_type_8)
        elif type == 9:
            self.click(self.source_type_9)
        # elif type == 10:
        #     self.click(self.infomationType_10)
        # elif type == 11:
        #     self.click(self.infomationType_11)
        else:
            print("请给出正确的来源")

    #评级情况
    grade_type_0 = "xpath=>//label[contains(text(),'评级情况')]/../a[contains(text(),'待评级')]"
    grade_type_1 = "xpath=>//label[contains(text(),'评级情况')]/../a[contains(text(),'已评级')]"
    grade_type_8 = "xpath=>//label[contains(text(),'评级情况')]/../a[contains(text(),'转无效')]"
    grade_type_9 = "xpath=>//label[contains(text(),'评级情况')]/../a[contains(text(),'不可评级')]"
    def Grade(self,type):
        if type == 0:
            self.click(self.grade_type_0)
        elif type == 1:
            self.click(self.grade_type_1)
        elif type == 8:
            self.click(self.grade_type_8)
        elif type == 9:
            self.click(self.grade_type_9)
        else:
            print("请给出正确的评级！")

    #失效时间
    invilid_time_0 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='0']"  # 今日
    invilid_time_1 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='1']"  # 本周
    invilid_time_2 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='2']"  # 本月
    invilid_time_3 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='3']"  # 自定义查询时间
    def InvalidTime(self, time):
        if time == 0:
            self.click(self.invilid_time_0)
        elif time == 1:
            self.click(self.invilid_time_1)
        elif time == 2:
            self.click(self.invilid_time_2)
        elif time == 3:
            self.click(self.invilid_time_3)
        else:
            print("请给出正确的时间!")

    # 搜索
    counselorName_input = "xpath=>//input[@placeholder='前负责人']"
    studentName_input = "xpath=>//input[@placeholder='学员姓名']"
    telephone_input = "xpath=>//input[@placeholder='手机号码']"
    # pid_input = "name=>pid"
    search_btn = "id=>search"
    def SearchCondition(self, **info):
        if info['counselorName']:
            self.send_keys(self.counselorName_input, info['counselorName'])
            self.click(self.search_btn)
        elif info['studentName']:
            self.send_keys(self.studentName_input, info['studentName'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input, info['telephone'])
            self.click(self.search_btn)
        # elif info['pid']:
        #     self.send_keys(self.pid_input,info['pid'])
        #     self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    # 查看
    check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def Check(self):
        self.click(self.check_btn)

    #分配
    allocation_btn = "xpath=>//td[@datano='0']/button[contains(text(),'分配')]"
    allocation_name_input = "xpath=>//input[@name='nameZh']"
    allocation_search_btn = "xpath=>//div[@class='form-group m-b-5 row search-wrap']/button[contains(text(),'搜索')]"
    allocation_submit_btn = "xpath=>//td[@datano='0']/a[contains(text(),'确定分配')]"
    # 多选分配
    #btn_0 = "xpath=>//input[@value='0']"  # 复选框
    def Allocation(self, **info):
        self.click(self.allocation_btn)
        sleep(1)
        self.send_keys(self.allocation_name_input, info['name'])
        self.click(self.allocation_search_btn)
        sleep(2)
        self.click(self.allocation_submit_btn)

    #评级
    grade_btn = "xpath=>//td[@datano='0']/button[contains(text(),'评级')]"
    option_value_1 = "xpath=>//select[@id='level']/option[@value='1']" #A级
    option_value_2 = "xpath=>//select[@id='level']/option[@value='2']" #B级
    option_value_3 = "xpath=>//select[@id='level']/option[@value='3']"#C级
    option_value_4 = "xpath=>//select[@id='level']/option[@value='4']"#D级
    option_value_5 = "xpath=>//select[@id='level']/option[@value='5']"#E级
    option_value_8 = "xpath=>//select[@id='level']/option[@value='8']"#无效
    def Drade(self,value):
        self.click(self.grade_btn)
        sleep(2)
        if value == 1:
            self.click(self.option_value_1)
        elif value == 2:
            self.click(self.option_value_2)
        elif value == 3:
            self.click(self.option_value_3)
        elif value == 4:
            self.click(self.option_value_4)
        elif value == 5:
            self.click(self.option_value_5)
        elif value == 8:
            self.click(self.option_value_8)
        else:
            print("请给出正确的评级！")