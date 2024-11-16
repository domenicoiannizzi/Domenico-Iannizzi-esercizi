from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


def table_scraping():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    time.sleep(3)

    button_privacy = driver.find_element(By.ID, "accept-choices")
    button_privacy.click()
    time.sleep(2)
    for el in range(2,7):
        for num in range(1,4):
            tabella = driver.find_element(By.XPATH, f"/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[{el}]/td[{num}]")
            print(tabella.text)
    driver.quit()

table_scraping()

