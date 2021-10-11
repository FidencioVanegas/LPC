import requests
from bs4 import BeautifulSoup

url = 'https://starwars.fandom.com/es/wiki/Star_Wars'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

sw = soup.find_all('ol')
print(sw)
archivo = open('Star Wars.txt','w')
archivo.write(str(sw))
archivo.close()
