from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# create and configure edge browser
driver = webdriver.Edge(options=edge_options)

# Navigate to signup page
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
fname.click()
fname.send_keys("ABC")

lname = driver.find_element(By.NAME, value="lName")
lname.click()
lname.send_keys("XYZ")

email = driver.find_element(By.NAME, value="email")
email.click()
email.send_keys("ABCXYZ@try.com")

btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()