from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

file = open("script.txt")
text = file.read()
text = str(text)
driver = webdriver.Chrome("D:\SDK's\chromedriver.exe")


def send(message):
    lines = message.split('\n')
    print('ok1')
    for line in lines:
        time.sleep(0.5)
        print('ok2')
        driver.find_element(By.CLASS_NAME, '_2A8P4').send_keys(line + Keys.ENTER)


driver.get(url="https://web.whatsapp.com/")
qrcode = input("Qr Code OK?")
if qrcode:
    driver.find_element(By.CLASS_NAME, "TbtXF").click()
    send(text)
