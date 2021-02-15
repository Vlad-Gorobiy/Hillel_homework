# 1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.
list_line_in_file = {}
counter_len_word = 0
list_delete_words = []
with open('delete_three-five_symbols', 'r') as delete_three_five_symbols:
    i = 0
    for line in delete_three_five_symbols:
        list_line_in_file[i] = line.split()
        print("~" * 100)
        print(line)
        for word in list_line_in_file[i]:
            if 3 <= len(word) <= 5:
                counter_len_word += 1
                list_delete_words.append(word)

        if counter_len_word % 2 == 0 and counter_len_word != 0:
            print(f'Слова для удаления из строки: {list_delete_words}')
            for delete_word in list_delete_words:
                list_line_in_file[i].pop(list_line_in_file[i].index(delete_word))

        print(f'Кол. слов, содержащие от трех до пяти символов: {counter_len_word}')
        counter_len_word = 0
        list_delete_words.clear()
        i += 1
with open('delete_three-five_symbols', 'a') as delete_three_five_symbols:
    delete_three_five_symbols.writelines('\nUpdate text:\n')

    for new_line in list_line_in_file.values():
        delete_three_five_symbols.writelines(' '.join(new_line) + '\n')

# 2)Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.
dict_phone_book = {}
with open('phone_book', 'r') as phone_book:
    for line in phone_book:
        dict_phone_book[line.split(' ')[2][0:-1]] = line.split(':')[0]
        print(line)
print("*"*100)
with open('PhoneBookName_K_or_C', 'w') as PhoneBookName_K_or_C:
    for Phone_number in dict_phone_book:
        Surname = dict_phone_book[Phone_number].title()
        if Surname.startswith('K') or Surname.startswith('C'):
            print(f'{Surname}: {Phone_number}')
            PhoneBookName_K_or_C.writelines(f'{Surname}: {Phone_number}\n')

# 3)Получить файл, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
list_change_str = []
with open('right_align', 'r') as tests:
    for line in tests:
        list_change_str.append(line.rjust(50))

with open('right_align', 'a') as tests:
    for item in list_change_str:
        tests.writelines(f'{item}')

# 4)Дан текстовый файл со статистикой посещения сайта за неделю.
# Каждая строка содержит ip адрес, время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
# Создайте новый текстовый файл, который бы содержал список ip без повторений из первого файла.
# Для каждого ip укажите количество посещений, наиболее популярный день недели.
# Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
