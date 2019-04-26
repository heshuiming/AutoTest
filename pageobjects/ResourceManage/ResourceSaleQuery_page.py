from unit.base_page import BasePage
from time import sleep

#资源搜索
class ResourceSaleQueryPage(BasePage):
    #条件搜索
    phone_input = "name=>telephone"
    student_input = "name=>studentName"
    search_btn = "id=>search"
    def Search(self, **info):
        if info['phone']:
            self.send_keys(self.phone_input, info['phone'])
            self.click(self.search_btn)
        elif info['studentName']:
            self.send_keys(self.student_input,info['studentName'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #查看
    check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def Check(self):
        self.click(self.check_btn)