import requests
from bs4 import BeautifulSoup


url = "http://www.ceneo.pl/;szukaj-suszarka"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print "<a href='%s'>%s</a>"%(link.get("href"),link.text)
	
	
g_data = soup.find_all("strong", {"class": "cat-prod-row-name"})

for item in g_data:
	print item.text
	