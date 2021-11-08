# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# input_email = driver.find_element_by_id("username").send_keys("kaniviki@yandex.ru")
# input_password = driver.find_element_by_id("password").send_keys("Twowrongsdon'tmakearight31")
# click_butn_login = driver.find_element_by_name("login").click()
# click_btn_shop = driver.find_element_by_link_text("Shop").click()
# click_book = driver.find_element_by_css_selector(".post-181>:nth-child(1)").click()
# title_book_text = driver.find_element_by_css_selector("[itemprop='name']").text
# assert title_book_text == "HTML5 Forms"
# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# input_email = driver.find_element_by_id("username").send_keys("kaniviki@yandex.ru")
# input_password = driver.find_element_by_id("password").send_keys("Twowrongsdon'tmakearight31")
# click_butn_login = driver.find_element_by_name("login").click()
# click_btn_shop = driver.find_element_by_link_text("Shop").click()
# click_categ_html = driver.find_element_by_link_text("HTML").click()
# element_pages = driver.find_elements_by_css_selector(".products>li")
# if len(element_pages) == 3:
#     print("На странице отображается три товара")
# else:
#     print("На странице отображается меньше или больше трех товаров")
# driver.quit()

# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# input_email = driver.find_element_by_id("username").send_keys("kaniviki@yandex.ru")
# input_password = driver.find_element_by_id("password").send_keys("Twowrongsdon'tmakearight31")
# click_butn_login = driver.find_element_by_name("login").click()
# click_btn_shop = driver.find_element_by_link_text("Shop").click()
# default_sorting = driver.find_element_by_name("orderby").get_attribute("value")
# if default_sorting == "menu_order":
#     print("Выбрана сортировка по умолчанию")
# selector = driver.find_element_by_class_name("orderby")
# select = Select(selector)
# select.select_by_value("price-desc")
# sort_highToLow = driver.find_element_by_name("orderby").get_attribute("value")
# if sort_highToLow == "price-desc":
#     print("Выбрана сортировка от большего к меньшему")
# driver.quit()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# input_email = driver.find_element_by_id("username").send_keys("kaniviki@yandex.ru")
# input_password = driver.find_element_by_id("password").send_keys("Twowrongsdon'tmakearight31")
# click_butn_login = driver.find_element_by_name("login").click()
# click_btn_shop = driver.find_element_by_link_text("Shop").click()
# click_book = driver.find_element_by_css_selector(".post-169>:nth-child(1)").click()
# old_price = driver.find_element_by_css_selector("del>span").text
# assert old_price == "₹600.00"
# new_price = driver.find_element_by_css_selector("ins>span").text
# assert new_price == "₹450.00"
# EC_images = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "images")))
# click_images = driver.find_element_by_class_name("images").click()
# EC_butn_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# click_butn_close = driver.find_element_by_class_name("pp_close").click()
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 5)
# driver.get("http://practice.automationtesting.in/")
# click_btn_shop = driver.find_element_by_link_text("Shop").click()
# add_to_basket = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# basket = driver.find_element_by_class_name("wpmenucart-contents").text
# assert basket == "1 Item₹180.00"
# click_basket_btn = driver.find_element_by_class_name("wpmenucart-contents").click()
# EC_Subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']>span"), "₹180.00"))
# EC_Total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total']>strong"), "₹189.00"))
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# btn_shop_click = driver.find_element_by_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0,300);")
# add_basket_firstBook = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# add_basket_secondBook = driver.find_element_by_css_selector("[data-product_id='180']").click()
# basket_btn_click = driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(3)
# del_firstBook = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(3)
# Undo_click = driver.find_element_by_link_text("Undo?").click()
# qty_secondBook = driver.find_element_by_xpath("//tbody/tr[2]/td[5]/div/input")
# qty_secondBook.clear()
# qty_secondBook.send_keys("3")
# upd_basket_click = driver.find_element_by_name("update_cart").click()
# value_qty = driver.find_element_by_xpath("//tbody/tr[2]/td[5]/div/input").get_attribute("value")
# assert value_qty == "3"
# time.sleep(3)
# app_coupon_click = driver.find_element_by_name("apply_coupon").click()
# time.sleep(3)
# error_coupon = driver.find_element_by_css_selector(".woocommerce-error>li").text
# assert error_coupon == "Please enter a coupon code."
# driver.quit()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 5)
driver.get("http://practice.automationtesting.in/")
btn_shop_click = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0,300);")
add_basket_Book = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(3)
basket_btn_click = driver.find_element_by_class_name("wpmenucart-contents").click()
prot_checkBtn_EC = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")))
prot_checkBtn_click = driver.find_element_by_css_selector(".wc-proceed-to-checkout>a").click()
first_name_EC = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
input_first_name = driver.find_element_by_id("billing_first_name").send_keys("Test")
input_last_name = driver.find_element_by_id("billing_last_name").send_keys("Trest")
input_email = driver.find_element_by_id("billing_email").send_keys("test@gmail.com")
input_phone = driver.find_element_by_id("billing_phone").send_keys("+7(999)999-99-99")
selector_country_click = driver.find_element_by_id("select2-chosen-1").click()
search_country = driver.find_element_by_id("s2id_autogen1_search").send_keys("Ukraine")
country_click = driver.find_element_by_class_name("select2-match").click()
input_address = driver.find_element_by_id("billing_address_1").send_keys("Bolshaya Monetnaya")
input_town = driver.find_element_by_id("billing_city").send_keys("Saint Petersburg")
input_state = driver.find_element_by_id("billing_state").send_keys("Russia")
input_postcode = driver.find_element_by_id("billing_postcode").send_keys("197101")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
check_pay_click = driver.find_element_by_id("payment_method_cheque").click()
place_orderBtn_click = driver.find_element_by_id("place_order").click()
text_title_EC = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
text_payMeth_EC = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//tfoot/tr[3]/td"), "Check Payments"))
driver.quit()