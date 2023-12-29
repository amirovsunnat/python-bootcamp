import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=url)
response.raise_for_status()
website_content = response.text

# create soup object
soup = BeautifulSoup(website_content, "html.parser")
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", "a", encoding="utf-8") as file:
    for index in range(len(titles)-1, -1, -1):
        file.write(f"{titles[index]}\n")
