from flip_kart_dd.pom_class.pom_filpkart import pm_cl
def test_add(_driver):
    obj_test = pm_cl(_driver)
    obj_test.close_login()
    obj_test.add_watch_to_cart()
    obj_test.add_refrigerator_to_cart()
    obj_test.add_bag_to_cart()
    obj_test.add_bluetooth_to_cart()
    obj_test.add_camera_to_cart()
    obj_test.cart_total_price_check()