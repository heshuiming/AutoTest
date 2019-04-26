from unit.base_page import BasePage
from time import sleep

#重复用户管理
class ResourceMergePage(BasePage):
    #查询条件
    counselorName_input = "id=>counselorName"
    studentName_input = "id=>studentName"
    telephone_input = "id=>telephone"
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
        else:
            self.click(self.search_btn)

    #合并
    jion_btn = "xpath=>//button[contains(text(),'合并')]"
    def Join(self):
        pass