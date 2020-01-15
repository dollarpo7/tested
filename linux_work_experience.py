from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome()


driver.get("http://linuxjobber.com")


click = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/homes/workexperience']")
click.click()


attempt = driver.find_element_by_xpath("//a[@href='https://linuxjobber.com/homes/pay/workexperience']")
attempt.click()


userName = driver.find_element_by_id("UserUsername")
userName.send_keys("")  #input username

password = driver.find_element_by_id("UserPassword")
password.send_keys("") #input password

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

click_attempt = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/homes/workexperience']")
click_attempt.click()

click_attempt = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/homes/pay/workexperience']")
click_attempt.click()

payCard = driver.find_element_by_xpath("//*[@type='submit']")
payCard.click()

driver.switch_to.frame("stripe_checkout_app")

cardNumber =  driver.find_element_by_xpath("//*[@type='tel']")
cardNumber.send_keys("42424242424242424")

date = driver.find_element_by_xpath("//*[@placeholder='MM / YY']")
date.send_keys("0318")

cvc = driver.find_element_by_xpath("//*[@placeholder='CVC']")
cvc.send_keys("1234")

pay = driver.find_element_by_xpath("//*[@type='submit']")
pay.click()

driver.quit()