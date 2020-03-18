
#Importing selenium library to open browser
from selenium import webdriver

#Setting URL
URL = "https://www.linkedin.com/login"
   
#Defining class for User having two variable username and password        
class User:
       
    #Passing username and password as parameter
    def __init__(self, username, password):
        self.username=username
        self.password=password
    
    #Function to login username and password and signnig in by clicking button
    def login( self ):  

        #Setting path for the FireFox driver(geckodriver) and passing the URL as he parameter
        driver = webdriver.Firefox()  
        driver.get(URL) 

        driver.find_element_by_id('username').send_keys(self.username)   #Sending username to Linkedin's login page
        driver.implicitly_wait(10)

        driver.find_element_by_id('password').send_keys(self.password)  #Sending password to Linkedin's login page
        driver.implicitly_wait(10) 

        driver.find_element_by_class_name("login__form_action_container ").click()    #Clicking the login button
        driver.implicitly_wait(10) 

        #Checking whether the login was successful by matching current driver url and actual url
        actualURL = "https://www.linkedin.com/feed/"
        expectedURL= driver.current_url
        driver.quit()   #Closing driver
        return(expectedURL==actualURL)	
        
        	