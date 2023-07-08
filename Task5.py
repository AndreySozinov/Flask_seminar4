# Создать программу, которая будет производить подсчет количества слов в каждом файле
# в указанной директории и выводить результаты в консоль.
# Используйте процессы.

from pathlib import Path
import multiprocessing


def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print (f'{file_path} содержит {len(content.split())} слов.')


def main():
    processes = []
    dir_path = Path('.')
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    for file_path in file_paths:
        process = multiprocessing.Process(target=count_words, args=(file_path,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
