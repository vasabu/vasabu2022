




import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):

    if not (currency_code and url):
        return None

    # меняем регистр
    currency_code = currency_code.upper()

    # принимает ответ от сервера
    respond = requests.get(url)
    print(respond)
    if respond.ok:

        cur = respond.text.split(currency_code)
        print(cur)
        print(len(cur))

        # если курса нет
        if len(cur) == 1:
            return None

        # Берем значение
        val= cur[1].split("</Value>")[0].split("<Value>")[1]
        print(val)
        # оборачиваем его в тип float
        val = float(val.replace(",", "."))

        return (val)

    else:
        return None


print(currency_rates("Gbp"))



'''Создаем   модуль utils_f.py и записываем в него функцию currency_rates()
  и помещаем файл в каталог pythonProject3 в нем же создаем файл-скрипт
  my_script.ru-  заходим в него
  '''
import utils_f

print(utils_f.currency_rates("Eur"))

'''Проверяем -все вроде работает нормально'''
