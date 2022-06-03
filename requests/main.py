from bs4 import BeautifulSoup
import requests
import re

top = []
r = requests.get('http://www.imdb.com/chart/top')
soup = BeautifulSoup(r.text, 'lxml')

peliculas = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
for i in range(0, len(peliculas)):
    pelicula_string = peliculas[i].get_text()
    pelicula = (' '.join(pelicula_string.split()).replace('.', ''))
    pelicula_titulo = pelicula[len(str(i))+1:-7]
    año = re.search('\((.*?)\)', pelicula_string).group(1)
    ranking = pelicula[:len(str(i))-(len(pelicula))]
    data = {"pelicula_titulo": pelicula_titulo, "año": año, "ranking": ranking, "link": links[i]}
    top.append(data)

for item in top:
    print(item['ranking'], '-', item['pelicula_titulo'], '('+item['año']+')')