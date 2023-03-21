t = input('Введите номер билета: ')
x = 0
y = 0
if len(t) % 2 == 0:
    for i in t[0:int(len(t) / 2)]:
        x = x + int(i)
    for i in t[int(len(t) / 2):int(len(t)) + 1]:
        y = y + int(i)
    if x == y:
        print('Билет счастливый')
    else:
        print('Билет не является счастливым')
else:
    print('Количество цифр нечётно')
