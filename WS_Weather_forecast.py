# Acquiring the website's source codes
import requests # Import the requests library
import xlsxwriter
page=requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
print(page) # Checking the result of the source codes collection
from bs4 import BeautifulSoup # Import the BeautifulSoup library
soup=BeautifulSoup(page.text,'lxml') # Define the soup
match=soup.find(id='seven-day-forecast') # Narrowing down to 'seven-day-forecast'
# print(match)
period_name=match.find_all('p',class_='period-name')
# print(period_name)
container=match.find_all('div',class_='tombstone-container')
now=container[0]
# print(now)
period=match.find(class_='period-name').get_text()
description=match.find(class_='short-desc').get_text()
temp=match.find(class_="temp").get_text()
# print(period+'\n'+description+'\n'+temp)
period_tags=match.select('.tombstone-container .period-name') # Select things satisfy these two conditions
periods=[ps.get_text() for ps in period_tags] # Put these things in the list called periods
desc=[sd.get_text() for sd in match.select('.tombstone-container .short-desc')]
temp=[tp.get_text() for tp in match.select('.tombstone-container .temp')]
import pandas
weather=pandas.DataFrame({'period':periods,'description':desc,'temperature':temp})
print(weather)
weather.to_csv('weather.csv')




