# Learn classes of python
# Author Dimas Pramudya Sumarsis
# 29 February 2020

# make a class
class Car():

    """ A Simple attempt to model a car"""

    def __init__(self, make, model, year):
        """Initialize car attribute"""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas to tank capacity"""
        self.fuel_capacity = self.fuel_capacity
        print("Fuel tank is full")

    def drive(self):
        """simulate driving"""
        print("Car is moving")

    def update_fuel_level(self, new_level):
        """Update new level"""
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")

    def add_fuel(self, amount):
        """add fuel to tank"""
        if (self.fuel_level + amount <=  self.fuel_capacity):
            self.fuel_level += amount
            print("add fuel")
        else:
            print("The tank won't hold that much!")
        

# ElectricCar Inheritance from Car

class Battery():
    """A Battery for an electric car."""

    def __init__(self, size=70):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %
        self.size = size
        self.charge_level = 0

    def get_range(self):
        """Return the battery's range."""
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270

class ElectricCar(Car):
    """A Simple model of an electric car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        # Attribute specific to electric cars .
        # Battery capacity in kWh .
        # self.battery_size = 70
        # Charge level in %
        # self.charge_level = 0

        self.battery = Battery()

    def charge(self):
        """Fully charge the vehicle"""
        self.battery.charge_level = 100
        print("The Vehicle is fully charged")

    def fill_tank(self):
        """Display an error message"""
        print("This car has no fuel tank!")

# call method

# my_ecar = ElectricCar("Tesla", "model s", "2016")

# print(my_ecar.make)
# print(my_ecar.model)
# print(my_ecar.year)

# my_ecar.charge()
# print(my_ecar.battery.get_range())
# my_ecar.drive()

# my_new_car = Car("Toyota", "Landcruiser", "2020")
# my_new_car.fuel_level = 10

# print(my_new_car.make)
# print(my_new_car.model)
# print(my_new_car.year)

# print(my_new_car.fill_tank())
# print(my_new_car.drive())

