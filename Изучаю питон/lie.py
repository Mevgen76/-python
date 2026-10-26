x = 0
while x == 0:
    try:
        x = int(input ('введите число: '))
        x += 10
        print (x)
    except ValueError:
        print('Вы не ввели число.')    