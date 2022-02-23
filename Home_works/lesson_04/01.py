"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами."""


hours = int(input("Количество отработанных часов >>>"))
hourly_rate = int(input("Стоимость человеко-часа >>>"))
bonus = int(input("Сумма премии >>>"))
salary = hours*hourly_rate + bonus

def calculate(salary):
    try:
        return salary - (salary * .13)
    except TypeError:
        return

print(calculate(salary))