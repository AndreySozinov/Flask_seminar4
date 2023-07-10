# Задание №9
#
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет
# их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого
# соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения
# и общем времени выполнения программы.
import re
import requests
import time
import threading
import argparse
from multiprocessing import Process
import asyncio
import aiohttp


def find_images(url_):
    # Читаем html-страницу.
    content_ = requests.get(url_).text
    # Формируем список ссылок на изображения по шаблону.
    return re.findall(r'img .*?src="(.*?)"', content_)


def download_image(image_ref):
    begin = time.time()
    response = requests.get(image_ref)
    filename = 'images/' + image_ref.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
        print(f'Downloaded {image_ref} - {time.time() - begin:.3f} sec.')


async def download_image2(image_ref):
    begin = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(image_ref) as response:
            content = await response.read()
    filename = 'images_async/' + image_ref.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(content)
        print(f'Downloaded {image_ref} - {time.time() - begin:.3f} sec.')


def image_grab(image_list):
    for img in image_list:
        if img.endswith(".jpg"):
            download_image(img)


async def image_grab2(image_list):
    for img in image_list:
        if img.endswith(".jpg"):
            await download_image2(img)


def main1(site_url):
    start = time.time()
    images = find_images(site_url)
    threads = []
    diapazon = len(images) // 3
    thread1 = threading.Thread(target=image_grab(images[:diapazon]))
    thread2 = threading.Thread(target=image_grab(images[diapazon:diapazon + diapazon]))
    thread3 = threading.Thread(target=image_grab(images[diapazon + diapazon:]))
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    thread1.start()
    thread2.start()
    thread3.start()

    for thread in threads:
        thread.join()
    print(f'All threading download: {time.time() - start:.2f}')


def main2(site_url):
    start = time.time()
    images = find_images(site_url)
    processes = []
    diapazon = len(images) // 3
    process1 = Process(target=image_grab(images[:diapazon]))
    process2 = Process(target=image_grab(images[diapazon:diapazon + diapazon]))
    process3 = Process(target=image_grab(images[diapazon + diapazon:]))
    processes.append(process1)
    processes.append(process2)
    processes.append(process3)
    process1.start()
    process2.start()
    process3.start()

    for process in processes:
        process.join()
    print(f'All processing download: {time.time() - start:.2f}')


async def main3(site_url):
    start = time.time()
    images = find_images(site_url)
    tasks = []
    diapazon = len(images) // 3
    task1 = asyncio.create_task(image_grab2(images[:diapazon]))
    task2 = asyncio.create_task(image_grab2(images[diapazon:diapazon + diapazon]))
    task3 = asyncio.create_task(image_grab2(images[diapazon + diapazon:]))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    await asyncio.gather(*tasks)
    print(f'All asyncing download: {time.time() - start:.2f}')


if __name__ == '__main__':
    # for site in ['https://gb.ru/', 'https://lenta.ru/']:
    #     main(site)

    parser = argparse.ArgumentParser(description='Grab images from site')
    parser.add_argument('-l', '--list', nargs='+', dest='list', help='List of urls for grabbing',
                        required=True)
    args = parser.parse_args()

    for site in args.list:
        print(site)
        main1(site)

    for site in args.list:
        print(site)
        main2(site)

    for site in args.list:
        print(site)
        asyncio.run(main3(site))
