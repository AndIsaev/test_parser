from datetime import datetime

import requests as requests
from bs4 import BeautifulSoup as bs
from config import URL_IMAGE, URL_TEMPLATE
from logs.settings import logger
from loader import Loader
from decorators import retry


class PostgresLoader(Loader):
    def __init__(self, cur):
        self.cur = cur
        self.new_objects = []
        self.cleared_data = []
        self.articles = ('table:nth-child(4)', 'table:nth-child(7)')
        self.max_date = None
        self.min_date = None
        self.titles_from_db = None

    def get_last_id(self):
        logger.debug('look for the last id from article-table')

        self.cur.execute('select id from article order by id desc limit 1')
        last_id = self.cur.fetchone()

        return last_id[0] if last_id else 0

    @retry()
    def request_to_resource(self):
        logger.debug('request to resource')
        html = requests.get(URL_TEMPLATE).text
        return bs(html, "html.parser")

    def parsing_data(self):
        soup = self.request_to_resource()
        table = soup.find_all('table')[2]
        tr = table.find('tr')

        count_id = self.get_last_id()
        logger.debug(f'amount the last id from article-table {count_id}')

        for article in self.articles:
            for row in tr.select(article):
                for i in row.find_all('tr'):
                    if i.find_all('b'):
                        title = i.find_all('b')[-1].text
                        date_of_published = datetime.strptime(i.find_all('b')[0].text, '%d.%m.%Y')
                        url_img = f'{URL_IMAGE}{i.find("img")["src"]}' if i.find('img') else None

                        count_id += 1
                        self.new_objects.append((count_id, title, url_img, date_of_published))

                        if not self.max_date:
                            self.max_date = date_of_published

                        if self.max_date < date_of_published:
                            self.max_date = date_of_published
                        else:
                            self.min_date = date_of_published

        self.insert_data()

    def insert_data(self):
        self.clear_data()
        logger.debug('have started insert data to article-table')
        self.cur.executemany('insert into article values(%s,%s,%s,%s)', self.cleared_data)
        logger.debug('have done insert')

    def clear_data(self):
        logger.debug('checking table to unique data')
        dates = (self.min_date.date(), self.max_date.date())
        self.cur.execute('select title from article where date_of_published between %s and %s', dates)
        self.titles_from_db = [i[0] for i in self.cur.fetchall()]
        self.transform_data()

    def transform_data(self):
        logger.debug('transform data')
        for val in self.new_objects:
            if val[1] not in self.titles_from_db:
                self.cleared_data.append(val)
        logger.debug('transform table have done')
