import threading
import time
import os


class Process(threading.Thread):
    def __init__(self, another_file: str, digit: int):
        super().__init__()
        self.another_file = another_file
        self.digit = digit  # 0 for even numbers, 1 for odd numbers

    def run(self):
        with open(self.another_file + ".txt", "w") as file:
            str_nums = ""
            count = 0
            for num in all_numbers:
                if num % 2 == self.digit:
                    file.write(f"{num}, ")
                    count = count + 1
                    str_nums += f"{num},"
            time.sleep(1)
            print(f"\nЕлементи: {str_nums} к-сть: {count}")


# must be: src/numbers
user_pash = input("Enter pash to file of numbers: ")

if os.path.exists(user_pash + ".txt"):
    with open("src/numbers.txt", "r") as file_of_nums:
        all_numbers = [int(num) for num in file_of_nums.read().split(",")]

        a = Process("src/even_numbers", 0)
        b = Process("src/odd_numbers", 1)

        a.start()
        b.start()
        a.join()
        b.join()

        print("Program ends")
else:
    print("Wrong path!")
