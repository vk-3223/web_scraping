from email import header
from lib2to3.pgen2 import driver
from urllib import response
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


URL= "YOUR_WEBSITE_LINK"
chrome_driver_path = "your_chromedriver_path"
header ={
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

response = requests.get(url=URL,headers=header).text
soup = BeautifulSoup(response,"html.parser")


laptop_name = soup.select(".a-size-medium")
all_laptop_name = [laptop.get_text().split("|")[-1] for laptop in laptop_name]
print(laptop_name)

laptop_price = soup.select(".a-price-whole")
laptop_price_name = [price.get_text().split("|")[-1] for price in laptop_price]
print(laptop_price_name)

all_laptop_link = soup.select(".a-link-normal")    
all_link = []

for link in all_laptop_link:
    href = link["href"]
    if "http" not in href:
        all_link.append(f"https://www.amazon.in/{href}")
    else:
        all_link.append(href)    
print(all_link)
driver = webdriver.Chrome(executable_path=chrome_driver_path)
for n in range(len(all_link)):
    driver.get("HERE_YOUR_GOOGLE_SHEET_LINK")
    time.sleep(2)
    all_laptop_by_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    all_laptop_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    all_laptop_by_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    sumbit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    all_laptop_by_name.send_keys(all_laptop_name[n])
    all_laptop_price.send_keys(laptop_price_name[n])
    all_laptop_by_link.send_keys(all_link[n])
    sumbit.click()