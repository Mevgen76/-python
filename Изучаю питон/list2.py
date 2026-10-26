number = [5,1,6]
# numbers[3] = 100
number.append(True)
number.append(False)

# list.append - добавляет значение в конец

number2 = [5,1,6]

number2.insert(1, 999)

# number.insert(1, 999)первое значение то,перед которым добавится второе

print(number)

choice = str(input('увидеть второй number?'))
if choice == "да":
 print(number2)

#  number.extend[7,7,7] - добавить в конец множество значений
#  number.extend(number2) - добавить в конец number2 - number2


# number.sort - сортирует от меньшего к большему

num3 = [5,7,1,8,54,1,8,6,845,13432,767]
num3.sort()
print(num3)



 
 