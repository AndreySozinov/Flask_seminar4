# Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте процессы.

import requests
from multiprocessing import Process, Pool

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
    filename = './processing/processing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
        print(f'Downloaded {url}')


processes = []

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
