from bs4 import BeautifulSoup
import requests


from django.contrib.auth.models import User

from .models import MyHokku
from .models import Tokio_authors
from django.conf import settings
from django.db import models


class Pars:
    def make_good(self):
        arr_of_urls = ['http://japanpoetry.ru/hokku/page-'+str(i)+'-catalog' for i in range(2, 28)]
        url = 'http://japanpoetry.ru/hokku'
        arr_of_urls.append(url)
        i = 0
        for url in arr_of_urls:
            request = requests.get(url)
            soup = BeautifulSoup(request.text, 'html.parser')
            teme = soup.find_all('div', class_='poetry')
            for temes in teme:
                new_hokku = MyHokku()
                temes2 = temes.find('div', {'class': 'poetry_text'})
                temes3 = temes.find('div', {'class': 'poetry_title'})
                last = temes2.text.replace(temes3.text, '', 1)
                new_hokku.text = last.strip()
                # new_user = User.objects.create(username='MisterMox')
                # new_user.save()
                # new_hokku.author = new_user
                i += 1
                new_hokku.number = i
                new_hokku.save()
        urls_names = 'https://my-calend.ru/names/male/japanese'
        request_author = requests.get(urls_names)
        soup_names = BeautifulSoup(request_author.text, 'html.parser')
        teme_names = soup_names.find_all('table', class_='names-table names-table-male')
        # for temes in teme_names:
        #     teme1 = temes.find_all('tr')
        #     for teme_pull in teme1:
        #         teme2 = teme_pull.find('span')
        #         if teme2 is not None:
        #             print(teme2.text)
        #             new_name = Tokio_authors()
        #             # new_user = User.objects.create(username='MisterMox')
        #             # new_user.save()
        #             # new_name.author = new_user
        #             new_name.name = teme2.text
        #             new_name.save()




# obb = Pars()
# obb.make_good()
# print(obb.text_1, obb.text_2, obb.text_3)
# print(obb.title_1, obb.title_2, obb.title_3)