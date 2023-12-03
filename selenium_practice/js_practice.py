from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
# get method to launch the URL
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.maximize_window()
# # to enter text in edit box
# sleep(5)
# # extract the value with Javascript Executor
# s = driver.find_element(By.CLASS_NAME, "search-keyword")
# print(driver.execute_script("arguments[0].value='ca';",s)) #working
# sleep(5)
# driver.implicitly_wait(0.5)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(5)
# # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #working
# s = driver.find_element(By.XPATH, "//img[@ALT='Picture of 14.1-inch Laptop']")
# driver.execute_script("arguments[0].scrollIntoView(true);",s) #working
# sleep(5)
# driver.implicitly_wait(0.5)
# driver.get("https://www.tutorialspoint.com/tutor_connect/index.php")
# # to scroll till page bottom
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# sleep(5)


driver.implicitly_wait(0.5)
driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
sleep(5)
s = driver.find_element(By.XPATH, "(//table[@id='product'])[2]/tbody/tr[2]/td[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", s)
sleep(5)
print(driver.execute_script("return arguments[0].innerText;",s))#working
driver.execute_script("window.scrollTo(0,0);")
driver.execute_script("document.getElementsByClassName('radioButton')[0].click();")
print(driver.execute_script("return document.getElementsByClassName('radioButton')[0].label;"))

#preceeding sibling (//table[@id='product'])[2]/tbody/tr[2]/td[2]/preceding-sibling::td
#following element (//table[@id='product'])[2]/tbody/tr[2]/td[2]/following::td[1]
sleep(5)
# driver.find_element(By.XPATH, "//a[text()='Open Tab']").click()
# w_hands = driver.window_handles
# print(w_hands)
# driver.switch_to.window(w_hands[-1])
# sleep(5)
# driver.get(r"https://demoqa.com/frames")
# driver.switch_to.frame("frame2")
# text_frame2 = driver.find_element(By.ID, "sampleHeading").text
# print(text_frame2)
# driver.switch_to.default_content()
# print(driver.title)
# sleep(5)


