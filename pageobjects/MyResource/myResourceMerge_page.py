from unit.base_page import BasePage

#我的资源合并历史
class MyResourceMerge(BasePage):
    #查看
    check_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def Check(self):
        self.click(self.check_btn)
