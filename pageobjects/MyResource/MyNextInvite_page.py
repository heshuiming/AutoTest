from unit.base_page import BasePage
from time import sleep

# 我的回访
class MyNextInvitePage(BasePage):
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
    followup_status0 = "xpath=>//a[contains(text(),'首次回访')]"  # 首次回访
    followup_status1 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'跟进')]"  # 跟进
    followup_status2 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'确定学习意向')]"  # 确定学习意向
    followup_status3 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'确定报名意向')]"  # 确定报名意向
    followup_status4 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'报名成功')]"  #报名成功
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

    #回访时间
    next_invitetime0 = "xpath=>//div[@class='pull-left']/a[@data-type='0']" #即将到访
    next_invitetime1 = "xpath=>//div[@class='pull-left']/a[@data-type='1']" #今天
    next_invitetime2 = "xpath=>//div[@class='pull-left']/a[@data-type='2']" #本周
    next_invitetime3 = "xpath=>//div[@class='pull-left']/a[@data-type='3']"#下月
    next_invitetime4 = "xpath=>//div[@class='pull-left']/a[@data-type='4']"#自定义查询时间
    def InviteTime(self,next_invitetime):
        if next_invitetime == 0:
            self.click(self.next_invitetime0)
        elif next_invitetime == 1:
            self.click(self.next_invitetime1)
        elif next_invitetime == 2:
            self.click(self.next_invitetime2)
        elif next_invitetime == 3:
            self.click(self.next_invitetime3)
        elif next_invitetime == 4:
            self.click(self.next_invitetime4)
        else:
            print("请给出正确的到访时间筛选！")

    #回访状态
    next_invite_status0 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[@data-type='0']"#未到访
    next_invite_status1 = "xpath=>//div[@class='form-group m-b-5 row search-wrap search-click']/a[contains(text(),'已回访')]"#已到访
    def InviteStatus(self,status):
        if status == 0:
            self.click(self.next_invite_status0)
        elif status == 1:
            self.click(self.next_invite_status1)
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
