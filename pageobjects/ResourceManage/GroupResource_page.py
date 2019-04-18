from unit.base_page import BasePage
from time import sleep

class GroupResourcePage(BasePage):
    #咨询类别
    consultation_1 = "xpath=>//label[contains(text(),'咨询类别')]/../a[contains(text(),'雅思')]"  # 雅思
    consultation_2 = "xpath=>//label[contains(text(),'咨询类别')]/../a[contains(text(),'北美')]"  # 北美
    consultation_8 = "xpath=>//label[contains(text(),'咨询类别')]/../a[contains(text(),'大客户')]"  # 大客户
    consultation_11 = "xpath=>//label[contains(text(),'咨询类别')]/../a[contains(text(),'加拿大留学')]"  # 加拿大留学
    consultation_12 = "xpath=>//label[contains(text(),'咨询类别')]/../a[contains(text(),'澳大利亚留学')]"  # 澳大利亚留学
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

    #来源
    source_type_0 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'客服')]" #客服
    source_type_1 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'销售')]" #销售
    source_type_2 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'市场活动')]" #市场活动
    source_type_3 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'渠道')]" #渠道
    source_type_4 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'TMK')]" #Tmk
    source_type_6 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'新媒体')]" #新媒体
    source_type_7 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'其他学校')]" #其他学校
    source_type_8 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'口碑资源')]" #口碑资源
    source_type_9 = "xpath=>//label[contains(text(),'来源')]/../a[contains(text(),'搜课')]" #搜课
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
    counselorName_input = "xpath=>//input[@placeholder='当前负责人']"
    studentName_input = "xpath=>//input[@placeholder='学员姓名']"
    telephone_input = "xpath=>//input[@placeholder='手机号']"
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

    #查看
    check_btn = "xpath=>//tbody/tr[1]/td[2]/div/button"
    def Check(self):
        self.click(self.check_btn)