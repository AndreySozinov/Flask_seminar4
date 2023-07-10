from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests

my_urls_list = set()
total_urls_visited = 0


def is_valid(url_name):
    parsed = urlparse(url_name)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url_):
    """
    Возвращает все URL-адреса, найденные на `url`, в котором он принадлежит тому же веб-сайту.
    """
    # все URL-адреса `url`
    urls = set()
    # доменное имя URL без протокола
    domain_name = urlparse(url_).netloc
    soup = BeautifulSoup(requests.get(url_).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href пустой тег
            continue
        # присоединяемся к URL, если он относительный (не абсолютная ссылка)
        href = urljoin(url_, href)
        parsed_href = urlparse(href)
        # удалить GET-параметры URL, фрагменты URL и т. д.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # недействительный URL
            continue
        if href in my_urls_list:
            # уже в наборе
            continue
        if domain_name not in href:
            # внешняя ссылка
            if href not in my_urls_list:
                my_urls_list.add(href)
            continue
        urls.add(href)
        my_urls_list.add(href)
    return urls


def crawl(url_n, urls_amount=30):
    """
    Сканирует веб-страницу и извлекает все ссылки.
    параметры:
         urls_amount (int): максимальное количество URL-адресов для сканирования, по умолчанию - 30.
    """
    global total_urls_visited
    links = get_all_website_links(url_n)
    for link in links:
        total_urls_visited += 1
        if total_urls_visited > urls_amount:
            break
        crawl(link, urls_amount=urls_amount)


def get_url_list(root_url, amount_of_urls=30):
    crawl(root_url, urls_amount=amount_of_urls)
    print("Итого URL:", len(my_urls_list))
    return my_urls_list


if __name__ == '__main__':
    url = 'https://www.google.ru/'
    crawl(url)
    print("Итого URL:", len(my_urls_list))
