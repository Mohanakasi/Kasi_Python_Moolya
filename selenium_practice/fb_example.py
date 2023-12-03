from selenium import webdriver
from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# service_browser = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID, "email").send_keys('kasisettipalli@gmail.com')
a_ch = ActionChains(driver)
a_ch.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
a_ch.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
a_ch.send_keys(Keys.TAB).perform()
a_ch.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
a_ch.send_keys(Keys.ENTER).perform()
"using in single line"
# a_ch.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
#  .key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)\
#  .send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys('v')\
#  .key_up(Keys.CONTROL).perform()


