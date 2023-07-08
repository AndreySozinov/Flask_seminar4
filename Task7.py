# Напишите программу на Python, которая будет находить сумму
# элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.
import random
import threading
import multiprocessing
import asyncio
import time

arr = [random.randint(1, 100) for i in range(1000000)]
summa = 0
index = 0


def sum_array():
    global arr, summa, index
    while index < len(arr):
        index += 1
        if index < len(arr):
            summa += arr[index]


async def async_sum():
    global arr, summa, index
    while index < len(arr):
        index += 1
        if index < len(arr):
            summa += arr[index]


def thread_count():
    global summa, index
    summa = 0
    index = 0
    threads = []
    for i in range(5):
        thread = threading.Thread(target=sum_array)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Сумма элементов массива: {summa}')


def process_count():
    global summa, index
    summa = 0
    index = 0
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=sum_array)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Сумма элементов массива: {summa}')


async def async_count():
    global summa, index
    summa = 0
    index = 0
    tasks = [asyncio.create_task(async_sum()) for i in range(5)]
    await asyncio.gather(*tasks)
    print(f'Сумма элементов массива: {summa}')


if __name__ == '__main__':
    start_time = time.time()
    thread_count()
    print(f'Threading time: {time.time() - start_time:.2f} seconds')

    start_time = time.time()
    process_count()
    print(f'Processing time: {time.time() - start_time:.2f} seconds')

    start_time = time.time()
    asyncio.run(async_count())
    print(f'Asyncing time: {time.time() - start_time:.2f} seconds')
