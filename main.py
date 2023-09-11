# user_number = int(input('Введите число больше нуля: '))
# user_string = input('Введите строку: ')
#
# number_list = list(range(1, user_number + 1))
#
# for i in range(len(number_list)):
#     if number_list[i] % 2 == 0:
#         number_list[i] = user_string
#
# print(number_list)
# print("Стучусь в контрибьютеры за красивые глаза")

#Задача: взять текст от пользователя и вывести число повторяющихся букв
user_string = input('Введите текст на английском языке: ')
letter_count = {} #Пустой словарь

for letter in user_string:
    if letter in letter_count: #Проверка есть ли данный символ в словаре
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
repeated_letters = {letter: count for letter, count in letter_count.items() if count > 1} #Новый словарь