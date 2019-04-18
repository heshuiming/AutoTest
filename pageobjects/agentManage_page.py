from unit.base_page import BasePage
from time import sleep

class agentManagePage(BasePage):
    #代理类型
    agentType0 = "xpath=>//a[@data-serval='0']" #公司
    agentType1 = "xpath=>//a[@data-serval='1']" #个人中介
    agentType2 = "xpath=>//a[@data-serval='2']" #留学中介
    agentType3 = "xpath=>//a[@data-serval='3']" #高校
    agentType4 = "xpath=>//a[@data-serval='4']" #教师
    agentType5 = "xpath=>//a[@data-serval='5']"  # 班主任
    def AgentType(self,i):
        if i == 0:
            self.click(self.agentType0)
        elif i == 1:
            self.click(self.agentType1)
        elif i == 2:
            self.click(self.agentType2)
        elif i == 3:
            self.click(self.agentType3)
        elif i == 4:
            self.click(self.agentType4)
        elif i == 5:
            self.click(self.agentType5)
        else:
            return 0

    #搜索条件
    agentName_input = "xpath=>//input[@class='form-control input-search'][@name='agentName']"
    telephone_input = "xpath=>//input[@class='form-control input-search'][@name='telephone']"
    managerName_input = "xpath=>//input[@class='form-control input-search'][@name='managerName']"
    search_btn = "id=>search"
    def Search(self,**param):
        if param['agentName']:
            self.send_keys(self.agentName_input,param['agentName'])
            self.click(self.search_btn)
        elif param['telephone']:
            self.send_keys(self.telephone_input,param['telephone'])
            self.click(self.search_btn)
        elif param['managerName']:
            self.send_keys(self.managerName_input,param['managerName'])
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    #新增
    add_new_btn = "xpath=>//div[@class='col-md-']/button[contains(text(),'新增')]"
    #代理类型
    company = "xpath=>//label[@for='typeStr-company']/i[@class='iconfont radioCheck']" #默认选中
    personalIntermediary = "xpath=>//label[@for='typeStr-personalIntermediary']/i[@class='iconfont radioNoCheck']"
    studyAgency = "xpath=>//label[@for='typeStr-studyAgency']/i[@class='iconfont radioNoCheck']"
    collUn = "xpath=>//label[@for='typeStr-collUn']/i[@class='iconfont radioNoCheck']"
    teacher = "xpath=>//label[@for='typeStr-teacher']/i[@class='iconfont radioNoCheck']"
    headMaster = "xpath=>//label[@for='typeStr-headMaster']/i[@class='iconfont radioNoCheck']"

    schoolCode = "xpath=>//select[@id='schoolCode']/option[@value='001']" #默认选择北京学校
    agentName_add = "xpath=>//div[@class='col-md-9']/input[@name='agentName']"
    companyName_add = "xpath=>//input[@name='companyName']"
    loginName_add = "name=>loginName"
    password_add = "name=>password"
    confirmPassword_add = "name=>confirmPassword"
    telephone_add = "xpath=>//div[@class='col-md-9']/input[@name='telephone']"
    managerName_add = "xpath=>//div[@id='managerLoginNameWrap']/input[@name='managerName']"
    submit_add_btn = "xpath=>//div[@class='modal-footer']/a[contains(text(),'确认')]"
    def AddNew(self,**param):
        self.click(self.add_new_btn)
        sleep(1)
        self.click(self.company)
        self.click(self.schoolCode)
        self.send_keys(self.agentName_add,param['agentName'])
        self.send_keys(self.companyName_add,param['companyName'])
        self.send_keys(self.loginName_add,param['loginName'])
        self.send_keys(self.password_add,param['password'])
        self.send_keys(self.confirmPassword_add,param['confirmPassword'])
        self.send_keys(self.telephone_add,param['telephone'])
        self.send_keys(self.managerName_add,param['managerName'])
        self.click(self.submit_add_btn)

    #下载模板
    download_btn = "link_text=>下载模板"
    def Download(self):
        self.click(self.download_btn)

    #编辑
    edit_btn = "xpath=>//td[@datano='0']/button[contains(text(),'编辑')]"
    def Edit(self,**param):
        self.click(self.edit_btn)
        self.click(self.company)
        self.click(self.schoolCode)
        self.send_keys(self.agentName_add, param['agentName'])
        self.send_keys(self.companyName_add, param['companyName'])
        self.send_keys(self.loginName_add, param['loginName'])
        self.send_keys(self.password_add, param['password'])
        self.send_keys(self.confirmPassword_add, param['confirmPassword'])
        self.send_keys(self.telephone_add, param['telephone'])
        self.send_keys(self.managerName_add,param['managerName'])
        self.click(self.submit_add_btn)

    #导入学员
    import_btn = "xpath=>//td[@datano='0']/button[contains(text(),'导入学员')]"
    upFile_btn = "name=>upFile"
    upload_btn = "id=>import-btn"
    #file_path = "D://ChromeDownload//代理资源.xlsx"
    def ImportStudent_btn(self):
        self.click(self.import_btn)
        sleep(5)
        self.send_keys(self.upFile_btn,"D://ChromeDownload//代理资源.xlsx")
        sleep(2)
        self.click(self.upload_btn)

    '''
    #选择上传文件
    def ImportStudent(self):
        self.click(self.upFile_btn)
        sleep(1)
        self.send_keys(self.file_path)
        sleep(1)
        self.click(self.upload_btn)
    '''

    #重置密码
    setPassword_btn = "xpath=>//td[@datano='0']/button[contains(text(),'重置密码')]"
    password_input = "id=>password"
    confirmPassword_input = "id=>confirmPassword"
    submit_btn = "xpath=>//a[@class='btn btn-primary btn-submit'][contains(text(),'确认')]"
    def SetPassword_btn(self):
        self.click(self.setPassword_btn)
    def SetPassword(self,password,confirmPassword):
        self.send_keys(self.password_input,password)
        self.send_keys(self.confirmPassword_input,confirmPassword)
        self.click(self.submit_btn)

