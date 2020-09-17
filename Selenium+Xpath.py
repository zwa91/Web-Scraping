#Importing packages
from selenium import webdriver
import requests
import pandas as pd

driver=webdriver.Chrome(r'C:\Users\Python\chromedriver.exe')
driver.get('https://www.edmunds.com/truck/')

element_1=driver.find_element_by_xpath('//*[@id="401838298-heading"]/a')
element_2=driver.find_element_by_xpath('//*[@id="401780675-heading"]/a')
element_3=driver.find_element_by_xpath('//*[@id="401786252-heading"]/a')
truck_name=[element_1.text,element_2.text,element_3.text]
print(truck_name)


truck_price_element=driver.find_element_by_xpath\
    ('/html/body/div[1]/div/main/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]/div/div[3]/dl[1]/dd')
truck_price=truck_price_element.text
print(truck_price)



