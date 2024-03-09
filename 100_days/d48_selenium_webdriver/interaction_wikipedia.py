from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# create and configure edge browser
driver = webdriver.Edge(options=edge_options)

# Navigate to wikipedia website
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# anchor tag using css selectors
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# click on a link
# article_count.click()

# find element by link text
all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# expand the search bar
search_icon = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')
search_icon.click()


# find the search <input> by name
search = driver.find_element(By.NAME, value="search")

# send keyboard keys
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)

# exit all sites and close the browser
# driver.quit()
