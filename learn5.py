class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full")

    def drive(self):
        print("Car is moving")

my_car = Car('audi', 'a4', 2020)

print(my_car.model)
print(my_car.make)
print(my_car.year)

my_car.fill_tank()
my_car.drive()

my_car = Car('audi', 'a4', 2016)
my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('Toyota', 'Land Cruiser', 2020)

print(my_car.model, my_old_car.model, my_truck.model)