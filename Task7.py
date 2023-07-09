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
summa2 = multiprocessing.Value('i', 0)
summa3 = 0


def sum_array(array):
    global summa
    summa += sum(array)


def sum_proc(array, s):
    with s.get_lock():
        s.value += sum(array)


async def async_sum(array):
    global summa3
    summa3 += sum(array)


def thread_count(array):
    threads = []
    thread1 = threading.Thread(target=sum_array(array[: 500_000]))
    thread2 = threading.Thread(target=sum_array(array[500_000:]))
    threads.append(thread1)
    threads.append(thread2)
    thread1.start()
    thread2.start()

    for thread in threads:
        thread.join()

    print(f'Сумма элементов массива: {summa}')


def process_count(array):
    processes = []
    process1 = multiprocessing.Process(target=sum_proc(array[: 500_000], summa2))
    process2 = multiprocessing.Process(target=sum_proc(array[500_000:], summa2))
    processes.append(process1)
    processes.append(process2)
    process1.start()
    process2.start()

    for process in processes:
        process.join()

    print(f'Сумма элементов массива: {summa2.value}')


async def async_count(array):
    tasks = []
    task1 = asyncio.create_task(async_sum(array[: 500_000]))
    task2 = asyncio.create_task(async_sum(array[500_000:]))
    tasks.append(task1)
    tasks.append(task2)
    await asyncio.gather(*tasks)
    print(f'Сумма элементов массива: {summa3}')


if __name__ == '__main__':
    start_time = time.time()
    print(f'Сумма элементов массива: {sum(arr)}')
    print(f'Synchro time: {time.time() - start_time:.3f} seconds')
    summa = 0

    start_time = time.time()
    thread_count(arr)
    print(f'Threading time: {time.time() - start_time:.3f} seconds')

    start_time = time.time()
    process_count(arr)
    print(f'Processing time: {time.time() - start_time:.3f} seconds')

    start_time = time.time()
    asyncio.run(async_count(arr))
    print(f'Asyncing time: {time.time() - start_time:.3f} seconds')
