# from selenium import webdriver
# chrome_driver_path = "C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.daraz.com.np/products/usb-wired-joystick-gamepad-joypad-controller-for-xbox-360-console-pc-windows-i101368612-s1022152493.html?spm=a2a0e.searchlist.list.1.27ab78f5eHmJQN&search=1")
# driver.close()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# timer_count = 100
# service = Service("C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# driver.get("https://www.daraz.com.np/products/usb-wired-joystick-gamepad-joypad-controller-for-xbox-360-console-pc-windows-i101368612-s1022152493.html?spm=a2a0e.searchlist.list.1.27ab78f5eHmJQN&search=1")
# # driver.execute_script("window.onbeforeunload = function() { timer_count=0 };")
# # price = driver.find_element(By.CSS_SELECTOR,"#module_product_price_1 .pdp-mod-product-price .pdp-product-price .pdp-price")
#
# #Using Xpath
# price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span')
#
# print(price.text)
# time.sleep(timer_count)
# import time
# from pprint import pprint
#
# #----------------------------------------------Challenge 1---------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service("C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://www.python.org/")
# # event_date = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time').text
# event_date = driver.find_elements(By.CSS_SELECTOR,".event-widget .shrubbery .menu time")
# event_info = driver.find_elements(By.CSS_SELECTOR,".event-widget .shrubbery .menu a")
# event_date_list = [date.text for date in event_date]
# event_info_list = [info.text for info in event_info]
# challenge_dict = {}
# for i in range(len(event_date_list)):
#     challenge_dict[0] = {
#         "time":event_date_list[i],
#         "name": event_info_list[i]
#     }
#     # challenge_dict2 = {
#     #     i : {
#     #         "time": event_date_list[i],
#     #         "name": event_info_list[i]
#     #     }
#     # }
#     # challenge_dict.update(challenge_dict2)
# pprint(challenge_dict)
# # print(event_date_list)
# # print(event_info_list)
#----------------------------------Challenge 2 ----------------------------------------------
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# service = Service("C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe")
# driver = webdriver.Chrome(service=service,options=options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # article_number = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# # article_number.click()
#
# # all_portals = driver.find_element(By.LINK_TEXT,"English")
# # all_portals.click()
#
# search_bar = driver.find_element(By.NAME,"search")
# search_bar.send_keys("Nepal")
# search_bar.send_keys(Keys.ENTER)
#
# # print(article_number)
# # time.sleep(500)

#--------------------------------------------Challenge 3-------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# service = Service("C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe")
# driver = webdriver.Chrome(service=service,options=options)
# driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
# first_name = driver.find_element(By.NAME,"fName")
# second_name = driver.find_element(By.NAME,"lName")
# email = driver.find_element(By.NAME,"email")
# submit_btn = driver.find_element(By.XPATH,'/html/body/form/button')
# first_name.send_keys("Nomat")
# second_name.send_keys("NinetyFour")
# email.send_keys("abc@gmail.com")
# submit_btn.click()

#-------------------------------------------------Challenge 4 Cookie Clicker-------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
#
buy_it = 0
click_on = True
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service = Service("C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=service,options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH,'//*[@id="cookie"]')
items = driver.find_elements(By.CSS_SELECTOR,'#store div b')
items_price = [int(item.text.split()[-1].replace(",","")) for item in items if items.index(item)<len(items)-2]
timeout = time.time() + 5
timer_5min = time.time() + 60*5
print(items)
print(items_price)
# while click_on:
#     cookie.click()
#     if time.time()>timeout:
#         money = int(driver.find_element(By.XPATH,'//*[@id="money"]').text.replace(",",""))
#         print(money)
#         for price in items_price:
#             buy_it = 0
#             if money >= price:
#                 buy_it = price
#         items[items_price.index(buy_it)].click()
#         timeout = time.time() + 5























