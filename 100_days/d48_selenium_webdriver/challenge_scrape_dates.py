from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


driver = webdriver.Edge(options = edge_options)
driver.get("https://www.python.org/")


# download_link = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# # print(download_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# print(event_times.text)
# for time in event_times:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for n in range(0, len(event_times)):
    events[n] = {
        "name": event_names[n].text,
        "time": event_times[n].text
    }

print(events)


# driver.close()
driver.quit()