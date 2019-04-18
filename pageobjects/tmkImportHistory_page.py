from unit.base_page import BasePage
from time import sleep

class tmkImportHistoryPage(BasePage):
    #录入时间
    search_btn = "id=>search"
    beginTime = "name=>beginTime"
    endTime = "name=>endTime"
    def EntryTime(self,**time):
        self.send_keys(self.beginTime,time['beginTime'])
        self.send_keys(self.endTime,time['endTime'])
        self.click(self.search_btn)