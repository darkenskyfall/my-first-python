from car import Car, ElectricCar

gas_fleet = []
electric_fleet = []

for _ in range(500):
    car = Car('ford', 'focus', 2020)
    gas_fleet.append(car)

for _ in range(250):
    ecar = ElectricCar('nissan', 'leaf', 2020)
    electric_fleet.append(ecar)

# fill the gas cars and charge cars

for car in gas_fleet:
    car.fill_tank()

for electric_car in electric_fleet:
    electric_car.charge()

print("Gas cars:", len(gas_fleet))
print("Electric cars:", len(electric_fleet))

# my_beetle = Car('volkswagen', 'beetle', 2020)
# my_beetle.fill_tank()
# my_beetle.drive()

# my_tesla = ElectricCar('Tesla', 'model s', 2020)
# my_tesla.charge()
# my_tesla.drive()