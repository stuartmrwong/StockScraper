# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:03:03 2019

@author: Stuart
"""


'''
#This code launches a chrome browser using a driver. It then navigates to the ticker and shows you it.

import bs4 as bs
from selenium import webdriver  
browser = webdriver.Chrome('C:\chromedriver.exe')
url = ("https://www.google.com/finance?q=atvi")
browser.get(url)
html_source = browser.page_source

soup = bs.BeautifulSoup(html_source, "lxml")
for el in soup.find_all("table", {"id": "cc-table"}):
    print(el.get_text())
    
browser.quit()
'''

'''
#This code actually requests from google finance but it throws an xpath error
from lxml import html
import requests
import time

def parse(ticker):
    url = "http://www.google.com/finance?q=%s"%(ticker)
    response = requests.get(url, verify=False)
    parser = html.fromstring(response.content)
    price0 = parser.xpath('<span class="IsqQVc NprOob iyOsi8pI_fTE-zJFzKq8ukm8">47.33</span>')[0].text_content().strip()
    print(price0)
parse('ATVI')
'''


 
# yfinance is yahoo finance, its a package that easily grabs stock data
import yfinance as yf #yiff yiff 
from datetime import timedelta, date
from knockknock import slack_sender


#Getting today's date in YYYY-MM-DD format
print(date.today().strftime('%Y-%m-%d'))
today_ = date.today().strftime('%Y-%m-%d')
tomorrow = date.today() + timedelta(hours=24)


# Get price data for ATVI for today, yfinance will not print today's data unless you request a range that includes tomorrow's date
data = yf.download('ATVI',today_, tomorrow)
#you can specify a earlier date other than today_ in YYY-MM-DD format if you want to get historical data
print(data) 

'''
# if you end up requesting more historical data you can make a plot here
import matplotlib.pyplot as plt
data.Close.plot()
plt.grid()
plt.show()
'''

TodaysClose = int(data['Close'].values[-1])
print('ATVI closed at ' + str(TodaysClose) + ' today.')

webhook_url = "<https://hooks.slack.com/services/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>"

@slack_sender(webhook_url=webhook_url, channel="<general>")
def train():
    import time
    time.sleep(2)
    #return {'loss': 0.9} # Optional return value
    

UserAlert = 40
if TodaysClose > UserAlert:
    #slack_sender(webhook_url=webhook_url, channel="<general>")
    train()
    print('ATVI')
    


