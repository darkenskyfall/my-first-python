
# print("Enter two numbers I'll divide them")

# x = input("First number: ")
# y = input("Second number: ")

# try:
#     result = int(x) / int(y)
# except ZeroDivisionError:
#     print("u can't divided by zero!")
# else:
#     print(result)

"""A simple calculator with division only"""

print("Enter two numbers. I'll divide them")
print("Enter 'q' to quit.")

while True:
    x = input("\nFirst number: ")
    if x == 'q':
        break
    y = input("\nSecond number: ")
    if y == 'q':
        break

    try:
        result = int(x) / int(y)
    except ZeroDivisionError:
        print("u can't divided by zero!")
    else:
        print(result)