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

# click on admin
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(4)

# JOB Section Starts

# click on job

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a').click()
time.sleep(3)
# ADD BUTTON
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(3)

jobTitle = 'Quality'
jobDesc = 'A Q/A (Quality Assurance) job involves testing software or products to ensure they meet specified standards, identifying defects, and collaborating with teams to enhance quality.'

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys(jobTitle)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea').send_keys(jobDesc)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea').send_keys(jobDesc)
time.sleep(3)
driver.execute_script("window.scrollTo(0,1200 )")
driver.implicitly_wait(4)
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]').click()
time.sleep(15)

# PAY GRADE SECTION

userName = "Pratham Vishwakarma"
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a').click()
time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
# time.sleep(4)
# ADD BUTTON
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(4)
# ADD A PAY GRADE
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input').send_keys(userName)
time.sleep(4)
# SAVE BUTTON
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(10)

# EMPLOYMENT STATUS SECTION

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a').click()
time.sleep(4)

# ADD BUTTON
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(4)
# Add Name
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys(userName)
time.sleep(4)
# Save Button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(10)

# Job Categories Section


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]/a').click()
time.sleep(4)

# Add Button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(4)
# Name
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys(userName)
time.sleep(4)
# save button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(10)

# Work Shift section

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]/a').click()
time.sleep(4)

# Add button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(4)
# shift name
shiftName = "General"
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input').send_keys(shiftName)
time.sleep(4)
driver.execute_script("window.scrollTo(0,1000 )")
# driver.implicitly_wait(4)
time.sleep(4)
# for time

# start time
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[1]/input').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/i[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/i[1]').click()
time.sleep(2)

# end time
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[1]/input').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/i[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/i[1]').click()
time.sleep(4)

# employee name
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[1]/input').send_keys(userName)
time.sleep(4)
# Save button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]').click()
time.sleep(10)