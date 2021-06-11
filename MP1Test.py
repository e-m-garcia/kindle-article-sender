from bs4 import BeautifulSoup
import requests

URL = 'https://www.pcgamer.com/news/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

item1 = soup.find(id = 'Item1')
print(item1)
headlineLink = item1.a.get('href')

item2 = soup.find(id = 'Item2')
article1Link = item2.a.get('href')

item3 = soup.find(id = 'Item3')
article2Link = item3.a.get('href')

print(headlineLink)
print(article1Link)
print(article2Link)