from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from api import get_airport_data
#PATH = "C:\chromedriver.exe"
# flag_1 = True

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
x=2
driver.get('https://www.flightradar24.com/')
time.sleep(100)
a = driver.find_element(By.XPATH, )
time.sleep(x)
ActionChains(driver).click(a).perform()