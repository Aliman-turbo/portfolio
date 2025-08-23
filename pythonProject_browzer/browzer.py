
import requests
from bs4 import BeautifulSoup
def get_movie_url(title):
    title = title.replace(" ","+")
    url = f"https://www.imdb.com/find?q={title}&s=tt&exact=true&ref_=fn_tt_ex"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    try:
        movie_link = soup.find("a",href = True,attrs={'class':'ipc-metadata-list-summary-item__t'})
        return f"https://www.imdb.com{movie_link['href']}"
    except :
        print('Ошибка')



def get_movie_info(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find('span', attrs={'data-testid': 'hero__primary-text'})
        element1 = soup.find('span',attrs={'data-testid':'plot-xl'})
        a = {'title': "Холодное сердце", 'description': element1}


        title = element.text if element else 'Название не найдено'
        return {
            "title":title,
            "description":element1.text

        }
    except Exception as e:
        print(f'Ошибка{e}')
if __name__ == '__main__':
    name_film = input("Введи название фильма:")
    get_url = get_movie_url(name_film)
    if get_url:
        print(f"url Страницы:{get_url}")
        get_func = get_movie_info(get_url)
        if get_func:
            print(f"Название {get_func["title"]}")
            print(f"Описание{get_func['description']}")










