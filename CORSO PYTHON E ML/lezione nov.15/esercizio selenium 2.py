from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

username= driver.find_element(By.ID, "username")
username1= driver.find_element(By.XPATH, "/html/body/div/div/section/section/ul/li[2]/b[1]").text
username.send_keys(username1 + Keys.RETURN)
time.sleep(3)

password= driver.find_element(By.ID, "password")
password1= driver.find_element(By.XPATH, "/html/body/div/div/section/section/ul/li[2]/b[2]").text
password.send_keys(password1 + Keys.RETURN)
time.sleep(3)

submit = driver.find_element(By.ID, "submit")
submit.click()
time.sleep(3)

logged_in = driver.find_element(By.TAG_NAME, "h1").text
print(f"Messaggio di accesso (h1): {logged_in}")
time.sleep(3)

secondo_mess= driver.find_element(By.TAG_NAME,"p").text
print(f"Secondo messaggio di accesso (p): {secondo_mess}")
time.sleep(3)

log_out = driver.find_element(By.CLASS_NAME, "button")
log_out.click()
time.sleep(3)

print(f"Titolo della pagina: {driver.title}")
driver.quit()