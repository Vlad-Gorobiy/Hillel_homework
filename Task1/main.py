#1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
#  keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 
print("Task №1")
my_dict = {}
for i in range(1,11):
    my_dict[i] = i**2
print(my_dict)
print("*" * 100)

#2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа. 
print("Task №2")
my_list = list(range(0,100,2))
print(my_list)
print("*" * 100)

#3)Заменить в произвольной строке согласные буквы на гласные.  
# еще думаю
print("Task №3")
print("-")
print("*" * 100)
#-

#4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1] 
#4.1) убрать из него повторяющиеся элементы
#4.2) вывести 3 наибольших числа из исходного массива
#4.3) вывести индекс минимального элемента массива
#4.4) вывести исходный массив в обратном порядке 
print("Task №4")
my_list_num = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
#4.1
copy_list_num = my_list_num[:]
for num in copy_list_num:
    if copy_list_num.count(num) > 1:
        copy_list_num.remove(num)
print(copy_list_num)
#4.2
copy_list_num = my_list_num[:]
copy_list_num.sort()
print(f'max numbers in list: {copy_list_num[-1]},{copy_list_num[-2]},{copy_list_num[-3]}')
#4.3
print(my_list_num.index(min(my_list_num)))
#4.4
my_list_num.reverse()
print(my_list_num)
print("*" * 100)

#5) Найти общие ключи в двух словарях: 
#dict_one = { ‘a’: 1,  ‘b’: 2, ‘c’: 3,  ‘d’: 4 }
# dict_two = { ‘a’: 6,  ‘b’: 7, ‘z’: 20,  ‘x’: 40 } 
print("Task №5")
dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40}
for key in dict_one.keys():
    if key in dict_two.keys():
        print(key)
print("*" * 100)

print("Task №6")
#6)Дан массив из словарей 
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
#6.1) отсортировать массив из словарей по значению ключа ‘age' 
i = 0
max = 0
while i < len(data):
    j = 0
    while j < len(data) - 1:
        if data[j].get('age') > data[j + 1].get('age'):
            data[j], data[j + 1] = data[j + 1], data[j]
        j += 1
    i += 1

for item in data:
    print(item)
print('~' * 100)
#6.2) сгруппировать данные по значению ключа 'city' 
# "Еще думаю"
#result = {}
#for i in range(0, len(data)):
#    result[data[i].get('city')] [{'name':data[i].get('name'), 'age':data[i].get('age')}]
#print(result)
print("*" * 100)

# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:
print("Task 7")
def most_frequent(list_var):
    max_count = 0
    dict_max_val = {}
    for i in range(0, len(list_var)):
        if list_var.count(list_var[i]) > max_count:
            max_count = list_var.count(list_var[i])

    for i in range(0, len(list_var)):
        if list_var.count(list_var[i]) == max_count:
            dict_max_val.update({list_var[i]: max_count})
    return dict_max_val

print(most_frequent(['aa','aa', 'bb', 'bb', 'bb']))
print("*" * 100)

# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.
print("Task №8")
numbrs = 123405
mult = 1
while numbrs > 0:
    if numbrs%10:
        mult *= numbrs%10
    numbrs = numbrs // 10
print(mult)
print("*" * 100)

# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
print("Task №9")
def chek_int_in_input(str):
    for digit in str:
        if digit.isdigit():
            return int(digit)
        else:
            return 1

def some_func(array, n):
    if n > len(array):
        return -1
    for it in range(0, len(array)):
        if it == n:
            array[it] *= n
            break
    return array

array_positive_num = [1, 2, 3, 4, 5]
inp_num = chek_int_in_input(input("Enter number:"))
print(some_func(array_positive_num, inp_num))
print("*" * 100)

# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
print("Task №10")
str ='hello 1 one two three 15 world'
spl_str = str.split(" ")
start = end = 0
while end < len(spl_str):
    if spl_str[end].isalpha():
        if end - start == 2:
            print(spl_str[start: end + 1])
        end +=1
    else:
        start = end = end + 1
