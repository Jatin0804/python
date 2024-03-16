from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from time import sleep
from os import environ
import requests

ENDPOINT_ALERTZY = environ["ENV_ENDPOINT_ALERTZY"]
API_KEY_ALERTZY = environ["ENV_API_KEY_ALERTZY"]


def send_sms(title: str, message: str):
    params = {
        "accountKey": API_KEY_ALERTZY,
        "title": title,
        "message": message,
    }

    requests.post(url=ENDPOINT_ALERTZY, params=params)


# Set Webdriver
ua = UserAgent()
user_agent = ua.random

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(f'--user-agent={user_agent}')
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
options.page_load_strategy = 'normal'

# Set Data
email = "leonrey_4@hotmail.com"
password = "#rmy4NnG$88?"

# Set Driver
driver = Chrome(options=options)
driver.get("https://www.coinbase.com/explore/s/listed")
sleep(3)

currency = driver.find_element(By.XPATH,
                               '/html/body/div[1]/div/div[1]/main/div/div/div[2]/div[3]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/button/div/div')
currency.click()

sleep(2)
search_currency = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div[1]/main/div/div/div[2]/div[3]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div/div/input')
search_currency.send_keys("USD")
sleep(1)
search_currency.send_keys(Keys.ENTER)

sleep(3)
table = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div/table/tbody')

rows = table.find_elements(By.CSS_SELECTOR, 'tr.cds-tableRow-t45thuk.cds-tableRowHover-t9ma3wv')

message = ""
for row in rows[:10]:
    row_clean = row.text.split("\n")
    message += f"{row_clean[1]} ({row_clean[2]}): {row_clean[3]} ({row_clean[5]})\n"

send_sms(title="Top 10 Crypto", message=message)