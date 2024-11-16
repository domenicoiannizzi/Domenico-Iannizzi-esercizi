#Visita Wikipedia, cerca "Python (programming language)", e stampa il titolo della pagina dei risultati


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://it.wikipedia.org/wiki/Pagina_principale")
time.sleep(5)

search_bar = driver.find_element(By.ID, "searchInput")
search_bar.send_keys("Python (programming language)" + Keys.RETURN)


print(f"Titolo della pagina: {driver.title}")
time.sleep(5)

driver.quit()