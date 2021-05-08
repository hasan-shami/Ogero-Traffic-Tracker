from constants import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path=path_chromedriver)
driver.get('https://ogero.gov.lb/myogero/consumption.php')

username = driver.find_element_by_xpath('//input[@type = "text"]')
password = driver.find_element_by_xpath('//input[@type = "password"]')
submit_button = driver.find_element_by_xpath('//button[@data-callback= "onSubmit"]')
username.send_keys(OgeroUsername)
password.send_keys(OgeroPassword)
submit_button.click()

upload = driver.find_element_by_xpath('//div[@class = "MyConsumptionLeft"]//div[3]//span[2]').text
download = driver.find_element_by_xpath('//div[@class = "MyConsumptionLeft"]//div[4]//span[2]').text
total = driver.find_element_by_xpath('//div[@class = "MyConsumptionLeft"]//div[5]//span[2]').text
extra_consumption = driver.find_element_by_xpath('//div[@class = "MyConsumptionLeft"]//div[6]//span[2]').text
consumption_until = driver.find_element_by_xpath('//div[@class = "MyConsumptionLeft"]//div[7]//span[2]').text




