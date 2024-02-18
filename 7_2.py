# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None
class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool, is_busy=False):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy
    def __str__(self):
        return f"{self.color},{self.count_passenger_seats},{self.is_baby_seat},{self.is_busy}"

car1 = Car("Green", 4, True)
car2 = Car("Grey", 4, True)
car3 = Car("Blue", 9, True)
cars = [car1, car2, car3]

class Taxi:
    def __init__(self, cars):
        self.cars = cars
    def find_car(self, count_passengers, is_baby):
        self.count_passengers = count_passengers
        self.is_baby = is_baby
        a=set(filter(lambda x: x.count_passenger_seats > count_passengers and x.is_baby_seat >= is_baby and not x.is_busy, cars))
        if not a:
            return None
        else:
            b=a.pop()
            b.is_busy=True
            return b
all_cars = Taxi(cars)
print(all_cars.find_car(2, True))
# print(car1.is_busy)
# print(car2.is_busy)
# print(car3.is_busy)