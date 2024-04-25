# Using beautiful soup to webscraping

from bs4 import BeautifulSoup
import lxml

# with open("website.html", mode="r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass
#
# # print(all_anchor_tags)
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# headings = soup.select(".heading")
# # print(headings)

# Webscraping live website
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a")
article_text = article_tag.getText()
print(article_tag)
