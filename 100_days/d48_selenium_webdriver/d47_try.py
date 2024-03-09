from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


driver = webdriver.Edge(options = edge_options)
driver.get("https://www.amazon.in/gp/product/B07QZ3CZ48/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&th=1")

price_ruppee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_pse = driver.find_element(By.CLASS_NAME, value="a-price-faction")
print(price_ruppee.text)

# driver.close()
driver.quit()