"""
    1. Реализуйте класс Car с атрибутами:
    - brand (марка)
    - model (модель)
    - engine (объем двигателя)
    - year (год выпуска)

    2. Создайте метод get_info,
        "Ford Focus v2.3", где 2.3 - объем двигателя (engine)

    3. Создайте список из 5 объектов класса Car.
    4. Отсортируйте список объектов по year и get_info, если год одинаковый
    5. Выведите на экран результат метода get_info для каждого объекта списка
"""


class Car:
    def __init__(self, brand, model, engine, year):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = str(year)
    def func(self):
        print("#2", self.brand, self.model, "v" + self.engine)

    def __repr__(self):
        return self.year


car_list = []
car1 = Car('Ford', 'Focus', "2.3", 2013)
car1.func()
car2 = Car("BMW", 'x7', "3.5", 2019)
car3 = Car("Ford", 'F150', "3", 2017)
car4 = Car("Toyota", 'Corolla', "2", 2018)
car5 = Car("Chery", 'Tiggo', "1.5", 2018)
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
car_list.append(car4)
car_list.append(car5)
c = sorted(car_list, key=lambda car: (car.year, car.engine))

for car in c:
    print(car.brand, car.model, "v" + car.engine)

