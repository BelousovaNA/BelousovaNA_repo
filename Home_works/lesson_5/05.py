"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randrange

random_numbers = [randrange(1, 200) for _ in range(50)]

with open('05.txt', 'w', encoding='utf-8') as output_data:
    output_data.write(" ".join(map(str, random_numbers)))

with open('05.txt', encoding='utf-8') as input_data:
    numbers = input_data.read().split()

    print(
        sum(float(x) for x in numbers)
    )
