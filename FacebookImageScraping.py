from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
from random import randint

Chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
Chrome_options.add_experimental_option("prefs", prefs)




path = input("enter the path of webDriver\n")


driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com")

username = input("enter your Email\n")
password = input("enter your password\n")



textusername = driver.find_element_by_id("email")
textusername.send_keys(username)

textpassword = driver.find_element_by_id("pass")
textpassword.send_keys(password)


btnlogin = driver.find_element_by_name("login")
btnlogin.submit()

#we are logged in!.......................................
time.sleep(10)
pageImgs = input("enter the images URL in any page to install it\n")
driver.get(pageImgs)
time.sleep(10)

for j in range (1 , 20):
    driver.execute_script("window.scrollTo(0 , document.body.scrollHight);")
    time.sleep(5)

    imgs = driver.find_elements_by_tag_name('img')
    imgs = [a.get_attribute('src') for a in imgs]
    imgs = [a for a in imgs if str(a).startswith("https://scontent.fjrs4-1.fna.fbcdn.net")]

path = os.getcwd()
path = os.path.join(path,"scrapedImages")

os.mkdir(path)


counter = 0

for img in imgs:
    save_as = os.path.join(path,str(counter) + '.jpg')
    wget.download(img,save_as)
    counter += 1


