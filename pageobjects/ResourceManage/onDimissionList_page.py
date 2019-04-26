from unit.base_page import BasePage
from time import sleep

#离职顾问资源再分配
class DimissionListPage(BasePage):
    #搜索
    counselor_email_input = "xpath=>//input[@placeholder='职员邮箱']"
    search_btn = "id=>search"
    def Search(self,**info):
        self.send_keys(self.counselor_email_input,info['email'])
        self.click(self.search_btn)

    #分配
    distribution_btn = "xpath=>//div[@class='select-btn-list']/button[1]/span[contains(text(),'分配')]"
    checkbox = "xpath=>//tbody/tr[1]/td[1]/div/label"
    def Distribution(self):
        self.click(self.checkbox)
        sleep(1)
        self.click(self.distribution_btn)

    #全部分配
    all_distribution_btn = "xpath=>//div[@class='select-btn-list']/button[2]/span[contains(text(),'全部分配')]"
    allcheckbox = "xpath=>//thead[@class='has-gutter']/tr/th[1]//div[1]/label"
    def AllDistribution(self):
        self.click(self.allcheckbox)
        sleep(1)
        self.click(self.all_distribution_btn)