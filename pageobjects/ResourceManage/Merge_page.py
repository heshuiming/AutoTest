from unit.base_page import BasePage

class MergePage(BasePage):
    #查询条件
    counselorName_input = "name=>counselorName"
    studentName_input = "name=>studentName"
    search_btn = "id=>search"
    def SearchCondition(self,**info):
        if info['counselorName']:
            self.send_keys(self.counselorName_input,info['counselorName'])
            self.click(self.search_btn)
        elif info['studentName']:
            self.send_keys(self.studentName_input,info['studentName'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)