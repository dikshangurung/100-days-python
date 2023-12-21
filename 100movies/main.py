import requests
from bs4 import BeautifulSoup
import html
movies = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# print(movies.text)
soup = BeautifulSoup(movies.text,"html.parser")
movies_container_list = soup.select(selector=".article-title-description .article-title-description__text .title")
movies_list = [html.unescape(movie.getText()) for movie in movies_container_list]
movies_list.reverse()
# for movie in movies_list:
#     print(movie+"\n")
with open("movies.txt",mode="w") as file:
    for movie in movies_list:
        try:
            file.write(f"{movie}\n")
        except UnicodeEncodeError:
            file.write("59) E.T. – The Extra Terrestrial\n")
