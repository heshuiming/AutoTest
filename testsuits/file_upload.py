from selenium import webdriver
from time import sleep

def upload():
    driver = webdriver.Chrome()
    driver.get("http://test.gedu.pxjy.com")
    driver.implicitly_wait(10)
    driver.find_element_by_name("loginName").send_keys("heshuiming@pxjy.com")
    driver.find_element_by_name("password").send_keys("heshuiming@123")
    driver.find_element_by_name("password").submit()

    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//span[contains(text(),'青龙')]").click()
    driver.implicitly_wait(10)

    search_window = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != search_window:
            driver.switch_to.window(handle)

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//i[@class='fa fa-pencil-square']").click()

    driver.implicitly_wait(10)
    driver.find_element_by_link_text("活动管理").click()

    sleep(10)
    driver.find_element_by_xpath("//td[@datano='0']/button[@data-id='2251'][@class='operation btn-import btn btn-danger  btn-sm m-r-10']").click()

    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//div[@class='col-md-9']/input[@name='upFile']").send_keys("D://ChromeDownload//活动资源.xlsx")

    sleep(3)
    driver.find_element_by_id("import-btn").click()
    sleep(10)


upload()