# Написать программу, которая считывает список из 10 URL-адресов и одновременно
# загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.

import requests
import threading

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://www.gismeteo.ru/',
        'https://news.ru/',
        'https://www.banki.ru/wikibank/finansovyiy_ryinok/',
        'https://skillbox.ru/',
        'https://www.rbc.ru/'
        ]


def download(url):
    response = requests.get(url)
    filename = './threading/threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
        print(f'Downloaded {url}')


if __name__ == '__main__':
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url, ])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
