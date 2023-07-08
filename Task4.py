# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте потоки.
from pathlib import Path
import threading


def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print (f'{file_path} содержит {len(content.split())} слов.')


def main():
    threads = []
    dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    for file_path in file_paths:
        thread = threading.Thread(target=count_words, args=(file_path,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
