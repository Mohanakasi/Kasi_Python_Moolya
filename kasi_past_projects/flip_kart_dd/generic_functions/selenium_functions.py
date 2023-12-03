from selenium.webdriver.support.select import Select
from flip_kart_dd.generic_functions.wat_deco import wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from openpyexcel import load_workbook, Workbook
from time import sleep
import re
wb = load_workbook(r"C:\development\pom_frame_work\flip_kart_dd\test_dat_files\test_data_fk.xlsx")
class Data_class:
    pass
def run_read_XPATH_data():
    ws = wb['XPATH']
    rows = ws.max_row
    col = ws.max_column
    for i in range(2, rows + 1):
        print(ws['B' + str(i)].value)
        for j in range(1, col + 1):
            setattr(Data_class, ws['A' + str(i)].value, eval(ws['B' + str(i)].value))
def run_read_product_information():
    ws1 = wb['product_information']
    rows = ws1.max_row
    col = ws1.max_column
    for i in range(2, rows + 1):
        print(type(ws1['B' + str(i)].value))
        for j in range(1, col + 1):
            setattr(Data_class, f'item{i-1}',ws1['A' + str(i)].value)
            setattr(Data_class, ws1['A' + str(i)].value, ws1['B' + str(i)].value)


class selenium_wrapper:

    def __init__(self,driver):
        self.driver = driver
        run_read_XPATH_data()
        run_read_product_information()

    @wait #click_element = wait(click_element) #click_element becomes wrapper
    def click_element(self,locator):  #locator--->("class name","ico-register")
        self.driver.find_element(*locator).click() #---> *locator---> "class name","ico-register"

    @wait
    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value, Keys.ENTER) # driver.find.element(By.ID, "FirstName")

    @wait
    def mouse_hover(self, locator):
        a = ActionChains(self.driver)
        ele_ = self.driver.find_element(*locator)
        a.move_to_element(ele_).perform()

    @wait
    def select_items(self,locator,value):
        web_el = self.driver.find_element(*locator)
        s = Select(web_el)
        if isinstance(value, str):
            s.select_by_visible_text(value)
        elif isinstance(value, int):
            s.select_by_index(value)
        else:
            raise TypeError

    def page_down(self):
        a = ActionChains(self.driver)
        a.send_keys(Keys.PAGE_DOWN).perform()

    def window_switch(self, window_num):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[window_num])
        sleep(5)
    
    def get_text_web_el(self, locator):
        return self.driver.find_element(*locator).text
    
    def data_add_excel(self, sheet_name, item_name, price, cell1, cell2):
        ws2 = wb[sheet_name]
        ws2[cell1] = item_name
        ws2[cell2] = price
        wb.save(r"C:\Users\User\PycharmProjects\kasi_test_yantra\Shruthi_HK\test_dat_files\test_data_fk.xlsx")


    def add_more_items(self, item_name, quanity):
        print(quanity)
        print(item_name)
        self.driver.find_element(By.XPATH,f"//a[contains(text(), '{item_name}')]/../../../..//input[@class='_253qQJ']").clear()
        self.enter_text((By.XPATH, f"//a[contains(text(), '{item_name}')]/../../../..//input[@class='_253qQJ']"), quanity)

    @wait
    def clear_search_field_home_page(self, locator):
        self.driver.find_element(*locator).clear()


    def price_check(self, item_price, total_):
        web_els = self.driver.find_elements(*item_price)
        total_price = int("".join(re.findall("\d", self.get_text_web_el(Data_class.total_price_cart_check_0ut))))
        els_text = []
        for i in web_els:
            els_text.append(int("".join(re.findall("\d", i.text))))

        return  sum(els_text), total_price