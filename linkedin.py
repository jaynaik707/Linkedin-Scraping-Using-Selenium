
#Importing selenium library to open browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Setting URL
URL="https://www.linkedin.com/login"

#Setting path for the FireFox driver(geckodriver) and passing the URL as he parameter
driver = webdriver.Firefox(executable_path=r"C:\Users\jayna\Documents\geckodriver.exe")
driver.get(URL)


        
#Defining class for User having two variable username and password        
class User:
    
    
    #Passing username and password as parameter
    def __init__(self, username, password):
        self.username=username;
        self.password=password;
    
    def login(self):
        elementEmailID = driver.find_element_by_id('username)
        elementEmailID.send_keys(self.username)
        time.sleep(5)
        elementPassword = driver.find_element_by_id('password')
        elementPassword.send_keys(self.password)
        time.sleep(5)
        signInButton = driver.find_element_by_class_name("btn__primary--large from__button--floating")
        signInButton.click()     
         

                 

user1=User("jaynaik707@gmail.com","yaj7398kian@")

user1.login()           