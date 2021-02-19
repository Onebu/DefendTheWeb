import requests
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#install the chrome driver and instantiate it
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://defendtheweb.net/playground/alphabetize")

#Input the user credential
username = driver.find_element_by_id("login-username")
username.clear()
username.send_keys("username")

password = driver.find_element_by_id("login-password")
password.clear()
password.send_keys("password")
#Find the login button then click it
driver.find_elements_by_xpath("//*[contains(text(), 'Log in')]")[0].click()
#Find the wordlist then sort it
wordlist = driver.find_element_by_id("words").text
items = filter(None, [i.strip() for i in wordlist.split(",")])
ans = ", ".join(sorted(items))

#Paste the solution to the answer text area
password = driver.find_element_by_id("answer")
password.clear()
password.send_keys(ans)
#Then submit it :)
driver.find_elements_by_xpath("//*[contains(text(), 'Submit')]")[0].click()