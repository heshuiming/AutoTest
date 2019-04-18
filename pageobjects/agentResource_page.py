from unit.base_page import BasePage
from time import sleep

#我的代理资源
class agentResourcePage(BasePage):
    #分配情况搜索
    #不可分配
    allocation_0_btn = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'不可分配')]"
    #待分配
    allocation_1_btn = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'待分配')]"
    #分配成功
    allocation_2_btn = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'分配成功')]"
    def Allocation(self,i):
        if i == 0:
            self.click(self.allocation_0_btn) #不可分配
        elif i == 1:
            self.click(self.allocation_1_btn) #待分配
        else:
            self.click(self.allocation_2_btn) #分配成功

    #需要回访搜索
    isNeedCall_0_btn = "xpath=>//a[@data-sertype='isNeedCall'][contains(text(),'否')]" #不需要回访
    isNeedCall_1_btn = "xpath=>//a[@data-sertype='isNeedCall'][contains(text(),'是')]" #需要回访
    def IsNeedCall(self,i):
        if i == 0:
            self.click(self.isNeedCall_0_btn)
        else:
            self.click(self.isNeedCall_1_btn)

    #代理类型搜索
    #录入时间搜索

    #条件搜索
    agent_name_input = "xpath=>//*[@id='searrelAgentIdWrap']/input[@name='agentName']"
    student_name_input = "xpath=>//*[@class='col-md-2 m-r-10']/input[@name='studentName']"
    student_pid_input = "xpath=>//input[@name='pid']"
    student_mobile_input = "xpath=>//input[@placeholder='手机号']"
    search_btn = "xpath=>//button[@id='search']"
    def ConditionSearch(self,**param):
        self.send_keys(self.agent_name_input,param['agentName'])
        self.send_keys(self.student_name_input,param['studentName'])
        self.send_keys(self.student_pid_input,param['studentPid'])
        self.send_keys(self.student_mobile_input,param['studentMobile'])
        self.send_keys(self.search_btn)

    #新增
    add_new_btn = "xpath=>//button[contains(text(),'新增')]"
    add_student_name_input = "xpath=>//input[@placeholder='姓名']"
    add_student_mobile_input = "xpath=>//input[@placeholder='联系方式']"
    add_agent_name_input = "xpath=>//ul[@id='relAgentIdSel']/li[contains(text(),'代理商')]" #代理用户名
    add_submit_btn = "xpath=>//div[@class='modal-footer']/a[contains(text(),'确认')]"
    def AddNew(self,**info):
        self.click(self.add_new_btn)
        self.send_keys(self.add_student_name_input,info['studentName'])
        self.send_keys(self.add_student_mobile_input,info['studentMobile'])
        self.click(self.add_agent_name_input)
        self.click(self.add_submit_btn)

    #设置不可回访
    no_return_visit_btn = "xpath=>//td[@datano='0']/button[contains(text(),'不可回访')]"
    def NoReturnVisit(self):
        self.click(self.no_return_visit_btn)

    #设置可回访
    retuen_visit_btn = "xpath=>//td[@datano='0']/button[contains(text(),'可回访')]"
    def ReturnVisit(self):
        self.click(self.retuen_visit_btn)

    #编辑

    def Edit(self):
        pass

    #删除
    def Delete(self):
        pass