n = int(input('Введи длину'))

user_list = []
i = 0
while i < n:
    string = 'enter #' + str(i + 1) + ': '
    user_list.append(input(string))
    i += 1

    print(user_list)