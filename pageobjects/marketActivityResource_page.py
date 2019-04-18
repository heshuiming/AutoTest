from unit.base_page import BasePage
from time import sleep

#我的活动资源
class MarketActivityResourcePage(BasePage):

    #条件搜索
    name_input = "xpath=>//div[@class='form-group m-b-5 search-wrap search-resize']/div[@class='col-md-2']/input[@name='studentName']"
    pid_input = "xpath=>//div[@class='form-group m-b-5 search-wrap search-resize']/div[@class='col-md-2']/input[@name='pid']"
    mobile_input = "xpath=>//div[@class='form-group m-b-5 search-wrap search-resize']/div[@class='col-md-2']/input[@name='telephone']"
    activity_name_input = "xpath=>//div[@class='form-group m-b-5 search-wrap search-resize']/div[@class='col-md-2']/input[@name='activityName']"
    create_name_input = "xpath=>//div[@class='form-group m-b-5 search-wrap search-resize']/div[@class='col-md-2']/input[@name='creatorName']"
    search_btn = "xpath=>//button[contains(text(),'搜索')]"
    def ConditionSearch(self,**param):
        self.send_keys(self.name_input,param['name'])
        self.send_keys(self.pid_input,param['pid'])
        self.send_keys(self.mobile_input,param['mobile'])
        self.send_keys(self.activity_name_input,param['activityName'])
        self.send_keys(self.create_name_input,param['createName'])
        self.click(self.search_btn)

    #新增AddNew
    new_add_btn = "xpath=>//button[contains(text(),'新增')]"
    add_studentName_input = "xpath=>//div[@class='col-md-9']/input[@name='studentName']"
    num_option = "xpath=>//*[@id='contactInformation']/option[@value='5']"  # 联系方式下拉框
    add_mobile_input = "xpath=>//input[@placeholder='联系方式']"
    add_activityName_input = "xpath=>//*[@id='activityId']" #活动名称
    intention_option = "xpath=>//*[@id='intentionType']/option[@value='1']"  # 咨询方向下拉框 默认：1
    add_submit = "xpath=>//*[@class='modal-footer']/a[contains(text(),'确认')]"
    def NewAdd(self, add_name, add_mobile,add_activityName):
        self.click(self.new_add_btn)
        sleep(1)
        self.send_keys(self.add_studentName_input, add_name)
        self.click(self.num_option)  # 选择联系方式
        self.send_keys(self.add_mobile_input, add_mobile)
        self.send_keys(self.add_activityName_input,add_activityName)
        self.click(self.intention_option)  # 选择咨询方式
        sleep(1)
        self.click(self.add_submit)


    #导出
    export_btn = "id=>export"
    def Export(self):
        self.click(self.export_btn)

    #查看
    check_info_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def CheckInfo(self):
        self.click(self.check_info_btn)

    # #编辑
    # def Edit(self):
    #     pass
    #
    # #删除
    # def Delete(self):
    #     pass