from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# navigate to the application home page
driver.get("https://staging-app.breakdownhero.com/")

# get the search location
try:
    wait = WebDriverWait(driver, 10)
    elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'manual-location-link')))
    print('Ready')
except TimeoutException:
    print("Loading took too much time!")

elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.problem-image.battery"))).click()

driver.quit()
