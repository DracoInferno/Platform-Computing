import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import collections
import csv

def writeToCSV(filename : str, metrics : dict):
    with open(file=filename, mode="w", newline="") as fp:
    #Create a writer object
        writer = csv.DictWriter(fp, fieldnames=metrics[0].keys())

        #Write the header row
        writer.writeheader()

        #Write the data row
        for metric in metrics:
            writer.writerow(metric)


def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    metrics = []
    SAMPLE_SIZE = 2
    count = 0
    start_time = time.time()
    presence_time = start_time
    num_clicks = 0
    while count < SAMPLE_SIZE:
        # Track presence time 
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
        #metrics["Scrolling (Pixels)"],append(current_scroll/scroll_height)
    
        #Monitor title
        title = driver.title
        print(f"Title: {title} ")

        #Track clicks
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        num_clicks += 1
        print(f"Number of clicks: {num_clicks}")

        # Monitor paragraph contents
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            paragraph_text = paragraph.text
            print(f"Paragraph: {paragraph_text}")

        metrics.append({"TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M%S", time.localtime()),
                        "Presence time (Seconds)" : presence_time,
                        "Scrolling (Pixels)" : current_scroll/scroll_height,
                        "Title" : title,
                        "Number of Clicks" : num_clicks,
                        "Pragraph" : paragraph_text } )
        count += 1
        time.sleep(2) 

    #driver.quit()
    print(metrics)
    writeToCSV("metrics.cvs", metrics)

if __name__ == "__main__":
    main()
    
