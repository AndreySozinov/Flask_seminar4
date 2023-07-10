import requests
import multiprocessing
from url_list import get_url_list


def download(url):
    response = requests.get(url)
    filename = './hundred_urls/processing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__ == '__main__':
    urls = get_url_list('https://www.google.ru/')
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download, args=[url, ])
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
