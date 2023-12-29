from bs4 import BeautifulSoup
import requests


url = "https://news.ycombinator.com/"
response = requests.get(url=url)
response.raise_for_status()
website_content = response.text


# create soup object
soup = BeautifulSoup(website_content, "html.parser")
# find span elements with the class "titleline" and then find the nested <a> elements
span_elements = soup.find_all('span', class_='titleline')

# find article upvotes
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

links = []
titles = []
for span in span_elements:
    a_element = span.find('a')
    if a_element:
        links.append(a_element.get('href'))
        titles.append(a_element.get_text(strip=True))


integer_upvotes = [int(vote.split()[0]) for vote in article_upvotes]

# find the highest score
highest = max(integer_upvotes)
index = integer_upvotes.index(highest)

# print highest scored movie title and link
print(f"Highest scored movie is: {titles[index]} with the {integer_upvotes[index]} upvotes. \nHere is the link to this "
      f"article: {links[index]}")

