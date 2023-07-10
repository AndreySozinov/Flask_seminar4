# Задание №8
#
# Напишите программу, которая будет скачивать страницы из
# списка URL-адресов и сохранять их в отдельные файлы на диске.
# В списке может быть несколько сотен URL-адресов.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# Представьте три варианта решения.

import requests
import threading
from url_list import get_url_list


def download(url):
    response = requests.get(url)
    filename = './hundred_urls/threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__ == '__main__':
    urls = get_url_list('https://www.google.ru/')
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url, ])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
