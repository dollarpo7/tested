from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
# driver.implicitly_wait(15)
# driver.get("https://www.google.com/")
# searchfield = driver.find_element_by_css_selector("input[name=d")



driver.get("https://linuxjobber.com/")


logIn = driver.find_element_by_xpath(".//a[@href='/users/login']").click()

userName = driver.find_element_by_id("UserUsername")
userName.send_keys("dollarpo7")

password = driver.find_element_by_id("UserPassword")
password.send_keys("folarin7")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

go = driver.find_element_by_xpath('//a[contains(text(), "dollarpo7")]').click()

select = driver.get("http://linuxjobber.com/users/accountSetting")

elect = driver.find_element_by_xpath('//button[contains(text(), "Launch A New Instance")]').click()

driver.quit()