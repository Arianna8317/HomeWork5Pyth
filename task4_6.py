# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
#при котором повторение элементов списка будет прекращено.

import itertools
for i in itertools.count(3):
             print (i),
             if i > 20:
                     break

list_1 = [ 1,3,5,7,9]
iter = itertools.cycle(list_1) 
for i, item in enumerate(iter):
            print (item),
            if  i > 20:
             break

       
           