from unit.base_page import BasePage
from time import sleep

class newMediaResourcePage(BasePage):
    #资源状态
    source_status_1 = "pxath=>//div[@id='serSchoolWrap']/a[@data-serval='1']" #待确认
    source_status_2 = "pxath=>//div[@id='serSchoolWrap']/a[@data-serval='2']"  # 需要再次确认
    source_status_3 = "pxath=>//div[@id='serSchoolWrap']/a[@data-serval='3']"  # 有效
    source_status_4 = "pxath=>//div[@id='serSchoolWrap']/a[@data-serval='4']"  # 无效
    def Origin(self,sourceStatus):
        if sourceStatus == 1:
            self.click(self.source_status_1)
        elif sourceStatus == 2:
            self.click(self.source_status_2)
        elif sourceStatus == 3:
            self.click(self.source_status_3)
        elif sourceStatus == 4:
            self.click(self.source_status_4)
        else:
            print("请输入正确的资源状态")

    search_btn = "id=>search"
    #搜索条件
    searchInput_studentName = "xpath=>//div[@class='col-md-2']/input[@name='studentName']"
    searchInput_Pid = "xpath=>//div[@class='col-md-2']/input[@name='pid']"
    searchInput_telephone = "xpath=>//div[@class='col-md-2']/input[@name='mobile']"
    def SearchCondition(self,**searchInput):
        if searchInput['studentName']:
            self.send_keys(self.searchInput_studentName,searchInput['studentName'])
            self.click(self.search_btn)
        elif searchInput['pid']:
            self.send_keys(self.searchInput_Pid,searchInput['pid'])
            self.click(self.search_btn)
        elif searchInput['telephone']:
            self.send_keys(self.searchInput_telephone,searchInput['telephone'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)


    #新增
    addNew_btn = "xpath=>//button[contains(text(),'新增')]"
    addInput_student = "xpath=>//div[@class='col-md-9']/input[@name='studentName']"
    addInput_telephone = "xpath=>//div[@class='checkValInpWrap pull-left']/input[@name='mobiles']"
    addSubmit_btn = "xpath=>//div[@class='modal-footer']/a[contains(text(),'确认')]"
    def AddNew(self,**addInput):
        self.click(self.addNew_btn)
        sleep(2)
        self.send_keys(self.addInput_student,addInput['studentName'])
        self.send_keys(self.addInput_telephone,addInput['telephone'])
        self.click(self.addSubmit_btn)

    #批量导入
    import_btn = "xpath=>//button[contains(text(),'下载模板')]"
    upFile_input = "xpath=>//div[@class='col-md-9']/input[@name='upFile']"
    upload_btn = "xpath=>//div[@class='modal-footer']/button[contains(text(),'上传')]"
    def Upload(self):
        self.click(self.import_btn)
        sleep(3)
        self.send_keys(self.upFile_input,"D://ChromeDownload//活动资源.xlsx")
        sleep(3)
        self.click(self.upload_btn)

    #下载模板
    download_btn = "xpath=>//button[contains(text(),'下载模板')]"
    def Download(self):
        self.click(self.download_btn)

    #查看
    check_btn = "//td[@datano='0']/button[@style='margin-right: 10px;']"
    def Check(self):
        self.click(self.check_btn)

    #查看跟进详情
    check_detail_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看跟进详情')]"
    def CheckDetail(self):
        self.click(self.check_detail_btn)
