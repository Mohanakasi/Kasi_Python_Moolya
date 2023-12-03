import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
# driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# # driver.minimize_window()
# # print(driver.current_url)
# # print(driver.title)
# # driver.close()
# # driver.quit()
# driver.find_element(By.NAME, "dropdown-class-example").click()
# time.sleep(3)
# driver.find_element(By.NAME, "enter-name").send_keys("Moahan kasi")
# driver.find_element(By.ID, "checkBoxOption1").click()
# driver.find_element(By.ID, "autocomplete").send_keys("Brazil")
# driver.find_element(By.LINK_TEXT, "Open Tab").click()

driver.get(r"https://www.python.org/downloads/")
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, "a[id='offers']").click()
# driver.find_element(By.CSS_SELECTOR, "a[class='Navbar_logo__26S5Y']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='/favourites']").click()
# driver.find_element(By.CSS_SELECTOR, "a#offers[href='/offers']").click()
# driver.find_element(By.CSS_SELECTOR, "a.Navbar_link__3Blki[href='/orders']").click()
