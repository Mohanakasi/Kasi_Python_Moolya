from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get(r"https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[@aria-label='Google apps']").click()
sleep(10)
driver.execute_script("document.getElementsByClassName('tX9u1b')[4].click();")
# driver.find_element(By.XPATH, "//span[text()='YouTube']/../..//span[@class='MrEfLc']").click()
# driver.find_element(By.CSS_SELECTOR, "span[style='background-position: 0 -2378px;']").click()
# res = driver.find_element(By.XPATH, "//li[@class='j1ei8c']/..//a[contains(@href, 'https://www.youtube.com')]")

# sleep(5)
# assert youtube_el_text.text == 'YouTube'
# sleep(6)
# you_tube_el = driver.find_element(By.XPATH, "//span[text()='YouTube']/..//div[@class='CgwTDb']")
# var1.move_to_element(you_tube_el).click().perform()
