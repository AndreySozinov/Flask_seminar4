# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте асинхронный подход.

from pathlib import Path
import asyncio


async def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'{file_path} содержит {len(content.split())} слов.')


async def main():
    processes = []
    dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(count_words(file_path)) for file_path in file_paths]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
