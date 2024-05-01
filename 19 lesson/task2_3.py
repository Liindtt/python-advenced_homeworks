import time
import random
import multiprocessing


def generate_list(n):
    return [random.randrange(-20, 21, 3) for _ in range(n)]


def sum_and_product(lst):
    summa = sum(lst)
    product = 1
    for num in lst:
        product *= num
    return summa, product


def main():
    n = 4000

    start_time = time.time()
    main_lst = generate_list(n)
    total_sum, total_product = sum_and_product(main_lst)
    end_time = time.time()

    print("Сума елементів списку: ", total_sum)
    print("Добуток елементів списку: ", total_product)
    print("Час виконання програми: ", end_time - start_time, "секунд")
    print("Кінець роботи програми!")


# Багатопроцесорний підхід:
if __name__ == "__main__":
    print("Багатопроцесорний підхід:")
    process = multiprocessing.Process(target=main)
    process.start()
    process.join()
