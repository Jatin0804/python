import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.in/gp/product/B07QZ3CZ48/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&th=1"
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8,hi;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
print(price)