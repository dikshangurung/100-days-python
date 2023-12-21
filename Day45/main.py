from bs4 import BeautifulSoup
from pprint import pprint
import requests
import html
response = requests.get("https://news.ycombinator.com/news")
# response_html = html.unescape(response.text)
# pprint(response_html)
soup = BeautifulSoup(response.text,"html.parser")
# all_title = soup.select(".title")
all_title = soup.select(selector=".titleline>a")
all_score = soup.select(".subline .score")
link_list = []
text_list = []
#List Comprehension baby
score_list = [int(el.getText().split()[0]) for el in all_score]
for title in all_title:
    link_list.append(title.get("href"))
    text_list.append(title.getText())

max_score = max(score_list)
print(f"The highest rated link is {link_list[score_list.index(max_score)]} and title is {text_list[score_list.index(max_score)]}")
# print(link_list)
# print(text_list)
# print(score_list)










# with open("website.html",mode="r",encoding="utf-8") as file:
#     content = file.read()
#     print(type(content))
# # soup = BeautifulSoup(content,"html.parser")
#
# # all_links = soup.find_all(name="a")
# all_links = soup.select("a")
# for link in all_links:
#     if link.getText()[:2] == "My":
#         print(link)

# one_link = soup.select_one(selector="p a")
# print(all_links)
# pprint(soup)
# all_li = soup.find_all(name="li")
# all_li = soup.select(selector="li")
# print(all_li[1].getText())
# all_link = soup.get("a")
#
# print(all_link)
# print(soup.title.name)
# print(soup.li)