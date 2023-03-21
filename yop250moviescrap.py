from bs4 import BeautifulSoup
import requests
import sys

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.text,features="html.parser")
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)

movie = []
for movies in tr:
    title = movies.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    year = movies.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = movies.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    row = title + ' - ' + year + ' ' + ' ' + rating
    movie.append(row)
print(movie)
