import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

browser = webdriver.Chrome()
hashtag = 'Candles4SSR'
url = 'https://twitter.com/hashtag/'+hashtag+'?src=hashtag_click'
browser.get(url)
time.sleep(1)
body = browser.find_element_by_tag_name('body')

tweet_contents = []
for _ in range(5):
    tweets = browser.find_elements_by_css_selector("[data-testid=\"tweet\"]")
    
    for tweet in tweets:
        print(tweet.text)
        tweet_contents += [tweet.text]
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.4)