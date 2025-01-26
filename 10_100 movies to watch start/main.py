import requests
from bs4 import BeautifulSoup

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page=response.text

my_movie_list=[]

soup=BeautifulSoup(yc_web_page, "html.parser")
article=soup.find_all('h3', class_='title')
for i in article:
    text = i.get_text()
    my_movie_list.append(text)
print(my_movie_list[::-1])


with open('movies.txt', 'w') as file:
    for item in my_movie_list[::-1]:
        file.write(item + '\n')
