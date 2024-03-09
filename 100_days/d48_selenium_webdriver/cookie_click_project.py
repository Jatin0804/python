from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# create and configure edge browser
driver = webdriver.Edge(options=edge_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

consent = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
consent.click()
time.sleep(1)
language = driver.find_element(By.ID, value='langSelect-EN')
language.click()
time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text

            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(By.ID, "money").text

        if "," in money_element:
            money_element = money_element.replace(",", "")

        cookie_count = int(money_element)

        affordable_upgrades = {}

        for cost, ids in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = ids

        highest_affordable = max(affordable_upgrades)
        print(highest_affordable)
        to_purchase = affordable_upgrades[highest_affordable]

        driver.find_element(by=By.ID, value=to_purchase).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break
