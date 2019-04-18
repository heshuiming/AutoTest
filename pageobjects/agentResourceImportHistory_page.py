from unit.base_page import BasePage
from time import sleep

class agentResourceImportHistoryPage(BasePage):
    #搜索
    beginTime_input = "name=>beginTime"
    endTime_input = "name=>endTime"
    search_btn = "id=>search"
    def Search(self,**time):
        if time['beginTime']:
            self.send_keys(self.beginTime_input,time['beginTime'])
            self.click(self.search_btn)
        elif time['endTime']:
            self.send_keys(self.endTime_input,time['endTime'])
            self.click(self.search_btn)
        elif time['beginTime'] and time['endTime']:
            self.send_keys(self.beginTime_input, time['beginTime'])
            self.send_keys(self.endTime_input,time['endTime'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #撤销导入
    cannal_import_btn = "xpath=>//td[@datano='0']/button[contains(text(),'撤销导入')]"
    def CannalImport(self):
        self.click(self.cannal_import_btn)
