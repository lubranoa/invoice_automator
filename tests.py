from selenium import webdriver

# create webdriver object 
driver = webdriver.Firefox() 

# get google.co.in 
driver.get("https://google.co.in/search?q=frsteam")
