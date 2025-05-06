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

# Organisation section start
# Click on Organisation dropdown
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span/i').click()
time.sleep(5)

# Click on general information
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a').click()
time.sleep(5)

# Click On edit button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div/label/span').click()
time.sleep(5)

# Organisation name

newName = "OrangeHRM 2.0"
name = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input')
name.clear()
time.sleep(2)
name.send_keys(newName)
time.sleep(8)

#  Registration no.
newNum = "160"
registrationNum = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
registrationNum.clear()
time.sleep(2)
registrationNum.send_keys(newNum)
time.sleep(8)


# FOR LOCATIONS
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span/i').click()
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a').click()
time.sleep(5)

# For Name

NewName = "Pratham"
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys(NewName)
time.sleep(5)

# For City

city = "Saharanpur"
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(city)
time.sleep(5)

# For Country
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i').click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[text()='India']").click()
time.sleep(5)

# click on add
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button').click()
time.sleep(4)

# enter name
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input').send_keys("Pratham Vishwakarma")
time.sleep(3)

# enter location
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Saharanpur")
time.sleep(3)

# enter state
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Uttar Pradesh")
time.sleep(3)

# enter postcode
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/input').send_keys("247001")
time.sleep(4)

# click on dropdown
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]').click()
time.sleep(4)

# Select india
driver.find_element(By.XPATH,"//*[text()='India']").click()
time.sleep(3)

# Phone
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/input').send_keys("1234567890")
time.sleep(3)

# Fax.no.
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[6]/div/div[2]/input').send_keys("32353254")
time.sleep(3)

# address
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[7]/div/div[2]/textarea').send_keys("street 1,brooklyn park")
time.sleep(3)

# notes
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[8]/div/div[2]/textarea').send_keys("Adding The Loaction")

# save button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
time.sleep(15)

# ORGANISATION STRUCTURE

# Click on Organisation dropdown
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span/i').click()
time.sleep(5)

# click on the Structure
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]/a').click()
time.sleep(5)

# click on edit button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/label/span').click()
time.sleep(3)

# click on the delete button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/ul/li/ul/li[1]/div[1]/div/div/div[2]/button[1]/i').click()
time.sleep(5)

# click on confirm delete
driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
time.sleep(5)

# click on the + icon
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/ul/li/ul/li[2]/div[1]/div/div/div[2]/button[3]/i').click()
time.sleep(4)

#enter the unit id
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/input').send_keys("12346")
time.sleep(3)

# enter the name
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/input').send_keys("Pratham Vishwakarma")
time.sleep(3)

# enter the desc.
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[3]/div/div[2]/textarea').send_keys("Jai Shree Ram")
time.sleep(3)

# click on the save button
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[4]/button[2]').click()
time.sleep(8)

