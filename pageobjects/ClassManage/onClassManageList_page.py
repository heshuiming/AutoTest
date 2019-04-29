from unit.base_page import BasePage
from time import sleep

#教务-班级管理
class OnClassManageList(BasePage):
    #上课形式
    isOnLine_0 = "xpath=>//div[@id='isOnlineWrap']/a[@data-sertype='isOnline'][@data-serval='0']" #线下课
    isOnLine_1 = "xpath=>//div[@id='isOnlineWrap']/a[@data-sertype='isOnline'][@data-serval='1']" #线上课
    def IsOnlineWrap(self,is_online):
        if is_online == 0:
            self.click(self.isOnLine_0)
        elif is_online == 1:
            self.click(self.isOnLine_1)
        else:
            print("请给出上课形式！")

    #所属校区
    schoolAreaId_127 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='127']" #魏公村
    schoolAreaId_128 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='128']"#天作校区
    schoolAreaId_129 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='129']"#新中关村校区
    schoolAreaId_130 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='130']"#中关村校区
    schoolAreaId_131 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='131']"#公主坟校区
    schoolAreaId_132 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='132']"#五道口校区
    schoolAreaId_133 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='133']"#国贸校区
    schoolAreaId_134 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='134']"#崇文门校区
    schoolAreaId_135 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='135']"#外经贸校区
    schoolAreaId_136 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='136']"#三元桥校区
    schoolAreaId_137 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='137']"#通州校区
    schoolAreaId_176 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='176']"#朝阳校区
    schoolAreaId_242 = "xpath=>//div[@id='serSchoolWrap']/a[@data-serval='242']"#测试删除校区
    def SerSchoolWrap(self,schoolAreaId):
        if schoolAreaId == 127:
            self.click(self.schoolAreaId_127)
        elif schoolAreaId == 128:
            self.click(self.schoolAreaId_128)
        elif schoolAreaId == 129:
            self.click(self.schoolAreaId_129)
        elif schoolAreaId == 130:
            self.click(self.schoolAreaId_130)
        elif schoolAreaId == 131:
            self.click(self.schoolAreaId_131)
        elif schoolAreaId == 132:
            self.click(self.schoolAreaId_132)
        elif schoolAreaId == 133:
            self.click(self.schoolAreaId_133)
        elif schoolAreaId == 134:
            self.click(self.schoolAreaId_134)
        elif schoolAreaId == 135:
            self.click(self.schoolAreaId_135)
        elif schoolAreaId == 136:
            self.click(self.schoolAreaId_136)
        elif schoolAreaId == 137:
            self.click(self.schoolAreaId_137)
        elif schoolAreaId == 176:
            self.click(self.schoolAreaId_176)
        elif schoolAreaId == 242:
            self.click(self.schoolAreaId_242)
        else:
            print("请给出正确的所属校区！")