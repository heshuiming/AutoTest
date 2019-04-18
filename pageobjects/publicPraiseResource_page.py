from time import sleep
from unit.base_page import BasePage

#我的口碑资源
class publicPraiseResourcePage(BasePage):
    # 分配情况-全部
    # 分配情况-不可分配
    # 分配情况-待分配
    # 分配情况-分配成功
    #搜索条件
    studentName_input = "xpath=>//input[@name='studentName']"
    pid_input = "xpath=>//input[@name='pid']"
    mobile_input = "xpath=>//input[@name='mobile']"
    search_btn = "id=>search"
    def Search(self,name,pid,mobile):
        student_name = self.send_keys(self.studentName_input,name)
        student_pid = self.send_keys(self.pid_input,pid)
        student_mobile = self.send_keys(self.mobile_input,mobile)
        if student_name != "":
            self.click(self.search_btn)
        elif student_pid != "":
            self.click(self.search_btn)
        elif student_mobile != "":
            self.click(self.search_btn)
        elif (student_name != "") and (student_pid != ""):
            self.click(self.search_btn)
        elif (student_name != "") and (student_mobile != ""):
            self.click(self.search_btn)
        else:
            self.click(self.search_btn)

    new_add_btn = "xpath=>//button[contains(text(),'新增')]"
    add_studentName_input = "xpath=>//input[@placeholder='姓名']"
    num_option = "xpath=>//*[@id='contactInformation']/option[@value='5']" #联系方式下拉框
    add_mobile_input = "xpath=>//input[@placeholder='联系方式']"
    intention_option = "xpath=>//*[@id='intention']/option[@value='1']" #咨询方向下拉框 默认：1
    itemKey_option = "xpath=>//*[@id='relCourseTypeId']/option[@value='1']" #来源部门下拉框 默认：1
    add_submit = "xpath=>//*[@class='modal-footer']/a[contains(text(),'确认')]"
    def NewAdd(self,add_name,add_mobile):
        self.click(self.new_add_btn)
        sleep(2)
        self.send_keys(self.add_studentName_input,add_name)
        self.click(self.num_option) #选择联系方式
        self.send_keys(self.add_mobile_input,add_mobile)
        self.click(self.intention_option) #选择咨询方式
        self.click(self.itemKey_option) #选择来源部门
        sleep(2)
        self.click(self.add_submit)

    #查看序号为1的学员信息
    check_info_btn = "xpath=>//td[@datano='0']/button[contains(text(),'查看')]"
    def CheckInfo(self):
        self.click(self.check_info_btn)

    # #删除
    # def Delete(self):
    #     pass
    #
    # #编辑
    # def Edit(self):
    #     pass
