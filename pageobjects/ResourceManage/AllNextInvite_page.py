from unit.base_page import BasePage
from time import sleep

class AllNextInvitePage(BasePage):
    #查询条件
    studentName_input = "name=>studentName"
    telephone_input = "name=>telephone"
    search_btn = "id=>search"
    def SearchCondition(self,**info):
        if info['studentName']:
            self.send_keys(self.studentName_input,info['studentName'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input,info['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #跟进状态
    followup_status_1 = "xpath=>//label[contains(text(),'跟进状态')]/../a[@data-type='1']" #首次回访
    followup_status_2 = "xpath=>//label[contains(text(),'跟进状态')]/../a[@data-type='2']" #跟进
    followup_status_3 = "xpath=>//label[contains(text(),'跟进状态')]/../a[@data-type='3']" #确定学习意向
    followup_status_4 = "xpath=>//label[contains(text(),'跟进状态')]/../a[@data-type='4']" #确定报名意向
    followup_status_5 = "xpath=>//label[contains(text(),'跟进状态')]/../a[@data-type='5']" #报名成功
    def FollowupStatus(self,status):
        if status == 1:
            self.click(self.followup_status_1)
        elif status == 2:
            self.click(self.followup_status_2)
        elif status == 3:
            self.click(self.followup_status_3)
        elif status == 4:
            self.click(self.followup_status_4)
        elif status == 5:
            self.click(self.followup_status_5)
        else:
            print("请给出正确的跟进状态！")


    #到访时间
    invite_time_0 = "xpath=>//label[contains(text(),'回访时间:')]/../a[@data-type='0']" #今天
    invite_time_1 = "xpath=>//label[contains(text(),'回访时间:')]/../a[@data-type='1']" #本周
    invite_time_2 = "xpath=>//label[contains(text(),'回访时间:')]/../a[@data-type='2']" #下月
    invite_time_3 = "xpath=>//label[contains(text(),'回访时间:')]/../a[@data-type='3']" #自定义查询时间
    invite_time_4 = "xpath=>//label[contains(text(),'回访时间:')]/../a[@data-type='4']" #报名成功
    def InviteTime(self,status):
        if status == 0:
            self.click(self.invite_time_0)
        elif status == 1:
            self.click(self.invite_time_1)
        elif status == 2:
            self.click(self.invite_time_2)
        elif status == 3:
            self.click(self.invite_time_3)
        elif status == 4:
            self.click(self.invite_time_4)
        else:
            print("请给出正确的回访时间！")

    #到访状态
    invite_status_0 = "xpath=>//label[contains(text(),'回访状态:')]/../a[@data-type='0']" #未到访
    invite_status_1 = "xpath=>//label[contains(text(),'回访状态:')]/../a[@data-type='1']" #已到访
    def InviteStatus(self,status):
        if status == 0:
            self.click(self.invite_status_0)
        elif status == 1:
            self.click(self.invite_status_1)
        else:
            print("请给出正确的回访状态")

