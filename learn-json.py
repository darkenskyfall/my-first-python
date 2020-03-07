
"""Store some numbers"""

import json

numbers = [1, 2, 3, 4, 5, 7, 8]

f_name = 'men.json'

try:
    with open(f_name) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    msg = "Can't find {0}.".format(f_name)
    print(msg)
else:
    print(numbers)