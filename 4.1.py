try:
    a = int(input('Введите число, чтобы проверить делится ли оно на 3: '))
    b = a % 3
except ValueError:
    print('Введено не число!')
else:
    if b == 0 and a != 0:
        print('Число', a, 'делится на 3')
    elif a == 0:

        print('Введён ноль!')
    else:
        print('Число', a, 'не делится на 3')