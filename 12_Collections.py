# Python has a great many number of container types called Collections

print("Example 1: defaultdict")
# unlike dict, with default you don't need to check whether a key is present or not.

from collections import defaultdict

colors = (
    ("y", "Yellow"),
    ("r", "Red"),
    ("b", "Blue"),
    ("blk", "Black"),
    ("wht", "White"),
    ("wht", "Snow"),
    ("wht", "Clouds")

)

fav_colors = defaultdict(list)

for name, color in colors:
    fav_colors[name].append(color)

print(fav_colors)

# lets take a look at what it would like like to have a KeyError when a key is not already present in the dictionary.
# The next examples addresses how to appending items to nested lists in a dictionary.
# NOTE: Python dictionaries are defined as[ key: value ]

print("\nExample2: KeyError using dict")
# some_dict = {}
# some_dict['colors']['fav'] = 'yellow'  # output: KeyError: 'colors'
# Using defaultdict instead we can avoid a KeyError when appeanding items to a nested list inside a dict

tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colors']['fav'] = 'yellow', 'red'
# Using json.dumps  we can print some_dict
import json
print(json.dumps(some_dict))  # outputs: {"colors": {"fav": ["yellow", "red"]}}
print("without json.dumps the output would look like this:")
print(some_dict)  # json = JavaScript Object Notation

print("\nExample 2: OrderedDict")
# - this will keep entries in a dict sorted as they were initially inserted. Overwriting a value of and existing key
# doesn't change the position of the key, Deleting and re-inserting will move the key to the end of the dictionary.
from _collections import OrderedDict
pokemon = {"Pikachu": 56, "Typhlosion": 78, "Haunter": 49}
#pokemon = OrderedDict([("Pikachu", 56), ("Typhlosion", 78), ("Haunter", 49)])
for key, value in pokemon.items():
    print(key, value)
# In prior version of Python this would output key: values in a random order in Python 3.7 OrderedDict is the default
print("\nWith Python 3.7 OrderedDict is now the default but if you were to incorporate it your code would look like:")
print('pokemon = OrderedDict([("Pikachu", 56), ("Typhlosion", 78), ("Haunter", 49)]')

print("\nExample 3: counter")
# with this we'll be able to count the number of occurrences of a particular item
# say we created code that counted the amount of food ordered to a catered event.
from collections import Counter
options = (
    ('chicken', 'dona'),
    ('chicken', 'dany'),
    ('tri-tip', 'dennis'),
    ('tri-tip', 'dan'),
    ('salmon', 'diane'),
    ('chicken', 'Bob')
)

orders = Counter(food for food, option in options)
# in the order of Key-Value Counter will count the amount of keys that a share the same value.
print(orders)

print("\nExample 4: deque (Double ended queue")
# this means you can append and delete elements from either side of the queue.



