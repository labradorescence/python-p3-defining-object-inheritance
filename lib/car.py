from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass

car_one = Car(2,4)
print(car_one.go()) #VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!
print(car_one.fill_up_tank())
#filling up!