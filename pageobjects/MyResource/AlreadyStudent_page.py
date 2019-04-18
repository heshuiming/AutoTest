from unit.base_page import BasePage
from time import sleep

class AlreadyStudentPage(BasePage):
    #来源
    source_0 = "xpath=>//a[@data-sertype='source'][@data-serval='0']"  # 客服
    source_1 = "xpath=>//a[@data-sertype='source'][@data-serval='1']"  # 销售
    source_2 = "xpath=>//a[@data-sertype='source'][@data-serval='2']"  # 市场活动
    source_3 = "xpath=>//a[@data-sertype='source'][@data-serval='3']"  # 渠道
    source_4 = "xpath=>//a[@data-sertype='source'][@data-serval='4']"  # TMK
    source_6 = "xpath=>//a[@data-sertype='source'][@data-serval='6']"  # 新媒体
    source_7 = "xpath=>//a[@data-sertype='source'][@data-serval='7']"  # 其他学校
    source_8 = "xpath=>//a[@data-sertype='source'][@data-serval='8']"  # 口碑资源
    source_9 = "xpath=>//a[@data-sertype='source'][@data-serval='9']"  # 搜课
    def Source(self, source):
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

    #条件搜索
    studentName_input = "name=>studentName"
    telephone_input = "name=>telephone"
    search_btn = "id=>search"
    def SearchCondition(self, **info):
        if info['studentName']:
            self.send_keys(self.studentName_input,info['studentName'])
            self.click(self.search_btn)
        elif info['telephone']:
            self.send_keys(self.telephone_input,info['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #查看
    check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def Check(self):
        self.click(self.check_btn)