import requests
import html
# from bs4 import BeautifulSoup
# import lxml
# daraz_item = html.unescape(requests.get("https://www.daraz.com.np/products/usb-wired-joystick-gamepad-joypad-controller-for-xbox-360-console-pc-windows-i101368612-s1022152493.html?spm=a2a0e.searchlist.list.1.496778f5DILu06&search=1").text)
# soup = BeautifulSoup(daraz_item,"lxml")
# # print(soup)
# # with open("daraz.html",mode="w",encoding="utf-8") as file:
# #     file.write(daraz_item)
# # print(soup)
# price = soup.select_one(selector="#module_product_price_1 .pdp-mod-product-price .pdp-product-price .pdp-price")
# print(price)
# # print(price.getText())
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
my_email = "pythontest3967@gmail.com"
my_password = "ruevmynqbbpslzkk"
service = Service("C:\\Users\\dxngr\\Desktop\\chrome_driver\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=service,options=options)
driver.get("https://www.daraz.com.np/products/xbox-360-console-pc-windows-usb-wired-joystick-gamepad-joypad-controller-i111995726-s1030293946.html?spm=a2a0e.searchlist.list.1.6ad878f5t1POKu&search=1")
price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span')
print(price.text)
# time.sleep(100)
