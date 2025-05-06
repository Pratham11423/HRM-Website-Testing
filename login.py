from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver = webdriver.Chrome()
# driver = webdriver.Chrome('C:\BSPLAut\chromedriver.exe')
driver.get(url)
driver.implicitly_wait(10)
user ="Admin"
passs ="admin123"
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').click()
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(user)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(passs)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)
# driver.find_element("xpath",'//input').send_keys("hello", Keys.ENTER)
# time.sleep(10)
# # driver.find_element(by:"xpath",value:'')
# # driver.find_element("xpath",'//input').click()
#
#
# # FOR DROPDOWN
# # dropdown = Select(driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img")).click()
# driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
# driver.implicitly_wait(3)
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, "oxd-userdropdown-link").click()
# driver.implicitly_wait(2)
# time.sleep(2)
# # oxd-dialog-close-button oxd-dialog-close-button-position
# driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
# driver.implicitly_wait(2)
# time.sleep(2)
# driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
# driver.implicitly_wait(2)
# time.sleep(2)
# # driver.find_element(By.CLASS_NAME, "").click()
# driver.find_element(By.XPATH, "//a[text()='Support']").click()
# driver.implicitly_wait(2)
# time.sleep(2)
# driver.find_element(By.CLASS_NAME, "oxd-dropdown-name").click()
# driver.implicitly_wait(2)
# time.sleep(2)

