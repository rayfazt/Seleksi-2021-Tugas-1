import bs4
from bs4 import BeautifulSoup
import requests
import json
import re
import time
import selenium
from selenium import webdriver

header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'
}

url = 'https://pcpartpicker.com/products/cpu/#page='

def get_source(url, header):
    response = webdriver.Firefox()
    response.get(url, headers=header)
    time.sleep(2)
    source = response.page_source
    return source

def scrape(source):
    products = []
    soup = BeautifulSoup(source, 'lxml')
    print(soup)

i = 1
source = get_source(url+str(i), header)
scrape(source)
# print("Hello World")