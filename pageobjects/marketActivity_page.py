from unit.base_page import BasePage
from time import sleep


#活动管理
class marketActivityPage(BasePage):
    #咨询方向搜索
    #活动类型搜索
    #校区搜索

    #搜素
    begin_time_input = "name=>beginTime"
    end_time_input = "name=>endTime"
    activityName_input = "name=>name"
    search_btn = "id=>search"
    def Search(self,**param):
        self.send_keys(self.begin_time_input,param['beginTime'])
        self.send_keys(self.end_time_input,param['endTime'])
        self.send_keys(self.activityName_input,param['activityName'])
        self.click(self.search_btn)

    #新增
    add_new_btn = "xpath=>//button[contains(text(),'新增')]" #新增按钮
    add_name_input = "xpath=>//div[@class='col-md-9']/input[@name='name']" #活动名称
    add_theme_input = "xpath=>//select[@id='theme']/option[@value='1']" #咨询方向
    add_beginTime_input = "xpath=>//div[@class='col-md-9 input-group input-medium date-picker input-daterange']/div[1]/input[@name='beginTime']" #开始时间
    add_endTime_input = "xpath=>//div[@class='col-md-9 input-group input-medium date-picker input-daterange']/div[1]/input[@name='endTime']" #结束时间
    add_type_input = "xpath=>//div[@class='col-md-9']/select[@name='type']/option[@value='1']" #活动类型
    add_peopleInCharge_input = "xpath=>//div[@class='col-md-9']/input[@name='peopleInCharge']" #活动负责人
    add_purpose_input = "xpath=>//div[@class='col-md-9']/input[@name='purpose']" #活动目的
    add_speaker_input = "xpath=>//div[@class='col-md-9']/input[@name='speaker']" #主讲人
    add_readonly_input = "xpath=>//input[@readonly='readonly']" #受众年级
    add_costType_input = "xpath=>//div[@class='col-md-9']/input[@name='costType']"#费用类型
    add_cost1_input = "xpath=>//div[@class='col-md-9 form-input']/input[@value='0']"#预计费用整数位
    add_cost2_input = "xpath=>//div[@class='col-md-9 form-input']/input[@value='00']" #预计费用小数位
    add_submit_btn = "xpath=>//div[@class='modal-footer']/a[contains(text(),'确认')]" #确认按钮
    def AddNew(self,**param):
        self.click(self.add_new_btn)
        self.send_keys(self.add_name_input,param['name'])
        self.send_keys(self.add_theme_input,param['theme'])
        self.send_keys(self.add_beginTime_input,param['beginTime'])
        self.send_keys(self.add_endTime_input,param['endTime'])
        self.click(self.add_type_input) #活动类型，默认为1
        self.send_keys(self.add_peopleInCharge_input,param['peopleInCharge'])
        self.send_keys(self.add_purpose_input,param['purpose'])
        self.send_keys(self.add_speaker_input,param['speaker'])
        self.send_keys(self.add_readonly_input,param['readonly'])
        self.send_keys(self.add_costType_input,param['costType'])
        self.send_keys(self.add_cost1_input,param['cost1'])
        self.send_keys(self.add_cost2_input,param['cost2'])
        sleep(2)
        self.click(self.add_submit_btn)

    #下载模板
    download_btn = "link_text=>下载模板"
    def Download(self):
        self.click(self.download_btn)
