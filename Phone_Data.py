from selenium import webdriver
from selenium.webdriver.support.ui import Select  #for dropdown menu
import time

driver = webdriver.Chrome()
driver.get("http://linuxjobber.com")
driver.implicitly_wait(15)


click_attempt = driver.find_element_by_xpath("//a[@href='/users/login']")
click_attempt.click()

time.sleep(1)

userName = driver.find_element_by_id("UserUsername")
userName.send_keys("")#input username

time.sleep(1)

password = driver.find_element_by_id("UserPassword")
password.send_keys("")#input password

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

#Name =driver.find_element_by_link_text("sirbossakej").click()
attempt = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/']")
attempt.click()

driver.get("https://linuxjobber.com/users/schedule")
time.sleep(1)

s1 = Select(driver.find_element_by_id("day"))
s1.select_by_index(1)

s2 = Select(driver.find_element_by_id("time"))
s2.select_by_index(5)

s3 = Select(driver.find_element_by_name("data[Schedule][mode]"))
s3.select_by_index(1)

s4 = Select(driver.find_element_by_id("day_2"))
s4.select_by_index(5)

s5 = Select(driver.find_element_by_id("time_2"))
s5.select_by_index(8)

s6 = Select(driver.find_element_by_name("data[Schedule][mode_2]"))
s6.select_by_index(1)

s7 = Select(driver.find_element_by_id("country"))
s7.select_by_index(40)

time.sleep(1)

lastName = driver.find_element_by_id("phone")
lastName.send_keys("9039423428")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

driver.quit()