from random import randint
import time


start_time = time.time()
n = 9999
list_of_nums = [randint(2, n + 1) for _ in range(1000000)]

# Решето Ератосфена
primes = [True] * (max(list_of_nums) + 1)
primes[0] = primes[1] = False

for i in range(2, int(max(list_of_nums)**0.5) + 1):
    if primes[i]:
        for j in range(i*i, max(list_of_nums) + 1, i):
            primes[j] = False

list_of_primes = [num for num in list_of_nums if primes[num]]
list_of_primes = set(list_of_primes)
end_time = time.time()

print(f"Список простих чисел: {list_of_primes}")
print(f"К-сть простих чисел у списку: {len(list_of_primes)}")
print(f"Швидкість виконання програми: {(end_time - start_time):.4f} секунд")
