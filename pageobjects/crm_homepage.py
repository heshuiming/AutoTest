import time
from unit.base_page import BasePage

class CrmHomePage(BasePage):
    #环球工作台登录页面
    input_username = "id=>login-userName"
    input_pwd = "id=>login-pwd"
    login_sumbit_btn = "id=>submit"
    def login(self, **data):
        self.send_keys(self.input_username, data['name'])  # 输入用户名
        self.send_keys(self.input_pwd, data['pwd'])  # 输入密码
        self.click(self.login_sumbit_btn)  # 点击登录
        time.sleep(1)
        self.click(self.crm_logo)  # 跳转至青龙
        time.sleep(1)
        search_window = self.driver.current_window_handle
        time.sleep(2)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != search_window:
                self.driver.switch_to.window(handle)
                time.sleep(2)

    # 点击登录按钮
    def login_btn(self,**data):
        self.send_keys(self.input_username, data['name'])  # 输入用户名
        self.send_keys(self.input_pwd, data['pwd'])  # 输入密码
        self.click(self.login_sumbit_btn)

    # 跳转至青龙系统
    crm_logo = "xpath=>//span[contains(text(),'青龙')]"
    def skip_crm(self):
        self.click(self.crm_logo)

    #“我的资源”模块
    my_source_btn = "xpath=>//span[contains(text(),'我的资源')]"
    #已成学员
    alreadyStudent_btn = "link_text=>已成学员"
    def alreadyStudent(self):  #跳转至我的学员
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.alreadyStudent_btn)

    #待跟进
    followup_btn = "link_text=>待跟进"
    def FollwUp(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.followup_btn)

    #我的到访
    myInvite_btn = "link_text=>我的到访"
    def MyInvite(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myInvite_btn)

    #我的回访
    myNextInvite_btn = "link_text=>我的回访"
    def MyNextInvite(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myNextInvite_btn)

    #转出资源
    myInvalidList_btn = "link_text=>转出资源"
    def MyInvalidList(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myInvalidList_btn)

    #我的资源合并历史
    myResourceMerge_btn = "link_text=>我的资源合并历史"
    def MyResourceMerge(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myResourceMerge_btn)


    #“资源录入”模块
    resource_input_btn = "xpath=>//span[contains(text(),'资源录入')]"
    #我的口碑资源
    publicPraiseResourceList_btn = "link_text=>我的口碑资源"
    def PublicPraiseResourceList(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.publicPraiseResourceList_btn)

    #我的活动资源
    marketActivityResource_btn = "link_text=>我的活动资源"
    def MarketActivityResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.marketActivityResource_btn)

    #活动资源导入历史
    marketActivityImportHistory_btn = "link_text=>活动资源导入历史"
    def MarketActivityImportHistory(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.marketActivityImportHistory_btn)

    #活动管理
    marketActivityManager_btn = "link_text=>活动管理"
    def MarketActivityManager(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.marketActivityManager_btn)

    #我的代理资源
    agentResource_btn = "link_text=>我的代理资源"
    def AgentResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.agentResource_btn)

    #代理资源导入历史
    agentImportHistory_btn = "link_text=>代理资源导入历史"
    def AgentImportHistory(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.agentImportHistory_btn)

    #代理管理
    agentManager_btn = "link_text=>代理管理"
    def AgentManager(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.agentManager_btn)

    #我的新媒体资源
    newMediaResource_btn = "link_text=>我的新媒体资源"
    def NewMediaResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.newMediaResource_btn)

    #我的TMK资源
    tmkResourceInMy_btn = "link_text=>我的TMK资源"
    def TmkResourceInMy(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkResourceInMy_btn)

    #TMK资源导入历史
    tmkImportHistory_btn = "link_text=>TMK资源导入历史"
    def TmkImportHistory(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkImportHistory_btn)

    #TMK任务设置
    tmkTaskSetting_btn = "link_text=>TMK任务设置"
    def TmkTaskSetting(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkTaskSetting_btn)

    #TMK任务历史查询
    tmkTaskQuery_btn = "link_text=>TMK任务历史查询"
    def TmkTaskQuery(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkTaskQuery_btn)

    #TMK兼职管理
    tmkEmployee_btn = "link_text=>TMK兼职管理"
    def TmkEmployee(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkEmployee_btn)

    #我的客服资源
    customerResource_btn = "link_text=>我的客服资源"
    def CustomerResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.customerResource_btn)

    #新增客服资源
    customerResAdd_btn = "link_text=>新增客服资源"
    def CustomerResAdd(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.customerResAdd_btn)

    #我的代理管理
    myAgent_btn = "link_text=>我的代理管理"
    def MyAgent(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.myAgent_btn)


    #“市场资源”模块
    market_resource_btn = "xpath=>//span[contains(text(),'市场资源')]"
    #全部资源
    allResourceInMarket_btn = "link_text=>全部资源"
    def AllResourceInMarket(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.allResourceInMarket_btn)

    #全部口碑资源
    allPublicPraiseResourceList_btn = "link_text=>全部口碑资源"
    def AllPublicPraiseResourceList(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.allPublicPraiseResourceList_btn)

    #全部活动资源
    marketActivityResourceAll_btn = "link_text=>全部活动资源"
    def MarketActivityResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.marketActivityResourceAll_btn)

    #全部代理资源
    agentResourceAll_btn = "link_text=>全部代理资源"
    def AgentResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.agentResourceAll_btn)

    #全部新媒体资源
    newMediaResourceAll_btn = "link_text=>全部新媒体资源"
    def NewMediaResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.newMediaResourceAll_btn)

    #全部TMK资源
    tmkResource_btn = "link_text=>全部TMK资源"
    def TmkResource(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.tmkResource_btn)

    #全部客服资源
    customerResourceAll_btn = "link_text=>全部客服资源"
    def CustomerResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.customerResourceAll_btn)

    #全部搜课资源
    searchResourceAll_btn = "link_text=>全部搜课资源"
    def SearchResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.searchResourceAll_btn)

    #“资源分配”模块
    resource_allocation_btn = "xpath=>//span[contains(text(),'资源分配')]"
    #全部资源
    onListAllResourceAllocation_btn = "link_text=>全部资源"
    def OnListAllResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.onListAllResourceAllocation_btn)

    #搜课资源
    searchResourceAllocationList_btn = "link_text=>搜课资源"
    def SearchResourceAllocationList(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.searchResourceAllocationList_btn)

    #代理资源
    agentResourceAllocation_btn = "link_text=>代理资源"
    def AgentResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.agentResourceAllocation_btn)

    #活动资源
    marketActivityResourceAllocation_btn = "link_text=>活动资源"
    def MarketActivityResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.marketActivityResourceAllocation_btn)

    #新媒体资源
    newMediaResourceAllocation_btn = "link_text=>新媒体资源"
    def NewMediaResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.newMediaResourceAllocation_btn)

    #口碑资源
    publicPraisResourceAllocation_btn = "link_text=>口碑资源"
    def PublicPraisResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.publicPraisResourceAllocation_btn)

    #TMK资源
    tmkResourceAllocation_btn = "link_text=>TMK资源"
    def TmkResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.tmkResourceAllocation_btn)

    #销售报备资源
    saleResourceAllocation_btn = "link_text=>销售报备资源"
    def SaleResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.saleResourceAllocation_btn)

    #客服资源
    customerResourceAllocation_btn = "link_text=>客服资源"
    def CustomerResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.customerResourceAllocation_btn)


    #“资源管理”模块
    resource_manage_btn = "xpath=>//span[contains(text(),'资源管理')]"
    #重复用户管理
    searchResourceMerge_btn = "link_text=>重复用户管理"
    def SearchResourceMerge(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.searchResourceMerge_btn)

    #全部资源
    allResource_btn = "link_text=>全部资源"
    def AllResource(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.allResource_btn)

    #本组资源
    groupResourceList_btn = "link_text=>本组资源"
    def GroupResourceList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.groupResourceList_btn)

    #全部到访
    allInvite_btn = "link_text=>全部到访"
    def AllInvite(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.allInvite_btn)

    #全部回访
    nextVisit_btn = "link_text=>全部回访"
    def NextVisit(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.nextVisit_btn)

    #过期资源池
    resourceOverdueClaimList_btn = "link_text=>过期资源池"
    def ResourceOverdueClaimList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceOverdueClaimList_btn)

    #公共资源池
    resourceInvalidClaimList_btn = "link_text=>公共资源池"
    def resourceInvalidClaimList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceInvalidClaimList_btn)

    #全部资源合并历史
    resourceMerge_btn = "link_text=>全部资源合并历史"
    def ResourceMerge(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceMerge_btn)

    #无效资源池
    resourceInvalidNotClaimList_btn = "link_text=>无效资源池"
    def ResourceInvalidNotClaimList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceInvalidNotClaimList_btn)

    #过期资源池管理
    resourceOverdueListForManage_btn = "link_text=>过期资源池管理"
    def ResourceOverdueListForManage(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceOverdueListForManage_btn)

    #公共资源池管理
    publicResourceManageList_btn = "link_text=>公共资源池管理"
    def PublicResourceManageList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.publicResourceManageList_btn)

    #再分配
    resourceToCounselor_btn = "link_text=>再分配"
    def ResourceToCounselor(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceToCounselor_btn)

    #组内再分配
    resourceToCounselorForGroup_btn = "link_text=>组内再分配"
    def ResourceToCounselorForGroup(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceToCounselorForGroup_btn)

    #资源搜索
    ResourceSaleQuery_btn = "link_text=>资源搜索"
    def ResourceSaleQuery(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.ResourceSaleQuery_btn)

    #超期资源
    ExceedTermResource_btn = "link_text=>超期资源"
    def ExceedTermResource(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.ExceedTermResource_btn)


    #”绩效管理“模块
    performance_manage_btn = "xpath=>//span[contains(text(),'绩效管理')]"
    #月度绩效
    monthPerformanceUserGroup_btn = "link_text=>月度绩效"
    def MonthPerformanceUserGroup(self):
        self.click(self.monthPerformanceUserGroup_btn)


    #”消息管理“模块
    massage_manage_btn = "xpath=>//span[contains(text(),'消息管理')]"
    #消息列表
    systemMsg_btn = "link_text=>消息列表"
    def SystemMsg(self):
        self.click(self.massage_manage_btn)
        time.sleep(2)
        self.click(self.systemMsg_btn)

    #消息接收人
    systemMsgReceiver_btn = "link_text=>消息接收人"
    def SystemMsgReceiver(self):
        self.click(self.massage_manage_btn)
        time.sleep(2)
        self.click(self.systemMsgReceiver_btn)


    #”订单管理“模块
    order_manage_btn = "xpath=>//span[contains(text(),'订单管理')]"
    #本组订单
    groupOrder_btn = "link_text=>本组订单"
    def GroupOrder(self):
        self.click(self.order_manage_btn)
        time.sleep(2)
        self.click(self.groupOrder_btn)

    #全部订单
    order_btn = "link_text=>全部订单"
    def Order(self):
        self.click(self.order_manage_btn)
        time.sleep(2)
        self.click(self.order_btn)

    #我的订单
    myOrder_btn = "link_text=>我的订单"
    def MyOrder(self):
        self.click(self.order_manage_btn)
        time.sleep(2)
        self.click(self.myOrder_btn)


    #”退费管理“模块
    refund_manage_btn = "xpath=>//span[contains(text(),'退费管理')]"
    #普通退费申请
    refundApply_btn = "link_text=>普通退费申请"
    def RefundApply(self):
        self.click(self.refund_manage_btn)
        time.sleep(2)
        self.click(self.refundApply_btn)

    #退费确认
    refundConfirm_btn = "link_text=>退费确认"
    def RefundConfirm(self):
        self.click(self.refund_manage_btn)
        time.sleep(2)
        self.click(self.refundConfirm_btn)

    #应收账款退费
    receivablesRefund_btn = "link_text=>应收账款退费"
    def ReceivablesRefund(self):
        self.click(self.refund_manage_btn)
        time.sleep(2)
        self.click(self.receivablesRefund_btn)


    #”班级管理“模块
    class_manage_btn = "xpath=>//span[contains(text(),'班级管理')]"
    #教务-班级管理
    onClassManageList_btn = "link_text=>教务-班级管理"
    def OnClassManageList(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.onClassManageList_btn)

    #学管-全部班级
    saAllClassList_btn = "link_text=>学管-全部班级"
    def SaAllClassList(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.saAllClassList_btn)

    #学管-本组班级
    onSaDirectorClassList_btn = "link_text=>学管-本组班级"
    def OnSaDirectorClassList(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.onSaDirectorClassList_btn)

    #学管-我的班级
    saClassList_btn = "link_text=>学管-我的班级"
    def SaClassList(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.saClassList_btn)

    #教务-全部班级
    saleClass_btn ="link_text=>教务-全部班级"
    def SaleClass(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.saleClass_btn)

    #排课通知
    scheduleNotice_btn = "link_text=>排课通知"
    def ScheduleNotice(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.scheduleNotice_btn)

    #合班
    classJoin_btn = "link_text=>合班"
    def ClassJoin(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.classJoin_btn)

    #合班历史
    history_btn = "link_text=>合班历史"
    def History(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.history_btn)

    #全部销售班级
    saleOfClassList_btn = "link_text=>全部销售班级"
    def SaleOfClassList(self):
        self.click(self.class_manage_btn)
        time.sleep(2)
        self.click(self.saleOfClassList_btn)


    #”教师管理“模块
    teacher_manage_btn = "xpath=>//span[contains(text(),'教师管理')]"
    #全部教师
    allTeacherManager_btn = "link_text=>全部教师"
    def AllTeacherManager(self):
        self.click(self.teacher_manage_btn)
        time.sleep(2)
        self.click(self.allTeacherManager_btn)

    #教师信息
    academicTeacherManager_btn = "link_text=>教师信息"
    def AcademicTeacherManager(self):
        self.click(self.teacher_manage_btn)
        time.sleep(2)
        self.click(self.academicTeacherManager_btn)

    #我的教师管理
    teachingTeacherManager_btn = "link_text=>我的教师管理"
    def TeachingTeacherManager(self):
        self.click(self.teacher_manage_btn)
        time.sleep(2)
        self.click(self.teachingTeacherManager_btn)

    #本组教师
    currentTeachingDepartment_btn = "link_text=>本组教师"
    def CurrentTeachingDepartment(self):
        self.click(self.teacher_manage_btn)
        time.sleep(2)
        self.click(self.currentTeachingDepartment_btn)

    #教师列表
    hrTeacherManager_btn = "link_text=>教师列表"
    def HrTeacherManager(self):
        self.click(self.teacher_manage_btn)
        time.sleep(2)
        self.click(self.hrTeacherManager_btn)

    #教师排课查询
    teacherInfoForPlanHour_btn = "link_text=>教师排课查询"
    def TeacherInfoForPlanHour(self):
        self.click(self.teacher_manage_btn)
        time.sleep(2)
        self.click(self.teacherInfoForPlanHour_btn)


    #”教师薪资“模块
    teacher_pay_btn = "xpath=>//span[contains(text(),'教师薪资')]"
    #教师课时审核
    statMonthClassTeacherInfo_btn = "link_text=>教师课时审核"
    def StatMonthClassTeacherInfo(self):
        self.click(self.teacher_pay_btn)
        time.sleep(2)
        self.click(self.statMonthClassTeacherInfo_btn)

    #教师薪资审核
    teacherRewardPunishHistory_btn = "link_text=>教师薪资审核"
    def TeacherRewardPunishHistory(self):
        self.click(self.teacher_pay_btn)
        time.sleep(2)
        self.click(self.teacherRewardPunishHistory_btn)

    #运营学校已审核课金
    statTeacherMonthFeeSchool_btn = "link_text=>运营学校已审核课金"
    def StatTeacherMonthFeeSchool(self):
        self.click(self.teacher_pay_btn)
        time.sleep(2)
        self.click(self.statTeacherMonthFeeSchool_btn)

    #实体学校已审核课金
    statTeacherMonthFeeAgency_btn = "link_text=>实体学校已审核课金"
    def StatTeacherMonthFeeAgency(self):
        self.click(self.teacher_pay_btn)
        time.sleep(2)
        self.click(self.statTeacherMonthFeeAgency_btn)


    #”考勤管理“模块
    attendance_manage_btn = "xpath=>//span[contains(text(),'考勤管理')]"
    #学员&教师考勤
    studentAndTeacherAttendance_btn = "link_text=>学员&教师考勤"
    def StudentAndTeacherAttendance(self):
        self.click(self.attendance_manage_btn)
        time.sleep(2)
        self.click(self.studentAndTeacherAttendance_btn)

    #教师补打考勤
    teacherFillAttendance_btn = "link_text=>教师补打考勤"
    def TeacherFillAttendance(self):
        self.click(self.attendance_manage_btn)
        time.sleep(2)
        self.click(self.teacherFillAttendance_btn)


    #”排班管理“模块
    schedule_manage_btn = "xpath=>//span[contains(text(),'排班管理')]"
    #排班设置
    staffSchedule_btn = "link_text=>排班设置"
    def StaffSchedule(self):
        self.click(self.schedule_manage_btn)
        time.sleep(2)
        self.click(self.staffSchedule_btn)

    #销售查看排班
    saleStaffSchedule_btn = "link_text=>销售查看排班"
    def SaleStaffSchedule(self):
        self.click(self.schedule_manage_btn)
        time.sleep(2)
        self.click(self.saleStaffSchedule_btn)


    #”学员管理“模块
    student_manage_btn = "xpath=>//span[contains(text(),'学员管理')]"
    #学员档案
    student_btn = "link_text=>学员档案"
    def Student(self):
        self.click(self.student_manage_btn)
        time.sleep(2)
        self.click(self.student_btn)


    #”基础信息“模块
    basic_msg_btn = "xpath=>//span[contains(text(),'基础信息')]"
    #课程管理
    course_btn = "link_text=>课程管理"
    def Course(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.course_btn)

    #套餐管理
    coursesIntegrated_btn = "link_text=>套餐管理"
    def CoursesIntegrated(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.coursesIntegrated_btn)

    #教学区管理
    teachAreaManage_btn = "link_text=>教学区管理"
    def TeachAreaManage(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.teachAreaManage_btn)

    #教室管理
    classRoom_btn = "link_text=>教室管理"
    def ClassRoom(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.classRoom_btn)

    #校区管理
    schoolAreaManage_btn = "link_text=>校区管理"
    def SchoolAreaManage(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.schoolAreaManage_btn)

    #校区排课管理
    schoolAreaScheduleManage_btn = "link_text=>校区排课管理"
    def SchoolAreaScheduleManage(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.schoolAreaScheduleManage_btn)

    #本校字典
    thisSchoolDictManage_btn = "link_text=>本校字典"
    def ThisSchoolDictManage(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.thisSchoolDictManage_btn)

    #本校类型
    courseTypeForSchool_btn = "link_text=>本校类型"
    def CourseTypeForSchool(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.courseTypeForSchool_btn)

    #本校科目
    courseSubjectForSchool_btn = "link_text=>本校科目"
    def CourseSubjectForSchool(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.courseSubjectForSchool_btn)

    #授课科目
    teachingSubject_btn = "link_text=>授课科目"
    def TeachingSubject(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.teachingSubject_btn)

    #签约机构管理
    signAgency_btn = "link_text=>签约机构管理"
    def SignAgency(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.signAgency_btn)

    #签约部门管理
    signDepartment_btn = "link_text=>签约部门管理"
    def SignDepartment(self):
        self.click(self.basic_msg_btn)
        time.sleep(2)
        self.click(self.signDepartment_btn)


    #”报表统计“模块（未写）
    #”代理返佣“模块
    agentMaid_btn = "xpath=>//span[contains(text(),'代理返佣')]"
    #代理返佣明细
    agentMaidList_btn = "link_text=>代理返佣明细"
    def AgentMaidList(self):
        self.click(self.agentMaid_btn)
        time.sleep(2)
        self.click(self.agentMaidList_btn)

    #代理返佣申请
    agentMaidApply_btn = "link_text=>代理返佣申请"
    def AgentMaidApply(self):
        self.click(self.agentMaid_btn)
        time.sleep(2)
        self.click(self.agentMaidApply_btn)

    #代理返佣比例审核
    agentMaidRateExamine_btn = "link_text=>代理返佣比例审核"
    def AgentMaidRateExamine(self):
        self.click(self.agentMaid_btn)
        time.sleep(2)
        self.click(self.agentMaidRateExamine_btn)

    #代理返佣财务审核
    agentMaidFinanceExamine_btn = "link_text=>代理返佣财务审核"
    def AgentMaidFinanceExamine(self):
        self.click(self.agentMaid_btn)
        time.sleep(2)
        self.click(self.agentMaidFinanceExamine_btn)

    #已返佣明细
    agentMaidFeeDetail_btn = "link_text=>已返佣明细"
    def agentMaidFeeDetail(self):
        self.click(self.agentMaid_btn)
        time.sleep(2)
        self.click(self.agentMaidFeeDetail_btn)


    #”销售机会查询“模块
    sale_chance_check_btn = "xpath=>//span[contains(text(),'销售机会查询')]"
    #学员回访信息
    studentRevisitInfomation_btn = "link_text=>学员回访信息"
    def StudentRevisitInfomation(self):
        self.click(self.sale_chance_check_btn)
        time.sleep(2)
        self.click(self.studentRevisitInfomation_btn)

    #本组学员回访信息
    studentRevisitInfomationGroup_btn = "link_text=>本组学员回访信息"
    def StudentRevisitInfomationGroup(self):
        self.click(self.sale_chance_check_btn)
        time.sleep(2)
        self.click(self.studentRevisitInfomationGroup_btn)


    #”财务报表“模块（未写）
    #”业务审核“模块
    business_auditing_btn = "xpath=>//span[contains(text(),'业务审核')]"
    #我发起的
    workflowInstance_btn = "link_text=>我发起的"
    def WorkflowInstance(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.workflowInstance_btn)

    #待审核
    workflowInstanceWaitAudit_btn = "link_text=>待审核"
    def WorkflowInstanceWaitAudit(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.workflowInstanceWaitAudit_btn)

    #已审核
    workflowInstanceApproveAudit_btn = "link_text=>已审核"
    def WorkflowInstanceApproveAudit(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.workflowInstanceApproveAudit_btn)

    #优惠申请
    discountWorkflowInstanceList_btn = "link_text=>优惠申请"
    def DiscountWorkflowInstanceList(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.discountWorkflowInstanceList_btn)

    #资源合并
    mergeResourceWorkflowInstance_btn = "link_text=>资源合并"
    def MergeResourceWorkflowInstance(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.mergeResourceWorkflowInstance_btn)

    #班级合并
    mergeClassWorkflowInstanceList_btn = "link_text=>班级合并"
    def MergeClassWorkflowInstanceList(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.mergeClassWorkflowInstanceList_btn)

    #退费申请
    feedBackFeeWorkflowInstanceList_btn = "link_text=>退费申请"
    def FeedBackFeeWorkflowInstanceList(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.feedBackFeeWorkflowInstanceList_btn)

    #拆分订单
    sepeateOrder_btn = "link_text=>拆分订单"
    def SepeateOrder(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.sepeateOrder_btn)

    #转班申请
    changeClassWorkflowInstanceList_btn = "link_text=>转班申请"
    def ChangeClassWorkflowInstanceList(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.changeClassWorkflowInstanceList_btn)

    #重读申请
    reReadWorkflowInstanceList_btn = "link_text=>重读申请"
    def ReReadWorkflowInstanceList(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.reReadWorkflowInstanceList_btn)

    #教师补考情审核
    fillTeacherRate_btn = "link_text=>教师补考勤审核"
    def FillTeacherRate(self):
        self.click(self.business_auditing_btn)
        time.sleep(2)
        self.click(self.fillTeacherRate_btn)


    #”优惠管理“模块
    discount_manage_btn = "xpath=>//span[contains(text(),'优惠管理')]"
    #优惠设置
    preferential_btn = "link_text=>优惠设置"
    def Preferential(self):
        self.click(self.discount_manage_btn)
        time.sleep(2)
        self.click(self.preferential_btn)


    #”流程管理“模块
    workflow_manage_btn = "xpath=>//span[contains(text(),'流程管理')]"
    #流程设置
    workflowConfig_btn = "link_text=>流程设置"
    def WorkflowConfig(self):
        self.click(self.workflow_manage_btn)
        time.sleep(2)
        self.click(self.workflowConfig_btn)


    #”支付管理“模块
    pay_manege_btn = "xpath=>//span[contains(text(),'支付管理')]"
    #汇款管理
    bankinSlip_btn = "link_text=>汇款管理"
    def BankinSlip(self):
        self.click(self.pay_manege_btn)
        time.sleep(2)
        self.click(self.bankinSlip_btn)

    #汇款查询
    bankinSlipSearch_btn = "link_text=>汇款查询"
    def BankinSlipSearch(self):
        self.click(self.pay_manege_btn)
        time.sleep(2)
        self.click(self.bankinSlipSearch_btn)

    #银行汇款导入历史
    bankinSlipImportHistory_btn = "link_text=>银行汇款导入历史"
    def BankinSlipImportHistory(self):
        self.click(self.pay_manege_btn)
        time.sleep(2)
        self.click(self.bankinSlipImportHistory_btn)

    #智能pos机管理
    posInfo_btn = "link_text=>智能pos机管理"
    def PosInfo(self):
        self.click(self.pay_manege_btn)
        time.sleep(2)
        self.click(self.posInfo_btn)

    #应收账款管理
    receivables_btn = "link_text=>应收账款管理"
    def Receivables(self):
        self.click(self.pay_manege_btn)
        time.sleep(2)
        self.click(self.receivables_btn)

    #应收账款回款
    receivablesRecover_btn = "link_text=>应收账款回款"
    def ReceivablesRecover(self):
        self.click(self.pay_manege_btn)
        time.sleep(2)
        self.click(self.receivablesRecover_btn)


    #“系统管理”模块（未写）