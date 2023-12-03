from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj) #using chrome service class in selenium
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# driver.quit()
# driver.close()

"locators"
sleep(3)
user_name_we = driver.find_element(By.NAME, 'username').send_keys('Admin')
# user_name_we = driver.find_element(By.CLASS_NAME, 'oxd-input oxd-input--active').send_keys('Admin')
password_text = driver.find_element(By.NAME, 'password').send_keys('admin123')
login_button = driver.find_element(By.XPATH, "//div//button[text()=' Login ']").click()
"navigation commands"
# driver.refresh()
# driver.forward()
# driver.back()
sleep(3)
driver.find_element(By.XPATH, "(//a[@class='oxd-main-menu-item'])[2]").click()
sleep(3)
driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys('ch')
sleep(5)
elem_s = driver.find_elements(By.XPATH, "//div[@role='listbox']//div[@role='option']")
for elem in elem_s:
    if elem.text == 'Charlie Carter':
        elem.click()
        break

sleep(3)

s_dd = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']//div[@class='ui-menu-item-wrapper']")
for elem in s_dd:
    if elem.text == "India":
        elem.click()
sleep(10)