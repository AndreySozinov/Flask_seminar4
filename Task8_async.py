import requests
import asyncio
import aiohttp
from url_list import get_url_list


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
    filename = './hundred_urls/async_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


async def main():
    urls = get_url_list('https://www.google.ru/')
    tasks = []
    for ur_l in urls:
        try:
            task = asyncio.create_task(download(ur_l))
        except IOError:
            print('Ошибка чтения сайта')
            continue
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
