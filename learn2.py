# init users
users = ['kholid', 'anam', 'arik', 'dodi']

# first user, second user and newest user
first_user = users[0]
second_user = users[1]
newest_user = users[-1]

print(first_user,second_user,newest_user)

# changing users
users[2] = 'lyga'
users[-1] = 'dimas'

print(users)

# starting with new element

# appending item of coffee
coffees = []
coffees.append('robusta')
coffees.append('arabika')
coffees.append('kapalapi')
coffees.append('luwak')
print(coffees)

# insert toraja at 2 of array
coffees.insert(2, 'toraja')
print(coffees)

# delete last of coffee list
del coffees[-1]
print(coffees)

# remove toraja in coffee
coffees.remove('toraja')
print(coffees)

# get last of coffee
most_recent_user = coffees.pop()
print(most_recent_user)

# check length
num_users = len(users)
print("we have " + str(num_users) + " of coffee")

# sorting from a to z
coffees.sort()
print(coffees)

# reverse from z to a
coffees.sort(reverse=True)
print(coffees)

coffees.reverse()

for coffee in coffees:
    print(coffee)