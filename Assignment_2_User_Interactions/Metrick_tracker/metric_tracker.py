import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

metrics = []
# Track presence time 
start_time = time.time()
presence_time = start_time
num_clicks = 0
while True:
    current_time = time.time()
    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    
    # Track scrolling
    scroll_height = driver.execute_script("return document.body.scrollHeight")  
    current_scroll = driver.execute_script("return window.pageYOffset")
    print(f"Scrolled {current_scroll}/{scroll_height} pixels")
    
    #Monitor title
    title = driver.title
    print(f"Title: {title} ")

    #Track clicks
    button = driver.find_element(By.TAG_NAME, "button")
    #num_clicks = 0
    button.click()
    num_clicks += 1
    print(f"Number of clicks: {num_clicks}")

    time.sleep(2) 



    #driver.quit()
    
