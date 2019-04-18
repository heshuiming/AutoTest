from unit.base_page import BasePage
from time import sleep

class AgentResourcePage(BasePage):
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
        elif consultation == 8:
            self.click(self.consultation_8)
        elif consultation == 11:
            self.click(self.consultation_11)
        elif consultation == 12:
            self.click(self.consultation_12)
        else:
            print("请给出正确的咨询方向1")

    # 分配情况
    allocation_status_0 = "xpath=>//label[contains(text(),'分配情况')]/../a[@data-serval='0']"  # 待分配
    allocation_status_1 = "xpath=>//label[contains(text(),'分配情况')]/../a[@data-serval='1']"  # 已分配
    allocation_status_2 = "xpath=>//label[contains(text(),'分配情况')]/../a[@data-serval='2']"  # 待领取
    def AllocationStatus(self, status):
        if status == 0:
            self.click(self.allocation_status_0)
        elif status == 1:
            self.click(self.allocation_status_1)
        elif status == 2:
            self.click(self.allocation_status_2)
        else:
            print("请给出正确的分配情况!")

    # 资源状态
    source_status_2 = "xpath=>//label[contains(text(),'资源状态')]/../a[@data-serval='2']"  # 未领取
    source_status_6 = "xpath=>//label[contains(text(),'资源状态')]/../a[@data-serval='6'][@data-delaystatus='0']"  # 领取后未创建销售机会
    source_status_7 = "xpath=>//label[contains(text(),'资源状态')]/../a[@data-serval='6'][@data-delaystatus='1']"  # 延迟后未创建销售机会
    def SourceStatus(self, status):
        if status == 2:
            self.click(self.source_status_2)
        elif status == 6:
            self.click(self.source_status_6)
        elif status == 7:
            self.click(self.source_status_7)
        else:
            print("请给出正确的资源状态!")

    #评级情况
    grade_status_0 = "xpath=>//label[contains(text(),'评级情况')]/../a[@data-serval='0']" #待评级
    grade_status_1 = "xpath=>//label[contains(text(),'评级情况')]/../a[@data-serval='1']" #已评级
    grade_status_8 = "xpath=>//label[contains(text(),'评级情况')]/../a[@data-serval='8']" #转无效
    grade_status_9 = "xpath=>//label[contains(text(),'评级情况')]/../a[@data-serval='9']" #不可评级
    def GradeStatus(self,status):
        if status == 0:
            self.click(self.grade_status_0)
        elif status == 1:
            self.click(self.grade_status_1)
        elif status == 8:
            self.click(self.grade_status_8)
        elif status == 9:
            self.click(self.grade_status_9)
        else:
            print("请给出正确的评级!")

    #代理名称
    agent_name = "xpath=>//input[@placeholder='请选择代理名称']"
    option = "xpath=>//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]"
    def AgentName(self):
        self.click(self.agent_name)
        sleep(2)
        self.click(self.option)
        sleep(1)
        self.click(self.search_btn)

    #录入时间
    begin_time = "xpath=>//input[@name='beginTime']"
    end_time = "xpath=>//input[@name='endTime']"
    search_btn = "id=>search"
    def EnterTime(self,**time):
        self.send_keys(self.begin_time,time['beginTime'])
        self.send_keys(self.end_time,time['endTime'])
        sleep(1)
        self.click(self.search_btn)

    #搜索条件
    studentName_input = "xpath=>//input[@name='studentName']"
    telephone_input = "xpath=>//input[@name='telephone']"
    #pid_input = "xpath=>//label[contains(text(),'搜索条件')]/../div/input[@placeholder='pid']"
    def SearchCondition(self, **info):
        if info['studentName']:
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

    #查看
    check_btn = "xpath=>//div[@class='dt-grid-container']/div[1]/div[3]/table[@border='0']/tbody/tr[1]/td[2]/div[1]/button[1]"
    def Check(self):
        self.click(self.check_btn)

    # 单个分配
    allocation_btn = "xpath=>//td[@datano='0']/button[contains(text(),'分配')]"
    allocation_name_input = "xpath=>//input[@name='nameZh']"
    allocation_search_btn = "xpath=>//div[@class='form-group m-b-5 row search-wrap']/button[contains(text(),'搜索')]"
    allocation_submit_btn = "xpath=>//td[@datano='0']/a[contains(text(),'确定分配')]"
    # 多选分配
    btn_0 = "xpath=>//input[@value='0']"  # 复选框
    def Allocation(self, **info):
        self.click(self.allocation_btn)
        sleep(1)
        self.send_keys(self.allocation_name_input, info['name'])
        self.click(self.allocation_search_btn)
        sleep(2)
        self.click(self.allocation_submit_btn)

    #评级
    grade_btn = "xpath=>//td[@datano='0']/button[4]"
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

    #导出（下载）
    download_btn = "//button[@id='showExportModal']"
    def Download(self):
        self.click(self.download_btn)