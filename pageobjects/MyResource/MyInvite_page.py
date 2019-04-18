from unit.base_page import BasePage
from time import sleep

class MyInvitePage(BasePage):
    #查询条件
    studentName_input = "name=>studentName"
    telephone_input = "name=>telephone"
    search_btn = "id=>search"
    def SearchCondition(self, **info):
        if info['studentName']:
            self.send_keys(self.studentName_input, info['studentName'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input, info['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #跟进状态
    followup_status0 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='0']"  # 新资源
    followup_status1 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='1']"  # 首次回访
    followup_status2 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='2']"  # 跟进
    followup_status3 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='3']"  # 确定学习意向
    followup_status4 = "xpath=>//a[@data-sertype='followupStatus'][@data-serval='4']"  # 确定报名意向
    def FollowupStatus(self, status):
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

    #到访时间
    invitetime0 = "xpath=>//div[@class='pull-left']/a[@data-type='0']" #即将到访
    invitetime1 = "xpath=>//div[@class='pull-left']/a[@data-type='1']" #今天
    invitetime2 = "xpath=>//div[@class='pull-left']/a[@data-type='2']" #本周
    invitetime3 = "xpath=>//div[@class='pull-left']/a[@data-type='3']"#下月
    invitetime4 = "xpath=>//div[@class='pull-left']/a[@data-type='4']"#自定义查询时间
    def InviteTime(self,invitetime):
        if invitetime == 0:
            self.click(self.invitetime0)
        elif invitetime == 1:
            self.click(self.invitetime1)
        elif invitetime == 2:
            self.click(self.invitetime2)
        elif invitetime == 3:
            self.click(self.invitetime3)
        elif invitetime == 4:
            self.click(self.invitetime4)
        else:
            print("请给出正确的到访时间筛选！")

    #到访状态
    invite_status0 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[@data-type='0']"#未到访
    invite_status1 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[@data-type='1']"#已到访
    def InviteStatus(self,status):
        if status == 0:
            self.click(self.invite_status0)
        elif status == 1:
            self.click(self.invite_status1)
        else:
            print("请给出正确的到访状态!")

    #查看
    def Check(self):
        pass

    #删除
    def Delete(self):
        pass

    #确认
    def Confirm(self):
        pass
