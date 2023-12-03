from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
current_window = driver.current_window_handle
driver.switch_to.new_window('tab')
sleep(5)
driver.switch_to.window(current_window)
sleep(10)
driver.find_element(By.ID, "autocomplete").send_keys('Br')
sleep(4)
countries = driver.find_elements(By.XPATH, "//ul//div[@class='ui-menu-item-wrapper']")
print(countries)
for country in  countries:
    print(countries)
    if country.text == "Brazil":
        print("if is executed")
        country.click()
        break
a_ch = ActionChains(driver)
a_ch.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(10)
a_ch.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
a_ch.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()