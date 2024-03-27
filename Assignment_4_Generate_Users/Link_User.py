import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import By


def findKeyword(driver, keyword)->bool:
    print(driver.page_source.lower())
    return keyword.lower() in driver.page_source.lower()

def countElem(driver, tag_name)->int:
    return len(driver.find_elements(By.TAG_NAME, tag_name))
 
def clickLink(driver,href):
    links = driver.find_elements

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = userAction("KEYWORD", driver, reward_time, ["student", "test"])
    tags_name = ["img"]

    for tag in tags:
        num_images = countElem(driver, tag)
        total_reward_time += reward_time
        time.sleep(reward_time)
    driver.quit()
    print("Presence Time:", total_reward_time)
if __name__ == "__main__":
    main()
    
