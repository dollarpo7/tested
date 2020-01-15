from selenium import webdriver
from selenium.webdriver.support.ui import Select  #for dropdown menu

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://linuxjobber.com/Jobplacements")



login_attempt = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/Jobplacements/apply']")
login_attempt.click()

firstName = driver.find_element_by_id("firstname")
firstName.send_keys("Adedolapo")

lastName = driver.find_element_by_id("lastname")
lastName.send_keys("Okunsanmi")

emailAddress = driver.find_element_by_id("email")
emailAddress.send_keys("okunsanmi.adedolapo@gmail.com")

s1 = Select(driver.find_element_by_id("education"))
s1.select_by_index(2)

file_input = driver.find_element_by_id('JobplacementsResume')
file_input.send_keys('C:\\Users\\Archibald\\Downloads\\Documents\\ch03.pdf')

submit = driver.find_element_by_id("but")
submit.click()

# close the browser window
driver.quit()






