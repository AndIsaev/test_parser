from datetime import datetime

import requests as requests
from bs4 import BeautifulSoup as bs

from decorators import sleep

URL_TEMPLATE = 'http://mosday.ru/news/tags.php?metro'
URL_IMAGE = 'https://mosday.ru/news/'
TIME = 600


class PostgresLoader:
    def __init__(self, cur):
        self.cur = cur
        self.new_objects = []
        self.articles = ('table:nth-child(4)', 'table:nth-child(7)')

    def get_last_id(self):
        self.cur.execute('select id from article order by id desc limit 1')
        last_id = self.cur.fetchone()

        return last_id[0] if last_id else 0

    @sleep(TIME)
    def parsing_data(self):
        html = requests.get(URL_TEMPLATE).text
        soup = bs(html, "html.parser")
        table = soup.find_all('table')[2]
        tr = table.find('tr')

        count_id = self.get_last_id()

        for article in self.articles:
            for row in tr.select(article):
                for i in row.find_all('tr'):
                    if i.find_all('b'):
                        title = i.find_all('b')[-1].text
                        date_of_published = datetime.strptime(i.find_all('b')[0].text, '%d.%m.%Y')
                        url_img = f'{URL_IMAGE}{i.find("img")["src"]}' if i.find('img') else None

                        count_id += 1
                        self.new_objects.append((count_id, title, url_img, date_of_published))

        self.insert_data()

    def insert_data(self):
        self.cur.executemany("insert into article values(%s,%s,%s,%s)", self.new_objects)


