"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

total = 0

while True:
    user_numbers = input("Введите строку из чисел через пробел >>> ").split()
    has_special_character = False

    for number in user_numbers:
        if number.isdigit():
            total += int(number)
        else:
            has_special_character = True
            break

    print(f"Общая сумма чисел = {total}")

    if has_special_character:
        break