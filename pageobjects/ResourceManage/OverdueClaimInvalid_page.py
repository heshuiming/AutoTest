from unit.base_page import BasePage
from time import sleep

#无效资源池
class OverdueClaimInvalidPage(BasePage):
    #咨询类别
    consultation_1 = "xpath=>//div[@id='ser-intentionType']/a[@data-sertype='intentionType'][@data-serval='1']"  # 雅思
    consultation_2 = "xpath=>//div[@id='ser-intentionType']/a[@data-sertype='intentionType'][@data-serval='2']"  # 北美
    consultation_8 = "xpath=>//div[@id='ser-intentionType']/a[@data-sertype='intentionType'][@data-serval='8']"  # 大客户
    consultation_11 = "xpath=>//div[@id='ser-intentionType']/a[@data-sertype='intentionType'][@data-serval='11']"  # 加拿大留学
    consultation_12 = "xpath=>//div[@id='ser-intentionType']/a[@data-sertype='intentionType'][@data-serval='12']"  # 澳大利亚留学
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
            print("请给出正确的咨询方向!")

    #来源
    source_type_0 = "xpath=>//a[@data-sertype='source'][@data-serval='0']" #客服
    source_type_1 = "xpath=>//a[@data-sertype='source'][@data-serval='1']" #销售
    source_type_2 = "xpath=>//a[@data-sertype='source'][@data-serval='2']" #市场活动
    source_type_3 = "xpath=>//a[@data-sertype='source'][@data-serval='3']" #渠道
    source_type_4 = "xpath=>//a[@data-sertype='source'][@data-serval='4']" #Tmk
    source_type_6 = "xpath=>//a[@data-sertype='source'][@data-serval='6']" #新媒体
    source_type_7 = "xpath=>//a[@data-sertype='source'][@data-serval='7']" #其他学校
    source_type_8 = "xpath=>//a[@data-sertype='source'][@data-serval='8']" #口碑资源
    source_type_9 = "xpath=>//a[@data-sertype='source'][@data-serval='9']" #搜课
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

    #搜索
    counselorName_input = "name=>counselorName"
    studentName_input = "name=>studentName"
    telephone_input = "name=>contact"
    # pid_input = "name=>pid"
    search_btn = "id=>search"
    def SearchCondition(self,**info):
        if info['counselorName']:
            self.send_keys(self.counselorName_input,info['counselorName'])
            self.click(self.search_btn)
        elif info['studentName']:
            self.send_keys(self.studentName_input,info['studentName'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input,info['telephone'])
            self.click(self.search_btn)
        # elif info['pid']:
        #     self.send_keys(self.pid_input,info['pid'])
        #     self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    # #查看
    # check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    # def Check(self):
    #     self.click(self.check_btn)

    #失效时间
    invilid_time_0 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='0']" #今日
    invilid_time_1 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='1']" #本周
    invilid_time_2 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='2']" #本月
    invilid_time_3 = "xpath=>//a[@data-sertype='timeCycle'][@data-serval='3']" #自定义查询时间
    def InvalidTime(self,time):
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

    #认领
    claim_btn = "xpath=>//td[@datano='0']/button[contains(text(),'认领')]"
    def Claim(self):
        self.click(self.claim_btn)