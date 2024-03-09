from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup)

# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

head_tags = soup.find(name="h1", id="name")
print(head_tags)

h3_tags = soup.find(name="h3", class_="heading")
print(h3_tags)