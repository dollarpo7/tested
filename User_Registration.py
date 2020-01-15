from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://linuxjobber.com")
driver.implicitly_wait(10)


click = driver.find_element_by_xpath("//a[@href='/freeuser']")
click.click()

time.sleep(1)

userName = driver.find_element_by_id("UserFullName")
userName.send_keys("tred")

time.sleep(1)

mail = driver.find_element_by_id("email")
mail.send_keys("tred@gmail.com")

time.sleep(1)

password = driver.find_element_by_id("UserPassword")
password.send_keys("tred")

time.sleep(1)

submit = driver.find_element_by_xpath("//*[@type='submit']")
submit.click()


userName = driver.find_element_by_id("UserUsername")
userName.send_keys("tred")

time.sleep(1)

password = driver.find_element_by_id("UserPassword")
password.send_keys("tred")

select = driver.find_element_by_xpath("//*[@type='submit']")
select.click()

driver.quit()