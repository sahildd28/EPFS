from selenium import webdriver
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from selenium import webdriver

options=webdriver.ChromeOptions()
# options.add_argument('headless') 
browser=webdriver.Chrome(options=options)
browser.get("https://www.amazon.in/")
browser.implicitly_wait(5)
browser.maximize_window()
browser.get("https://www.flipkart.com/")
browser.implicitly_wait(5)
cross_login=browser.find_element_by_xpath("/html/body/div[2]/div/div/button")
cross_login.submit()
m_input="iphone XR"
search2=browser.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search2.send_keys(m_input)
submit2=browser.find_element_by_css_selector("#nav-search-submit-button")
submit2.submit()  