# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# input_reg_email = driver.find_element_by_id("reg_email").send_keys("kaniviki@yandex.ru")
# time.sleep(2)
# input_reg_password = driver.find_element_by_id("reg_password").send_keys("Twowrongsdon'tmakearight31")
# time.sleep(2)
# click_butn_register = driver.find_element_by_name("register").click()
# driver.quit()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 5)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# input_email = driver.find_element_by_id("username").send_keys("kaniviki@yandex.ru")
# input_password = driver.find_element_by_id("password").send_keys("Twowrongsdon'tmakearight31")
# click_butn_login = driver.find_element_by_name("login").click()
# btn_logout_visible = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
# driver.quit()