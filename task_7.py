"""

1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли
будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

"""


if __name__ == "__main__":

    import os

    folder_s = ["my_project", "settings", "mainapp", "adminapp", "authapp"]
    x = len(folder_s)
    print(x)
    i = 1

    while i < x:
        print(i)
        dir_ob = os.path.join(folder_s[0], folder_s[i])
        if not os.path.exists(dir_ob):
            os.makedirs(dir_ob)
            print(dir_ob)
        i += 1


# Проверка ОК

"""

3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках 
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
 например, во фреймворке django.
 
"""

if __name__ == "__main__":

    import os
    import shutil
    from os.path import relpath

    folder_a = ["my_project", "settings", "mainapp", "adminapp", "authapp"]
    cat_n_1 = folder_a[2]
    cat_n_2 = folder_a[4]

    root_dir = r'C:\Users\User\PycharmProjects\pythonProject3\my_project'

    files = [os.path.relpath(os.path.join(root, file), root_dir) for root, _, files in os.walk(
        root_dir) for file in files if file.endswith(".html")]

    dl = len(files)
    new_dir = os.path.join(root_dir, "template")
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    new_dir_1 = os.path.join(new_dir, cat_n_1)
    if not os.path.exists(new_dir_1):
        os.makedirs(new_dir_1)

    new_dir_2 = os.path.join(new_dir, cat_n_2)
    if not os.path.exists(new_dir_2):
        os.makedirs(new_dir_2)

    i = 0
    while i < dl:
        if i >= dl/2:
            shutil.copy(os.path.join(root_dir, files[i]), new_dir_2)
        else: shutil.copy(os.path.join(root_dir, files[i]), new_dir_1)
        i += 1

# Проверка ОК

"""

4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
 размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых
  не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

"""
import os
import sys

dict_s = {}

def vol_vol(folder_2):

    if not os.path.exists(folder_2):
        return

    with os.scandir(folder_2) as f:
        for item in f:
            if os.path.isfile(item):

                key_s = 10 ** len(str(os.stat(item).st_size))
                dict_s[key_s] = dict_s.get(key_s, 0) + 1

            elif os.path.isdir(item):

                folder_3 = os.path.join(folder_2, item)
                print('прошел=', folder_3) 
                vol_vol(folder_3)


if __name__ == "__main__":

    folder_1 = sys.argv[1]
    folder_2 = (os.path.join(os.getcwd(), folder_1))
    vol_vol(folder_2)
    print(dict_s)

# Проверка ОК
#{10000: 87, 100000: 902, 1000: 10, 10: 1}




