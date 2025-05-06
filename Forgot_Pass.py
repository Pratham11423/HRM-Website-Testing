# Jai Shree Ram

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
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input').send_keys(user)
time.sleep(5)

# reset btn
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
time.sleep(8)

