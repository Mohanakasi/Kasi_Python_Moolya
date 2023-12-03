from flip_kart_dd.generic_functions.selenium_functions import Data_class,selenium_wrapper
from time import sleep
import re
class pm_cl(selenium_wrapper):

    def close_login(self):
        self.click_element(Data_class.close_login_btn)

    def add_watch_to_cart(self):
        self.enter_text(Data_class.search_field, Data_class.item1)
        self.mouse_hover(Data_class.item_watch)
        self.click_element(Data_class.item_watch)
        self.window_switch(1)
        sleep(3)
        item_name = self.get_text_web_el(Data_class.item_name_grab)
        price = self.get_text_web_el(Data_class.item_price_grab)
        self.data_add_excel("items_added_details", item_name, price, 'A2', 'B2')
        self.click_element(Data_class.add_to_cart_button)
        sleep(5)
        self.add_more_items(Data_class.item1.split('_')[0], Data_class.Fastrack_WATCH)
        sleep(10)
        self.window_switch(0)
        self.driver.back()
        self.driver.refresh()
        sleep(10)
        cart_count_after_add = int(self.get_text_web_el(Data_class.cart_count))
        assert cart_count_after_add == 1

    def add_refrigerator_to_cart(self):
        cart_count_before_add = int(self.get_text_web_el(Data_class.cart_count))
        self.enter_text(Data_class.search_field, Data_class.item2)
        sleep(5)
        self.mouse_hover(Data_class.refrigerator_select)
        self.click_element(Data_class.refrigerator_select)
        self.window_switch(2)
        sleep(3)
        item_name = self.get_text_web_el(Data_class.item_name_grab)
        price = self.get_text_web_el(Data_class.item_price_grab)
        self.data_add_excel("items_added_details", item_name, price, 'A3', 'B3')
        self.click_element(Data_class.add_to_cart_button)
        sleep(5)
        self.add_more_items(Data_class.item2.split('_')[0], Data_class.SAMSUNG_refrigerator)
        sleep(10)
        self.window_switch(0)
        self.driver.back()
        self.driver.refresh()
        sleep(10)
        cart_count_after_add = int(self.get_text_web_el(Data_class.cart_count))
        exact_count = cart_count_before_add+1
        assert exact_count == cart_count_after_add

    def add_bag_to_cart(self):
        cart_count_before_add = int(self.get_text_web_el(Data_class.cart_count))
        self.enter_text(Data_class.search_field, Data_class.item3)
        sleep(5)
        self.mouse_hover(Data_class.bag_select)
        self.click_element(Data_class.bag_select)
        self.window_switch(3)
        sleep(3)
        item_name = self.get_text_web_el(Data_class.item_name_grab)
        price = self.get_text_web_el(Data_class.item_price_grab)
        self.data_add_excel("items_added_details", item_name, price, 'A4', 'B4')
        self.click_element(Data_class.add_to_cart_button)
        sleep(5)
        self.add_more_items(Data_class.item3.split('_')[0], Data_class.SKYBAGS_backpack)
        sleep(10)
        self.window_switch(0)
        self.driver.back()
        self.driver.refresh()
        sleep(10)
        cart_count_after_add = int(self.get_text_web_el(Data_class.cart_count))
        exact_count = cart_count_before_add + 1
        assert exact_count == cart_count_after_add

    def add_bluetooth_to_cart(self):
        cart_count_before_add = int(self.get_text_web_el(Data_class.cart_count))
        self.enter_text(Data_class.search_field, Data_class.item4)
        sleep(5)
        self.mouse_hover(Data_class.blue_tooth)
        self.click_element(Data_class.blue_tooth)
        self.window_switch(4)
        sleep(3)
        item_name = self.get_text_web_el(Data_class.item_name_grab)
        price = self.get_text_web_el(Data_class.item_price_grab)
        self.data_add_excel("items_added_details", item_name, price, 'A5', 'B5')
        self.click_element(Data_class.add_to_cart_button)
        sleep(5)
        self.add_more_items(Data_class.item4.split('_')[0], Data_class.OnePlus_bluetooth)
        sleep(10)
        self.window_switch(0)
        self.driver.back()
        self.driver.refresh()
        sleep(10)
        cart_count_after_add = int(self.get_text_web_el(Data_class.cart_count))
        exact_count = cart_count_before_add + 1
        assert exact_count == cart_count_after_add


    def add_camera_to_cart(self):
        cart_count_before_add = int(self.get_text_web_el(Data_class.cart_count))
        self.enter_text(Data_class.search_field, Data_class.item5)
        sleep(5)
        self.mouse_hover(Data_class.camera)
        self.click_element(Data_class.camera)
        self.window_switch(5)
        sleep(3)
        item_name = self.get_text_web_el(Data_class.item_name_grab)
        price = self.get_text_web_el(Data_class.item_price_grab)
        self.data_add_excel("items_added_details", item_name, price, 'A6', 'B6')
        self.click_element(Data_class.add_to_cart_button)
        sleep(5)
        self.add_more_items(Data_class.item5.split('_')[0], Data_class.SONY_Camera)
        sleep(10)
        self.window_switch(0)
        self.driver.back()
        self.driver.refresh()
        sleep(10)
        cart_count_after_add = int(self.get_text_web_el(Data_class.cart_count))
        exact_count = cart_count_before_add + 1
        assert exact_count == cart_count_after_add

    def cart_total_price_check(self):
        self.click_element(Data_class.cart_link_home_page)
        sleep(5)
        expected_count = self.price_check(Data_class.item_prices_cart, Data_class.total_price_cart_check_0ut)
        print(expected_count)
        assert expected_count[0] == expected_count[1]
        self.data_add_excel("items_added_details", "Toatal_Price", expected_count[1], 'A7', 'B7')