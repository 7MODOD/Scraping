from selenium import webdriver
import time
from random import randint

path = input("enter the path of webDriver\n")

driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

user = input("enter your username\n")
passw = input("enter your password\n")

time.sleep(5)

username = driver.find_element_by_name("username")

username.send_keys(user)

pas = driver.find_element_by_name("password")

pas.send_keys(passw)


time.sleep(2)
btn = driver.find_element_by_css_selector("button[type = 'submit']")
btn.submit()

time.sleep(5)
page  = input("enter the page username to follow thier followers\n")
pageUrl = "https://www.instagram.com/"+page+"/"
driver.get(pageUrl)
time.sleep(5)

follow = driver.find_element_by_partial_link_text("followers")
follow.click()


time.sleep(5)



sss = driver.find_element_by_xpath('//div[@class="isgrP"]')
driver.execute_script("arguments[0].scrollTo(0,5000)",sss)


#time.sleep(5)
for k in range(50):
    
    time.sleep(1)
    for j in range(5):
        for i in range(7):
       
            ff= driver.find_elements_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
            for f in ff:
                
                driver.execute_script("arguments[0].click()",f)
                time.sleep(randint(3, 10))

            time.sleep(randint(3, 10))
            driver.execute_script("arguments[0].scrollTo(0,5000)",sss)

    time.sleep(20)
    





