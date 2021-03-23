from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("D:\SDK's\chromedriver.exe")
file = open("script.txt")
text = file.read()



def send(message):
    message.encode('utf-8')
    lines = message.split('\n')
    for line in lines:
        time.sleep(0.5)
        driver.find_element(By.ID, 'input').send_keys(line + Keys.ENTER)


driver.get(url="https://www.online-toolz.com/langs/pt/tool-pt-notepad.html")
#driver.find_element(By.LINK_TEXT, "Anotações").click()
send(text)
