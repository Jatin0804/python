from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


driver = webdriver.Edge(options = edge_options)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, "submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

download_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[2]/a')
print(download_link.text)

# driver.close()
driver.quit()