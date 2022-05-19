from bs4 import BeautifulSoup
import requests
import random


class Pars:
    title_1 = ''
    title_2 = ''
    title_3 = ''
    text_1 = ''
    text_2 = ''
    text_3 = ''

    def make_good(self):
        arr_of_urls = ['http://japanpoetry.ru/hokku/page-'+str(i)+'-catalog' for i in range(2, 28)]
        url = 'http://japanpoetry.ru/hokku'
        arr_of_urls.append(url)
        list = random.choices(arr_of_urls, k=3)
        my_hokku = []
        for url in list:
            request = requests.get(url)
            soup = BeautifulSoup(request.text, 'html.parser')
            teme = soup.find_all('div', class_='poetry')
            texts = []
            for temes in teme:
                temes2 = temes.find('div', {'class': 'poetry_text'})
                temes3 = temes.find('div', {'class': 'poetry_title'})
                last = temes2.text.replace(temes3.text, '', 1)
                texts.append(last.strip())
            my_hokku.append(''.join(random.choices(texts, k=1)) + '\n')
        authors = []
        urls_names = 'https://my-calend.ru/names/male/japanese'
        request_author = requests.get(urls_names)
        soup_names = BeautifulSoup(request_author.text, 'html.parser')
        teme_names = soup_names.find_all('table', class_='names-table names-table-male')
        for temes in teme_names:
            teme1 = temes.find_all('tr')
            for teme_pull in teme1:
                teme2 = teme_pull.find('span')
                if teme2 is not None:
                    authors.append(teme2.text)
        my_authors = random.choices(authors, k=3)
        self.title_1 = my_authors[0]
        self.title_2 = my_authors[1]
        self.title_3 = my_authors[2]
        self.text_1 = my_hokku[0]
        self.text_2 = my_hokku[1]
        self.text_3 = my_hokku[2]
