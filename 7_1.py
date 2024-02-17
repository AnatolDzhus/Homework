class Car:
    def __init__(self, color:str, count_passenger_seats:int, is_baby_seat:bool, is_busy=False):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = is_busy
        pass

    def __str__(self):
        return f"{self.color},{self.count_passenger_seats},{self.is_baby_seat},{self.is_busy}"


car1 = Car("Green", 4, False)
print(str(car1))
