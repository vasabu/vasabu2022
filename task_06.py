


'''1Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
 логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
 — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.'''




def parse_log():
    with open('nginx_logs.txt') as f:
        for line in f:
            re_pr = line.split('"')[1]
            ip_a = line.split(' - - ')[0]
            re_t = re_pr.split()[0]
            pr_t = re_pr.split()[1]
            yield(ip_a, re_t, pr_t)



if __name__ == "__main__":
   cor_sp = parse_log()
   for el in cor_sp:
       print(el)



# Проверка ОК


'''3Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в
файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи'''

def dict_us_ho():
    with open("users.txt", "r", encoding="UTF-8") as f_us:
        # выводим текстовый объект в переменную в виде текстовых абзацов
        content_users = f_us.read() 
        # даллее обжимаем текст -убираем пробелы с обеих сторон абзацев(strip),меняем запятую на пробелы
        # во всем тексте,и наконец разматываем текст в список - каждая строка становится элементом списка
        content_users_l = content_users.strip().replace(',', ' ').splitlines()
        # определяем длину списка
        dl_us = len(content_users_l)


    

    with open("hobbi.txt", "r", encoding="UTF-8") as f_ho:
        content_hobbi = f_ho.read()
        content_hobbi_l = content_hobbi.strip().splitlines()
        dl_ho = len(content_hobbi_l)

    raz_cl = dl_us - dl_ho
    if raz_cl == 0:
        # Объединяем два списка и преобразуем кортежы в словарь
        f_cl_and_f_val = dict(zip(content_users_l, content_hobbi_l))
        return f_cl_and_f_val

    if raz_cl < 0:
        f_cl_and_f_val = '1'
        return f_cl_and_f_val
    if raz_cl > 0:
        i = 0
        while i < raz_cl:
            content_hobbi_l.append('None')
            content_hobbi_h = content_hobbi_l
            i = i + 1
    f_cl_and_f_val = dict(zip(content_users_l, content_hobbi_h))
    return f_cl_and_f_val





def main_op():
    dict_us_ho()
    print(dict_us_ho())



if __name__ == "__main__":
    a = int(input("Для запуска программы введите цифру 0 = "))
    if a == 0:
        main_op()


# Проверка показала ок




'''6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
 командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
  значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, 
равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1'''



# Скрипт для записи данных

# Первый Скрипт
sym = " "

def add_sale():
    sym = input("Введите сумму выручки:  ")
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(sym)
        f.write('\n')

def main():
	add_sale()


if __name__ == "__main__":
    main()

#Проверка ОК


#Второй скрипт


import sys

num_1 = 0
num_2 = 0
num_0 = 0
el_s = []
if len(sys.argv) == 1:
    num_0 = 1
    print(num_0)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    num_1 = int(sys.argv[1])
    print(num_1)
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        content = f.read()
        el_s = content.strip().splitlines()
        el_s = el_s[num_1:]
        print(el_s)
        for item in el_s:
            print(item)

if len(sys.argv) == 3 and sys.argv[2].isdigit():
        num_2 = int(sys.argv[2])
        num_1 = int(sys.argv[1])
        print(num_2, num_1)
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            content = f.read()
            el_s = content.strip().splitlines()
            el_s = el_s[num_1:num_2+1]
            print(el_s)
            for item in el_s:
                print(item)

#Проверка ОК
