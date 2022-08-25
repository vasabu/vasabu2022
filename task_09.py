
'''
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.

'''

#классы

import time

trafik = 0.0

def time_long(trafik):
    tic = time.time()
    tac = tic + trafik
    while time.time() < tac:
        continue
    print(f't = {time.time():.0f}')

class TrafficLight:
    __color = ''
    def running(self, trafik_red, trafik_yelow, trafik_green):

        TrafficLight.__color = 'red'
        print(f't = {time.time():.0f}')
        print("горит красный")
        time_long(trafik_red)

        TrafficLight.__color = 'yelow'
        print("горит желтый")
        time_long(trafik_yelow)

        TrafficLight.__color = 'green'
        print("горит зеленый")
        time_long(trafik_green)


traff = TrafficLight()
traff.running(7, 2, 10)

'''
Проверка:

t = 1661013219
горит красный
t = 1661013226
горит желтый
t = 1661013228
горит зеленый
t = 1661013238
'''

'''
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т

'''


class Road:
    massa = 0

    def raschet(self, _long_tras, _short_tras):

        self._long_tras = _long_tras
        self._short_tras = _short_tras
        massa = int(_long_tras * _short_tras * 125 / 1000)
        print(f'Вес покрытия {massa} тонн')



a = Road()
a.raschet(20, 10000)

# Проверка:
#Вес покрытия 25000 тонн


'''
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

dict_zp = {"wage": f'{int(input("Введите оклад = "))}', "bonus": f'{int(input("Введите премию = "))}'}

class Worker:
    def __init__(self, _income_1, _income_2, name, surname):
        self._income_1 = int(_income_1)
        self._income_2 = int(_income_2)
        self.name = name
        self.surname = surname



class Position(Worker):
    def __init__(self, _income_1, _income_2, name, surname, position):
        super().__init__(_income_1, _income_2, name, surname)
        self.position = position
    def get_full_name(self):
        
        return f'{self.name} {self.surname}'
    def get_total_income(self):

        return self._income_1 + self._income_2

a = Position(dict_zp["wage"], dict_zp["bonus"], str(input('Введите имя = ')),
             str(input('Введите фамилию = ')), str(input('Введите должность = ')))
print(a.get_full_name())
print(a.get_total_income())

'''
Проверка:
Введите оклад = 100
Введите премию = 50
Введите имя = aaa
Введите фамилию = sssss
Введите должность = ddddddd
aaa sssss
150
'''
'''
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_info(self):
        print('Машина Поехала')
    def stop_info(self):
        print('Машина Остановилась')
    def turn_left(self):
        print('Машина Повернула Налево')
    def turn_rite(self):
        print('Машина Повернула Направо')
    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая Скорость Машины < 40 км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if 40 < self.speed <= 60:
            print(f'Текущая Скорость Машины Превышенна на 20 км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая Скорость Машины Превышенна Более чем на 20 км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Спортиная Машина')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('Полицейская машина')


a = Car(int(input('Введите Скорость Машины = ')), str(input('Введите Цвет Машины = ')),
        str(input('Введите Модель Машины = ')), str(input('Введите Номер Полиса = ')))

a.go_info()
a.stop_info()
a.turn_left()
a.show_speed()

b = WorkCar(int(input('Введите Скорость Машины = ')), str(input('Введите Цвет Машины = ')),
        str(input('Введите Модель Машины = ')), str(input('Введите Номер Полиса = ')))
b.show_speed()

t = TownCar(int(input('Введите Скорость Машины = ')), str(input('Введите Цвет Машины = ')),
        str(input('Введите Модель Машины = ')), str(input('Введите Номер Полиса = ')))
t.show_speed()

# Проверка ОК

'''
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.

'''

class Stationery():
    title = ' '

    def drow(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def drow(self):
        print('Отрисовка Ручкой')


class Pencil(Stationery):

    def drow(self):
        print('Отрисовка Карандашом')


class Handle(Stationery):

    def drow(self):
        print('Отрисовка Маркером')


a = Stationery()
b = Pen()
c = Pencil()
d = Handle()
a.drow()
b.drow()
c.drow()
d.drow()

# Проверка ОК


