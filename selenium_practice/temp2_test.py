from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# service_obj = Service()
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# dd = Select(driver.find_element(By.ID, 'dropdown-class-example'))
# dd.select_by_visible_text('Option1')
# dd.select_by_index(2)
# dd.select_by_value('option3')
#
# country_main = "India"
# driver.find_element(By.ID, 'autocomplete').send_keys('india')
# sleep(1)
#
# s_dd = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']//div[@class='ui-menu-item-wrapper']")
# for elem in s_dd:
#     if elem.text == country_main:
#         elem.click()
#         break
# sleep(10)
# passed_text = driver.find_element(By.ID, 'autocomplete').get_attribute('value')
# "asserts"
# assert country_main == passed_text
#
# "check box"
# check_box1 = driver.find_element(By.ID, 'checkBoxOption1')
# check_box1.click()
# print(check_box1.is_selected())
# "getting all elements and loop for particular element"
# check_box_list = driver.find_elements(By.XPATH, "//label//*[@type='checkbox']")
# print(check_box_list)
# sleep(3)
# for elem in check_box_list:
#     if elem.get_attribute("value") == 'option3':
#         elem.click()
# sleep(5)
#
# "alerts handling"
# text_main = 'Hello , share this practice page and share your knowledge'
# driver.find_element(By.XPATH, "//input[@value='Alert']").click()
# alt = driver.switch_to.alert #switching to pop-up
# text_got = alt.text #getting text from pop-up
# assert text_main in text_got
# sleep(5)
# alt.accept()

"synchronization"
"waits"
"implicit wait"
"explicit"
# driver.implicitly_wait(10)
# w_wait = WebDriverWait(driver, 10)
# w_wait.until(expected_conditions.visibility_of_element_located())

"sleep will hold the execution simply upto the time given"
"implicit wait hold the execution until the elements are loaded in DOM, if the elemens are loaded"
"earlier it will terminates  remaining time"
"explicit wait holds the execution until given condition being satisifed"

m_hov = ActionChains(driver)
m_hov.key_down(Keys.PAGE_DOWN)
sleep(5)
m_hov.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
sleep(5)
m_hov.click(driver.find_element(By.ID, "mousehover")).perform()
m_hov.key_down(Keys.ARROW_DOWN).perform()
sleep(5)
driver.switch_to.new_window('tab')
original_window = driver.current_window_handle
driver.switch_to.new_window('window')
driver.get("https://www.postman.com")
driver.find_element(By.XPATH, "(//input[@type='email'])[1]").send_keys('mohanakasi.s3@gmail.com')
driver.switch_to.window(original_window)
width = driver.get_window_size().get('width')
height = driver.get_window_size().get('height')
print(width, height)
# m_hov.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# m_hov.context_click(driver.find_element(By.XPATH, "//a[text()='Reload']")).perform()
# sleep(5)
# m_hov.send_keys(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# m_hov.key_down(Keys.CONTROL).send_keys('tab').key_up(Keys.CONTROL).perform()
sleep(10)
