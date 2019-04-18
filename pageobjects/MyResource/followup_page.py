from unit.base_page import BasePage
from time import sleep

class followup(BasePage):
    #跟进状态
    followup_status0 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='0']" #新资源
    followup_status1 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='1']" #首次回访
    followup_status2 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='2']" #跟进
    followup_status3 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='3']" #确定学习意向
    followup_status4 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='4']" #确定报名意向
    def FollowupStatus(self,status):
        if status == 0:
            self.click(self.followup_status0)
        elif status == 1:
            self.click(self.followup_status1)
        elif status == 2:
            self.click(self.followup_status2)
        elif status == 3:
            self.click(self.followup_status3)
        elif status == 4:
            self.click(self.followup_status4)
        else:
            print("请给出正确的跟进状态！")

    #来源
    source_0 = "xpath=>//a[@data-sertype='source'][@data-serval='0']" #客服
    source_1 = "xpath=>//a[@data-sertype='source'][@data-serval='1']" #销售
    source_2 = "xpath=>//a[@data-sertype='source'][@data-serval='2']" #市场活动
    source_3 = "xpath=>//a[@data-sertype='source'][@data-serval='3']" #渠道
    source_4 = "xpath=>//a[@data-sertype='source'][@data-serval='4']" #TMK
    source_6 = "xpath=>//a[@data-sertype='source'][@data-serval='6']" #新媒体
    source_7 = "xpath=>//a[@data-sertype='source'][@data-serval='7']" #其他学校
    source_8 = "xpath=>//a[@data-sertype='source'][@data-serval='8']" #口碑资源
    source_9 = "xpath=>//a[@data-sertype='source'][@data-serval='9']" #搜课
    def Source(self,source):
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

    #是否延时
    delay_status0 = "xpath=>//a[@data-sertype='delayStatus'][@data-serval='0']" #否
    delay_status1 = "xpath=>//a[@data-sertype='delayStatus'][@data-serval='1']" #是
    def IsDelay(self,delay):
        if delay == 0:
            self.click(self.delay_status0)
        elif delay == 1:
            self.click(self.delay_status1)
        else:
            print("请给出是否延时！")

    #分配时间
    accept_time_start = "xpath=>//label[contains(text(),'分配时间')]/../div[1]/input[1]"
    accept_time_end = "xpath=>//label[contains(text(),'分配时间')]/../div[1]/input[2]"
    def AcceptTime(self,**time):
        self.send_keys(self.accept_time_start)
        self.send_keys(self.accept_time_end)

    #最后跟进时间
    last_time_start = "xpath=>//label[contains(text(),'最后跟进时间')]/../div[1]/input[1]"
    last_time_end = "xpath=>//label[contains(text(),'最后跟进时间')]/../div[1]/input[2]"
    def LastFollowupTime(self):
        self.send_keys(self.last_time_start)
        self.send_keys(self.last_time_end)

    #排序方式
    def SortMode(self):
        pass

    #搜索条件
    studentName_input = "xpath=>//div[@class='form-item']/input[@name='studentName']"
    pid_input = "xpath=>//div[@class='form-item']/input[@name='pid']"
    telephone_input = "xpath=>//div[@class='form-item']/input[@name='telephone']"
    search_btn = "id=>search"
    def SearchCondition(self,**info):
        if info['studentName']:
            self.send_keys(self.studentName_input,info['studentName'])
            self.click(self.search_btn)
        elif info['pid']:
            self.send_keys(self.pid_input,info['pid'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input,info['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #新建资源
    add_new_btn = "xpath=>//button[contains(text(),'新建资源')]"
    new_studentName = "xpath=>//div[@class='col-md-10']/input[@name='studentName']"
    new_telephone = "xpath=>//div[@class='checkValInpWrap pull-left']/input[@name='telephone']"
    verification_tip = "xpath=>//input[@placeholder='咨询类型']" #咨询类型
    ACS_tip = "xpath=>//span[contains(text(),'ACS')]" #咨询类型ACS
    add_btn = "xpath=>//button[contains(text(),'添加')]" #添加按钮
    submit_btn = "xpath=>//button[contains(text(),'确认')]"
    def NewResource(self,**info):
        self.click(self.add_new_btn)
        sleep(1)
        self.send_keys(self.new_studentName,info['studentName'])
        self.send_keys(self.new_telephone,info['telephone'])
        self.click(self.verification_tip)
        sleep(1)
        self.click(self.ACS_tip)
        sleep(1)
        self.click(self.add_btn)
        sleep(1)
        self.click(self.submit_btn)

    #跟进
    followup_btn = "xpath=>//td[@datano='0']/button[contains(text(),'跟进')]"
    def FollowupResource(self):
        self.click(self.followup_btn)
