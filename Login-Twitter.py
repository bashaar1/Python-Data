from selenium import webdriver


import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.twitter.com')


# Username
username = '03204406855'
password = 'faraztariq12'


time.sleep(4)

login = browser.find_elements(
    By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')

login[0].click()


time.sleep(4)
print("Login in Twitter")

user = browser.find_elements(
    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

user[0].send_keys(username)
print("Username Entered")
pressnext = browser.find_elements(By.XPATH,
                                  '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
pressnext[0].click()

time.sleep(4)

user = browser.find_elements(
    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')

user[0].send_keys(password)

print("Password Sent")
print("Successfully Sent the password and the username")

LOG = browser.find_elements(
    By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
LOG[0].click()
print("Login Successful")


time.sleep(5)


browser.close()

