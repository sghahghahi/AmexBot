# This program adds 100 Amex offers at a time to your Amex credit card
# so that you can add unseen offers

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Retreive username and password from local file
with open("credentials.txt", "r") as file:
    USR = file.readline()
    PWD = file.readline()

# Set up Selenium driver
driver = webdriver.Chrome()

# Navigate to Amex Offers website
driver.get("https://global.americanexpress.com/offers/eligible")

# Log in
username = driver.find_element(By.ID, "eliloUserID")
username.send_keys(USR)
password = driver.find_element(By.ID, "eliloPassword")
password.send_keys(PWD)
login = driver.find_element(By.ID, "loginSubmit")
login.click()
time.sleep(10)
twoFactor = driver.find_element(By.ID, "question-input")
twoFactor.send_keys(Keys.RETURN)
time.sleep(5)

# Add up to 100 offers per iteration
offersAdded = 0
iterations = 1 # Can change number of iterations depending on number of offers available
for num in range(iterations):
    offers = driver.find_elements(By.XPATH, "//button[@title='Add to Card']")
    for offer in offers:
        offer.send_keys(Keys.RETURN)
        offersAdded += 1
    # Done. Refresh page and repeat
    time.sleep(5)
    driver.refresh()
    time.sleep(10)

print("Total offers added:", offersAdded)

driver.quit()
