import self as self

import string
from random import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

EmployeeName = "Johny "
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("../Drivers/chromedriver.exe", 0, options)
driver.get("https://opensource-demo.orangehrmlive.com/")
wait = WebDriverWait(driver, 30)
print('--- Logging into Application ---')


def to_login(user_id, password):
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def Add_Employee():

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Add Employee']")))
    driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
    driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "firstName")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "firstName")))
    driver.find_element(By.NAME, "firstName").send_keys(EmployeeName)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "lastName")))
    driver.find_element(By.NAME, "lastName").send_keys("Rio")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def Add_NewUser(username):

    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Admin']")))
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
    driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(username)
    driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]").click()

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option']/span[text()='Admin']")))
    driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Admin']").click()


    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(EmployeeName)
    driver.implicitly_wait(10)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option']/span[text()='Johny   Rio']")))
    driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Johny   Rio']").click()

    driver.find_element(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]").click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option']/span[text()='Enabled']")))
    driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Enabled']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()='(1) Record Found']")))
    driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]").click()

def get_random_alpha_numeric_string(string_length = 16):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(string_length)))

def to_logout():
    driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Logout')))
    driver.find_element(By.LINK_TEXT, "Logout").click()
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    assert "OrangeHRM" in driver.title
    print('--- Logout Successful ---')


print("-- Login via admin credentials --")
to_login(user_id="Admin", password="admin123")
try:
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "PIM")))
    print('--- Login Successful ---\n')
    Add_Employee()
    Add_NewUser("Yeswanth")
    to_logout()
except NoSuchElementException:
    print("--- Login Failed ---\n")

print("-- Login via Admin User--")
driver.close()
