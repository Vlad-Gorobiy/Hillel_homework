# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
def decorator(func):
    def wrapper(arg):
        result = func(arg)
        if result != 0:
            print(f"result_decor = {100 % result}")
            return result
        else:
            print("Результат функции decorator: 0")
            return result
    return wrapper

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

def chek_type_arg(func):
    def wrapper(arg):
        if type(arg) is int:
            result = func(arg)
            print(f"Результат функции chek_type_arg: {result}")
            #return result
        else:
            raise ValueError("string type is not supported")
    return wrapper

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.
def cash_decorator(func):
    cache = {}
    def wrapper(arg):
        if arg in cache:
            print("Used cache with counter = {}")
            return cache[arg]
        else:
            cache[arg] = func(arg)
            print("Function executed with counter = {}, function result = {}")
            return cache[arg]
        return wrapper



@chek_type_arg
@decorator
def foo(num):
    result = num % 3
    if result == 0:
        print("We are OK!")
    else:
        print(f"Bad news guys, we got {result}")
    return result

print("Task 1, 2")
foo(53)


