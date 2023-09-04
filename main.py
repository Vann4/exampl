user_number = int(input('Введите число: '))
user_string = input('Введите строку: ')

number_list = list(range(1, user_number + 1))

for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        number_list[i] = user_string