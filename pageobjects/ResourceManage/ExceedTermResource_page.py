from unit.base_page import BasePage
from time import sleep

#超期资源
class ExceedTermResourcePage(BasePage):
    # 咨询类别
    consultation_1 = "xpath=>//label[contains(text(),'咨询类别')]/../a[@data-serval='1']"  # 雅思
    consultation_2 = "xpath=>//label[contains(text(),'咨询类别')]/../a[@data-serval='2']"  # 北美
    consultation_8 = "xpath=>//label[contains(text(),'咨询类别')]/../a[@data-serval='8']"  # 大客户
    consultation_11 = "xpath=>//label[contains(text(),'咨询类别')]/../a[@data-serval='11']"  # 加拿大留学
    consultation_12 = "xpath=>//label[contains(text(),'咨询类别')]/../a[@data-serval='12']"  # 澳大利亚留学
    def Consultation(self, consultation):
        if consultation == 1:
            self.click(self.consultation_1)
        elif consultation == 2:
            self.click(self.consultation_2)
        elif consultation == 11:
            self.click(self.consultation_11)
        elif consultation == 12:
            self.click(self.consultation_12)
        else:
            print("请给出正确的咨询方向1")

    #资源类型
    source_0 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='0']"  # 客服
    source_1 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='1']"  # 销售
    source_2 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='2']"  # 市场活动
    source_3 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='3']"  # 渠道
    source_4 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='4']"  # TMK
    source_6 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='6']"  # 新媒体
    source_7 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='7']"  # 其他学校
    source_8 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='8']"  # 口碑资源
    source_9 = "xpath=>//label[contains(text(),'来源')]/../a[@data-serval='9']"  # 搜课
    def SourceType(self, source):
        if source == 0:
            self.click(self.source_0)
        elif source == 1:
            self.click(self.source_1)
        elif source == 2:
            self.click(self.source_2)
        elif source == 3:
            self.click(self.source_3)
        elif source == 4:
            self.click(self.source_4)
        elif source == 6:
            self.click(self.source_6)
        elif source == 7:
            self.click(self.source_7)
        elif source == 8:
            self.click(self.source_8)
        elif source == 9:
            self.click(self.source_9)
        else:
            print("请给出正确的来源!")

#资源状态
    source_status_4 = "xpath=>//label[contains(text(),'资源状态')]/../a[@data-serval='4']" #跟进中
    source_status_5 = "xpath=>//label[contains(text(),'资源状态')]/../a[@data-serval='5']" #已过期
    source_status_6 = "xpath=>//label[contains(text(),'资源状态')]/../a[@data-serval='6']" #转公共资源
    def SourceStatus(self,status):
        if status == 4:
            self.click(self.source_status_4)
        elif status == 5:
            self.click(self.source_status_5)
        elif status == 6:
            self.click(self.source_status_6)
        else:
            print("请给出正确的资源状态!")

    #分配时间
    assignTime_0 = "xpath=>//label[contains(text(),'分配时间')]/../a[@data-serval='0']" #本周
    assignTime_1 = "xpath=>//label[contains(text(),'分配时间')]/../a[@data-serval='1']" #本月
    assignTime_3 = "xpath=>//label[contains(text(),'分配时间')]/../a[@data-serval='3']" #自定义时间段
    def AllcationTime(self,assignTime):
        if assignTime == 0:
            self.click(self.assignTime_0)
        elif assignTime == 1:
            self.click(self.assignTime_1)
        elif assignTime == 3:
            self.click(self.assignTime_3)
        else:
            print("请给出正确的分配时间！")

    #条件搜索
    exceedTermDay_input = "name=>exceedTermDay"
    counselorName_input = "name=>counselorName"
    studentName_input = "name=>studentName"
    telephone_input = "name=>telephone"
    search_btn = "id=>search"
    def ConditionSearch(self,**info):
        if info['exceedTermDay']:
            self.send_keys(self.exceedTermDay_input,info['exceedTermDay'])
            self.click(self.search_btn)
        elif info['counselorName']:
            self.send_keys(self.counselorName_input,info['counselorName'])
            self.click(self.search_btn)
        elif info['studentName']:
            self.send_keys(self.studentName_input,info['studentName'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input,info['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #查看
    check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def Check(self):
        self.click(self.check_btn)

    # 分配
    allocation_btn = "xpath=>//td[@datano='0']/button[contains(text(),'分配')]"
    allocation_name_input = "xpath=>//input[@name='nameZh']"
    allocation_search_btn = "xpath=>//div[@class='form-group m-b-5 row search-wrap']/button[contains(text(),'搜索')]"
    allocation_submit_btn = "xpath=>//td[@datano='0']/a[contains(text(),'确定分配')]"
    # 多选分配
    # btn_0 = "xpath=>//input[@value='0']"  # 复选框
    def Allocation(self, **info):
        self.click(self.allocation_btn)
        sleep(1)
        self.send_keys(self.allocation_name_input, info['name'])
        self.click(self.allocation_search_btn)
        sleep(2)
        self.click(self.allocation_submit_btn)
