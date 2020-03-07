print("hello world")

msg = "hello world"
print(msg)

fname = 'lyga'
lname = 'fakhin'
fullname = fname + ' ' + lname
print(fullname)

bikes = ['trek', 'specialized', 'polygon']
print(bikes)

first_bike = bikes[0]
last_bike = bikes[-1]
print(first_bike, last_bike)

for bike in bikes:
    print(bike)

bikes.append('wim cycle')
print(bikes)

squares = []
for x in range(1, 11):
    squares.append(x**2)

print(squares)

finishers = ['sam', 'bob', 'ada', 'bea']
firstwo = finishers[:2]
print(firstwo)

copy_of_bikes = bikes[:]
print(copy_of_bikes)

dimension = (1920,2000)
print(dimension)

isActive = True

if isActive:
    print('oke')
else:
    print("not oke")

students = ['abihu', 'adam', 'putra', 'soleh']

for student in students:
    if student == 'abihu' or student == 'putra':
        print(student)
    else:
        print('student not found')

alien = {'color':'green', 'points':5}
print("The alien's color is " + alien['color'])

alien['x_position'] = 0
print(alien)

fav_numbers = {'eric':17, 'ever':4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

# age = input("How old are you? ")
# age = int(age)
# print(age)

# pi = input("what is the value of pi? ")
# pi = float(pi)
# print(pi)

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

# msg = ''
# while msg != 'quit':
#     msg = input("whats your message? ")
#     print(msg)

def greet_user():
    """Display a personalized."""
    print("Hello")

greet_user()

def get_name(username):
    """Display Name with Parameters"""
    print("We halo " + username + " , piye kabare?")

get_name('lyga')

def make_pizza(topping='bacon'):
    """make single topping pizza"""
    print("Have a " + topping + " pizza!")

make_pizza()
make_pizza('wijen')

def add_numbers(x,y):
    """add two numbers"""
    return x + y

sum = add_numbers(10, 5)
print(sum)

class Dog():
    """Represent a dog."""
    def __init__(self,name):
        """initialize dog name"""
        self.name = name
    
    def sit(self):
        """simulate sitting"""
        print(self.name + " is sitting")

my_dog = Dog('doggy')
print(my_dog.name + " is great dog")
my_dog.sit()

class SARDog(Dog):
    """Represent inheritance of dog"""

    def __init__(self,name):
        """initialize dog"""
        super().__init__(name)

    def search(self):
        """simulate searching"""
        print(self.name + " is searching.")

my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog")
my_dog.sit()
my_dog.search()
            
# filename = 'lyga.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line)

# filename = 'lyga.txt'
# with open(filename, 'w') as file_object:
#     file_object.write("I Love Programming")

prompt = "How many tickets do you needs? "
num_tickets = input(prompt)

try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again")
else:
    print("Your tickets are printing " + str(num_tickets) + " tickets")

