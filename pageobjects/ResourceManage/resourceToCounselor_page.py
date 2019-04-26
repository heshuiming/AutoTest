from unit.base_page import BasePage
from time import sleep

#再分配
class ResourceToCounselor(BasePage):
    #条件搜索
    phone_input = "name=>telephone"
    student_input = "name=>studentName"
    search_btn = "id=>search"
    def Search(self,**info):
        if info['phone']:
            self.send_keys(self.phone_input,info['phone'])
            self.click(self.search_btn)
        elif info['studentName']:
            self.send_keys(self.student_input,info['studentName'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #分配资源
    checkbox = "xpath=>//tr[@datano='0']/td[2]/input"
    allocation_btn = "id=>allocationOfResources"
    def Allocation(self):
        self.click(self.checkbox)
        sleep(1)
        self.click(self.allocation_btn)

    #查看
    check_btn = "xpath=>//tr[@datano='0']/td[4]/button[2]"
    def Check(self):
        self.click(self.check_btn)
