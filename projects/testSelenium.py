from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
driver.get("http://3.222.215.204:8080/")

userName = driver.find_element(by=By.NAME, value='j_username')
userPass = driver.find_element(by=By.NAME, value='j_password')
userName.send_keys('devops')
userPass.send_keys('devops')
submitButton = driver.find_element(by=By.NAME, value='Submit')
submitButton.click()

time.sleep()

