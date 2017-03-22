from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create a new Chrome session
driver = webdriver.Chrome()

driver.maximize_window()

# navigate to the application home page
driver.get("https://staging-app.breakdownhero.com/")


# get the search location
try:
    wait = WebDriverWait(driver, 60)
    elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.safety-title.hide-show-animate.col-xs-12.ng-hide')))
    print('Ready')
except TimeoutException:
    print("Loading took too much time!")
#time.sleep(30)

elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "manual-location-link"))).click()
#new one text

driver.quit()
