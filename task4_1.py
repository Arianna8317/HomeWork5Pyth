# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.
# """
# def wages_calculate( hours, sal, bonus) :
#     return hours*sal + bonus
# h = int( input ("Количество часов = "))
# s = int( input ( "Почасовая ставка = "))
# b = int( input ( "Бонус равен = "))
# print ( f"Зарплата {wages_calculate(h,s,b)}")
from sys import argv
script, hours_number, salary_per_hour, bonus = argv 
salary = int(hours_number) * int(salary_per_hour) + int(bonus)
print (f"Зарплата равна {salary}")

