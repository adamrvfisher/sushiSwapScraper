# -*- coding: utf-8 -*-
"""
@author: Adam Fisher
"""

# import modules
import pandas
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options

# url to send post request       
url = 'https://www.sushi.com/xswap'
    
class rateGrabber:
    def __init__(self, url):
        options = Options()
  
        # this parameter tells Chrome that
        # it should be run without UI (Headless)
        options.headless = False
          
        # initializing webdriver for Chrome with our options
        self = webdriver.Chrome(options=options)
        
        # self = webdriver.Chrome()
        self.get(url)
        # click button to select dropdown menu for chain selection
        self.find_element(By.XPATH, '//button[text()="Ethereum Mainnet"]').click()
        sleep(5)
        # click Arbitrum One 
        self.find_element(By.XPATH, '//button[text()="Arbitrum One"]').click()
        sleep(3)
        # click button to select dropdown menu for token selection
        self.find_element(By.XPATH, '//button/div[text()="ETH"]').click()
        sleep(3)
        # send keys into text box to select token
        self.find_element(By.ID, 
            'undefined-token-selector-dialog-address-input').send_keys('DPX')
        sleep(3)
        # click token 
        self.find_element(By.XPATH, '//div[contains(@class,"DPX")]').click()
        sleep(3)
        # click button to select dropdown menu for token selection
        self.find_element(By.XPATH, '//button/div[text()="ETH"]').click()
        sleep(3)
        # send keys into text box to select token
        self.find_elements(By.XPATH, 
            '//input[@inputmode="search"]')[1].send_keys('RDPX')
        sleep(3)
        
        # find element that contains the text RDPX
        child = self.find_elements(By.XPATH, '//div[contains(text(),"RDPX")]')[1]
        # find parent element
        parent = child.find_element(By.XPATH, '..')
        # find parent element
        gparent = parent.find_element(By.XPATH, '..')
        
        # click element
        gparent.click()
            
        # enter quantity into text input  
        self.find_element(By.XPATH, '//input[@title="Token Amount"]').send_keys('30')
        sleep(.3)
        
        # find the exact XPATH of element containing swap data
        swapRateElement = self.find_element(By.XPATH, '/html/body/div[1]/'+
                    'div[1]/div[2]/article/div[4]/div[2]/div[1]/div[1]/div')
        
        # parse data out
        swapRate = swapRateElement.text.split()[3]
        
        print(swapRate) 

rateGrabber(url)

# use find elements, return list of elements 
# elems = self.find_elements()

# iterate through list and print html
# for i in range(0, len(elems)):
#     print(elems[i].get_attribute("innerHTML"))
#     print('- - - - - -')
#     print(elems[i].get_attribute("outerHTML"))     
#     print('- - - - - -')
#     print(elems[i].text)
#     print('- - - - - -')
