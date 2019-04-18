from unit.base_page import BasePage
from time import sleep

#活动资源导入历史页面
class marketAcyivityImportHistoryPage(BasePage):

    begin_time_input = "name=>beginTime"
    end_time_input = "name=>endTime"
    search_btn = "id=>search"
    def Search(self,beginTime,endTime):
        self.send_keys(self.begin_time_input,beginTime)
        self.send_keys(self.end_time_input,endTime)
        self.click(self.search_btn)
