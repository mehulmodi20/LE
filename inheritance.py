class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._miles = 0
        self._current_location = "None"

    @property
    def miles(self):
        return self._miles

    @miles.setter
    def miles(self, miles):
        self._miles += miles

    @miles.deleter
    def miles(self):
        raise Exception("can't reset miles")

    @property
    def current_location(self):
        return self._current_location

    @current_location.setter
    def current_location(self, location):
        self._current_location = location if location else "home"

    def drive(self, pointa, pointb, miles):
        print(self.current_location)
        self.current_location = pointb
        self.miles = miles
        print(self._current_location)
        print(self.current_location)

    def __str__(self):
        description = "I am a %s %s %s %s miles driven currently parked at %s" % (
            self.year, self.make, self.model, self.miles, self._current_location)
        return description


class Car(Vehicle):
    wheels = 4

    def __init__(self, *args, seats=None):
        super().__init__(*args)
        self.seats = seats


class Bike(Vehicle):
    wheels = 2
    seats = 2

    def __init__(self, *args):
        super().__init__(*args)


car = Car("nissan", "altima", "2014", seats=5)
# print(car.__dict__)
# bike = Bike("harley", "davidson", "2000")
# print(bike.__dict__)
print(car.miles)
print(car.current_location)
car.drive(car.current_location, "work", 30)
# bike.drive(car.current_location, "lake", 15)
# print(car.current_location)
# print(car.miles)
# # car.drive(car.current_location, "home", 30)
# print(car.current_location)
# print(car.miles)
# del car.miles
# print(car)
# print(bike)
# # del car.miles
# del car.current_location
# print(car)
