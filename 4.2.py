try:
    a = int(input('Введите число: '))
    b = 100 / a
except ZeroDivisionError:
    print('Введён 0!')
except ValueError:
    print('Введено не число!')
else:
    print('Результат деления 100 на введённое число: ', b)