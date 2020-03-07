# for number in range(1001):
#     print(number)

# for number in range(1, 1001):
#     print(number)

# numbers = list(range(1,10000001))
# print(numbers)

ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]

# get youngest of ages with min
youngest = min(ages)
print(youngest)

# get oldest of ages with max
oldest = max(ages)
print(oldest)

# total of years
total_years = sum(ages)
print(total_years)

# slicing data
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']

# slice first three data
first_three = finishers[:3]
print(first_three)

# slice middle three data
middle_three = finishers[1:4]
print(middle_three)

# slice last three data
last_three = finishers[-3:]
print(last_three)

copy_of_finishers = finishers[:]
print(copy_of_finishers)

# squares = []
# for x in range(1,11):
#     square = x**2
#     squares.append(square)

# print(squares)

squares = [x**2 for x in range(1, 11)]
print(squares)

upper_names = ['kai', 'abe', 'ada', 'gus', 'zoe']

for upper in upper_names:
    print(upper.upper())

dimensions = (800,600)

for dimension in dimensions:
     print(dimension)

dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print("Hello " + dog + "!")
print("I love these dog")

print("\nThese were my first two dogs:")
old_dogs = dogs[:2]
for old_dog in old_dogs:
    print(old_dog)

del dogs[0]
dogs.remove('peso')
print(dogs)

# making dictionary
alien_0 = {'color': 'green', 'points': 5}

# get value with associated key
print(alien_0['color'])
print(alien_0['points'])

# getting value with get
alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)

print(alien_color)
print(alien_points)

# adding new value
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5
print(alien_0)
# adding to empty dictionary

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# modifyng value
alien_0['color'] = 'black'
alien_0['points'] = 20
print(alien_0)

# deleting value key pair
del alien_0['color']
print(alien_0)

# Looping through all key value pairs
# fav_languages = {
#     'jen': 'Python',
#     'sarah': 'C',
#     'edward': 'Ruby',
#     'Phil': 'Python',
#     'Dodi': 'Swift'
# }

# # show each person favorite language
# for name, language in fav_languages.items():
#     print(name + " work with " + language)

# # show everyone who's taken the survey
# for name in fav_languages.keys():
#     print(name)

# # show all the languages that have been choosen
# for language in fav_languages.values():
#     print(language)

# # show each person favorite language
# # order by name
# for name in sorted(fav_languages.keys()):
#     print(name)

# # finding dictionary length
# num_responses = len(fav_languages)
# print(num_responses)

# just try
# kosong = ""
# for i in range(100):
#     if i == 75:
#         kosong = "ada"
#         print(kosong)
#     else:
#         kosong = ""
#         print(kosong)

# NESTING A LIST DICTIONARY

# # start with empty list
# users = []

# # make new user and add them to the list
# new_user = {
#     'last':'fermi',
#     'first':'enrico',
#     'username':'efermi'
# }
# users.append(new_user)

# # make another new user and add them as well'
# new_user = {
#     'last':'haezer',
#     'first':'abihu',
#     'username':'zerab'
# }
# users.append(new_user)

# for user_dict in users:
#     print(user_dict)
#     for k, v in user_dict.items():
#         print(k + ': ' + v)
#     print('\n')

# users = [
#     {
#         'last': 'fermi',
#         'first': 'enrico',
#         'username': 'efermi'
#     },
#     {
#         'last': 'curie',
#         'first': 'marie',
#         'username': 'mcurie'
#     }
# ]

# for user_dict in users:
#     print(user_dict)
#     for k, v in user_dict.items():
#         print(k + ': ' + v)
#     print('\n')

# fav_languages = {
#     'jen': ['ruby', 'python'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
# }

# for name, langs in fav_languages.items():
#     print(name + ' ')
#     for lang in langs:
#         print('- ' + lang)

users = {
    'aenstein': {
        'first': 'albert',
        'last': 'enstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_dict in users.items():
    print("\nUsername " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']

    print("\tFullname: " + full_name.title())
    print("\tLocation: " + location.title())




from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages['jen'] = ['Python', 'C']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['Pyhton', 'haskell']

for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)

aliens = []

# for alien_num in range(1000000):
#     new_alien = {}
#     new_alien['color'] = 'green'
#     new_alien['points'] = 5
#     new_alien['x'] = 20 * alien_num
#     new_alien['y'] = 0
#     print(new_alien)
#     aliens.append(new_alien)

# num_aliens = len(aliens)

# print("number of aliens created:")
# print(num_aliens)

test = 'test'
print(test == 'ss')

topping = 'mushrooms'
print(topping != 'test')

age = 18
print(age != 18)

age_0 = 18
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

game_active = True
can_edit = False

price = 0
age = 20

if age > 18:
    price = 2000
elif age == 18:
    price = 1000
else:
    price = 500

print("Your cost is " + str(price) + ".")

players = ['ace', 'ole', 'hoe']

print('ace' in players)