import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from matplotlib import pyplot as plt

browser = webdriver.Chrome()
browser.get("https://www.pcgarage.ro/notebook-laptop/asus/gaming-173-rog-strix-g731gt-fhd-procesor-intel-core-i7-9750h-12m-cache-up-to-450-ghz-8gb-ddr4-512gb-ssd-geforce-gtx-1650-4gb-no-os-black/")


PRICE_LOCATOR= "price_num"
elem = browser.find_element_by_class_name(PRICE_LOCATOR).text
pattern = '([0-9]+\.[0-9]+\,[0-9]+) RON'

matcher = re.search(pattern, elem)
price_list= matcher.group(1)
price_list= [e for e in price_list if e != '.' and e!= ',']
price_list.insert(4,'.')
price=''.join(price_list)
price=float(price) 

print(price)

browser.quit()