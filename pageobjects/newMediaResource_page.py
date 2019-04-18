from unit.base_page import BasePage
from time import sleep

class newMediaResourcePage(BasePage):
    #分配情况
    allocation_type_0 = "xpath=>//div[@id='ser-allocation']/a[@data-index='1']" #不可分配
    allocation_type_1 = "xpath=>//div[@id='ser-allocation']/a[@data-index='2']" #待分配
    allocation_type_2 = "xpath=>//div[@id='ser-allocation']/a[@data-index='3']" #分配成功
    def AssignedType(self,type):
        if type == 0:
            self.click(self.allocation_type_0)
        elif type == 1:
            self.click(self.allocation_type_1)
        elif type == 2:
            self.click(self.allocation_type_2)
        else:
            print("请输入正确的分配类型")

    #来源
    origin_type_0 = "pxath=>//div[@id='ser-infomationType']/a[@data-serval='1']" #H5
    origin_type_1 = "pxath=>//div[@id='ser-infomationType']/a[@data-serval='2']" #公众号
    origin_type_2 = "pxath=>//div[@id='ser-infomationType']/a[@data-serval='3']" #微信小助手
    origin_type_3 = "pxath=>//div[@id='ser-infomationType']/a[@data-serval='4']" #QQ
    def Origin(self,originType):
        if originType == 0:
            self.click(self.origin_type_0)
        elif originType == 1:
            self.click(self.origin_type_1)
        elif originType == 2:
            self.click(self.origin_type_2)
        elif originType == 3:
            self.click(self.origin_type_3)
        else:
            print("请输入正确的来源类型")

    search_btn = "id=>search"
    #录入时间
    beginTime = "name=>beginTime"
    endTime = "name=>endTime"
    def EntryTime(self,**time):
        self.send_keys(self.beginTime,time['beginTime'])
        self.send_keys(self.endTime,time['endTime'])
        self.click(self.search_btn)

    #搜索条件
    searchInput_studentName = "xpath=>//div[@class='searchInput']/input[@name='studentName']"
    searchInput_Pid = "xpath=>//div[@class='searchInput']/input[@name='pid']"
    searchInput_wechat = "xpath=>//div[@class='searchInput']/input[@name='wechat']"
    searchInput_telephone = "xpath=>//div[@class='searchInput']/input[@name='telephone']"
    def SearchCondition(self,**searchInput):
        if searchInput['studentName']:
            self.send_keys(self.searchInput_studentName,searchInput['studentName'])
            self.click(self.search_btn)
        elif searchInput['pid']:
            self.send_keys(self.searchInput_Pid,searchInput['pid'])
            self.click(self.search_btn)
        elif searchInput['wechat']:
            self.send_keys(self.searchInput_wechat,searchInput['wechat'])
            self.click(self.search_btn)
        elif searchInput['telephone']:
            self.send_keys(self.searchInput_telephone,searchInput['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)


    #新增
    addNew_btn = "xpath=>//button[contains(text(),'新增')]"
    addInput_student = "xpath=>//div[@class='col-md-8']/input[@name='studentName']"
    addInput_telephone = "xpath=>//div[@class='checkValInpWrap pull-left']/input[@name='telephone']"
    addSubmit_btn = "xpath=>//div[@class='modal-footer']/a[contains(text(),'确认')]"
    def AddNew(self,**addInput):
        self.click(self.addNew_btn)
        sleep(2)
        self.send_keys(self.addInput_student,addInput['studentName'])
        self.send_keys(self.addInput_telephone,addInput['telephone'])
        self.click(self.addSubmit_btn)

    #查看
    check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def Check(self):
        self.click(self.check_btn)