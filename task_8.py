'''
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}    email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''

import re

def email_parse(e_mail):

    try:
        dict_parse = list(map(lambda y: y.groupdict(), MODEL_AL.finditer(e_mail)))
        print(dict_parse[0])

    except:
        raise ValueError from ValueError

if __name__ == "__main__":

    e_mail = input(" Введите электронный адрес = ")

    MODEL_AL = re.compile(r"(?P<user_name>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain_name>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")

    email_parse(e_mail)

#Проверка ОК

'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger

@type_logger
def calc_cube(x):
return x ** 3
>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

def type_logger(func):

    def decor(args):

        res = func(args)
        print(f"{args}:{type(args)}")
        print(f"{func.__name__}:{type(func)}")
        print(f"{res}:{type(res)}")
    return decor


@type_logger
def calc_cube(x):
    """ cube of args """
    return x ** 3

if __name__ == "__main__":

    a = int(input('Введите цифру:  '))

    f = calc_cube(a)


#Проверка ОК

#Введите цифру:  25
#25:<class 'int'>
#calc_cube:<class 'function'>
#15625:<class 'int'>



'''
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):

raise ValueError(msg)
ValueError: wrong val -5

'''

from functools import wraps



def val_checker(fanc_filtr):

    def f_f(fanc):

        @wraps(fanc)
        def duc(x):
            if fanc_filtr(x):
                return fanc(x)

            print(f'ОШИБКА {ValueError}: wrong val {x}')
            raise ValueError from ValueError

        return duc

    return f_f


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = int(input('Введите цифру:  '))

f = calc_cube(a)

print(f)


# Проверка ОК