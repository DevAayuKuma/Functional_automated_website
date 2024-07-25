# write a script to grab the text from the website and store it in a list
# compare the list with an expected list and use assertion for the verification.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")  # invoke the greenkart website
print(driver.title)                                               # getting the title of the website
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
results = driver.find_elements(By.XPATH, "//div[@class='product']")

for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)

print(actual_list)
assert expected_list == actual_list

