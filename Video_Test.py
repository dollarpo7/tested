from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("http://linuxjobber.com")

#driver.execute_script("window.scrollTo(1,10);")

logIn = driver.find_element_by_xpath(".//a[@href='/users/login']").click()

userName = driver.find_element_by_id("UserUsername")
userName.send_keys("dollarpo7")

time.sleep(1)

password = driver.find_element_by_id("UserPassword")
password.send_keys("folarin7")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

time.sleep(2)

driver.get("http://linuxjobber.com")

time.sleep(2)

select = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/tutorials/coursedescription/LINUX-FUNDAMENTALS']")
select.click()

time.sleep(2)

driver.get("https://linuxjobber.com/Tutorials/basics_of_linux_lectures")

#ENROLL NOW
'''login_attempt = driver.find_element_by_link_text("ENROLL NOW")
login_attempt.click()'''

time.sleep(1)

key1 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/1/1']").click()

time.sleep(1)

driver.get("https://linuxjobber.com/Tutorials/basics_of_linux_lectures")

time.sleep(1)

key2 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/116/1']").click()

time.sleep(1)

elect = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/']")
elect.click()

time.sleep(1)
#******************************************2nd course***********************************************************************************************************************

cry = driver.get("https://linuxjobber.com/tutorials/coursedescription/PUPPET-TRAINING")

time.sleep(1)

driver.get("https://linuxjobber.com/Tutorials/puppet")

time.sleep(1)

login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

time.sleep(1)

key3 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/31/3']").click()

time.sleep(1)

driver.get("https://linuxjobber.com/Tutorials/puppet")

time.sleep(1)

login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()


key4 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/35/3']").click()

time.sleep(1)

elect2 = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/']")
elect2.click()

time.sleep(1)
#******************************************3rd course***********************************************************************************************************************

'''click3 = driver.find_element_by_xpath("//a[@href='http://linuxjobber.com/tutorials/coursedescription/RHCSA']")
click3.click()

time.sleep(1)

driver.get(".//a[@href='']")

time.sleep(1)

login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

time.sleep(1)

key3 = driver.find_element_by_xpath(".//a[@href='']").click()

time.sleep(1)


time.sleep(1)

key3 = driver.find_element_by_xpath(".//a[@href='/users/access_course']").click()

time.sleep(1)

elect3 = driver.find_element_by_xpath("//a[@href='http://linuxjobber.com/']")
elect3.click()

time.sleep(1)
'''
#******************************************4th course***********************************************************************************************************************
click4 = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/tutorials/coursedescription/JAVA']")
click4.click()

time.sleep(1)

log4 = driver.get("https://linuxjobber.com/Tutorials/java")

time.sleep(1)


login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

time.sleep(1)

key5 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/54/6']").click()

time.sleep(1)

driver.get("https://linuxjobber.com/Tutorials/java")

time.sleep(1)



login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

key6 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/74/6']").click()

time.sleep(1)

elect4 = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/']")
elect4.click()

time.sleep(1)

#******************************************5th course***********************************************************************************************************************

click5 = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/tutorials/coursedescription/AWS']")
click5.click()

time.sleep(1)

log5 = driver.get("https://linuxjobber.com/Tutorials/aws")


time.sleep(1)

login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

time.sleep(1)

key6 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/49/4']").click()

time.sleep(1)

driver.get("https://linuxjobber.com/Tutorials/aws")

time.sleep(1)



login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

key7 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/53/4']").click()

time.sleep(1)

elect5 = driver.find_element_by_xpath("//a[@href='http://linuxjobber.com/']")
elect5.click()

time.sleep(1)

#******************************************6th course***********************************************************************************************************************

click6 = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/tutorials/coursedescription/BUSINESS-ANALYSIS']")
click6.click()

time.sleep(1)

log6 = driver.get("https://linuxjobber.com/Tutorials/businessanalysis")
time.sleep(1)

login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()

time.sleep(1)

key8 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/75/7']").click()

time.sleep(1)

driver.get("https://linuxjobber.com/Tutorials/businessanalysis")

time.sleep(1)

login_attempt = driver.find_element_by_link_text("Load More Topics")
login_attempt.click()



key9 = driver.find_element_by_xpath(".//a[@href='/tutorials/lab_video/83/7']").click()

time.sleep(1)

elect6 = driver.find_element_by_xpath("//a[@href='http://linuxjobber.com/']")
elect6.click()

time.sleep(2)

driver.quit()
