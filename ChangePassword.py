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
# driver.find_element(By.XPATH,'//input[@placeholder="Username"]').click()
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys(user)
time.sleep(2)
# driver.find_element(By.XPATH,'//input[@placeholder="Password"]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(passs)
time.sleep(3)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)
driver.find_element("xpath",'//input').send_keys("hello", Keys.ENTER)
time.sleep(10)
driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
driver.implicitly_wait(3)
time.sleep(3)
driver.find_element(By.CLASS_NAME, "oxd-userdropdown-link").click()
driver.implicitly_wait(2)
time.sleep(2)
# oxd-dialog-close-button oxd-dialog-close-button-position
driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div/div/button").click()
driver.implicitly_wait(2)
time.sleep(2)
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
driver.implicitly_wait(2)
time.sleep(2)
# driver.find_element(By.CLASS_NAME, "").click()
driver.find_element(By.XPATH, "//a[text()='Support']").click()
driver.implicitly_wait(2)
time.sleep(2)
# Again for dropdown
driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
driver.implicitly_wait(2)
time.sleep(2)
driver.find_element("link text", "Change Password").click()
driver.implicitly_wait(3)
time.sleep(3)

newPassword ="admin1234"
confirmNewPassword = "admin1234"

# To Change Password
driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys(passs)
driver.implicitly_wait(2)
time.sleep(2)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(newPassword)
driver.implicitly_wait(2)
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-input--active").send_keys(confirmNewPassword)
# <input data-v-1f99f73c="" class="oxd-input oxd-input--active" type="password" autocomplete="off">
driver.implicitly_wait(2)
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(2)
time.sleep(2)
# //input[@class='oxd-input oxd-input--focus']

