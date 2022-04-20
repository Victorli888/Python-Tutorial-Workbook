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
# pokemon = OrderedDict([("Pikachu", 56), ("Typhlosion", 78), ("Haunter", 49)])
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
from collections import deque
d = deque()
d.append('apple')
d.append('PBJ')
d.append('Milk')

print(f"Your lunch box has: {len(d)} things in it.")  # output: 3
print(d)
print(d[0])  # output: apple
print(d[-1])  # output: Milk

print("\nYou can pop values from both sides")
d = deque(range(5))
print(f"There are {len(d)} of numbers and they are {d}.")
print(f"Lets take out the left most number and the rightmost number in deque")
d.popleft()  # pops 0
d.pop()  # pops 4
print(f"Our list now looks like {d}.")
# We can set a max limit of items that deque can hold, and once it reaches this limit it will pop out the items from the
# opposite end.
print("\nSetting a limit on items in deque.")
d = deque([1, 2, 3, 4, 5], maxlen=5)
print(d)
print("say I'd like to add a new value (6) into deque")
d.extend([6])
print(f"My new list would look like this {d}.")  # I'm adding 6 to the end of the deque and so 1 is popped off
print("\n We're not limited to left of right")
d = deque([1, 2, 3, 4, 5])
d.extendleft([0, -1, -2])  # Extends leftwards in the order of items presented,
d.extend([6, 7, 8])
print(d)

print("\n\nExample 5: More on namedtuple")
# A named tuple acts like a dictionary BUT unlike dictionaries namedTuple is immutable.
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')  # namedtuple('tuple_name', 'field_names')
scooby = Animal(name='Scooby', age=7, type='doggo')
print(f"I'm {scooby.name}, I'm {scooby.age} years old, and I am the best {scooby.type}")
# Namedtuples are faster than Dictionaries but TAKE NOTE that the downside is it is immutable.
# I would not be able to go sooby.age = 8, This would create an AttributeError: can't set attribute
# USE NAMEDTUPLES TO MAKE YOUR CODE SELF DOCUMENTING
print("\nNamedtuples are backwards compatiable [ONLY]")
print(f"I have {scooby[1]} scooby snacks, Would you like some {scooby[0]}")
print("\nConvert Namedtuples into a dictionary")
print(scooby._asdict())  # this will convert it to a Ordered Dictionary

print("\n\n\nUsing enum.Enum")  # Enumerated type - A way to organize various things
# From example 5, our Animal namedtuple had a type field that is a string, If the user typed dog Dog DOG or puppy then
# it would create problems in the code. Using Enumerations we can avoid this issue buy not using Strings

from enum import Enum
class Species(Enum):
    cat = 1 # from here on any other species represented by 1 will be referred to as cat
    dog = 2
    horse = 3
    spider = 4
    chicken = 5
    owl = 6

    kitten = 1
    meow_meow = 1
    kitty = 1
    doggo = 2

# I'm going to use the Animal namedtuple from example 5
tom = Animal(name="Tom", age=5, type=Species.cat)
skitty = Animal(name='Skitty', age=3, type=Species.kitty)
meowzedong= Animal(name='Meow ZeDong', age=7, type=Species.meow_meow)
tiny_selvester = Animal(name='Baby Selvester', age=1, type=Species.kitten)

print("Test1: Is tom.type equal to meowzedong.type")
print(f"Survey says.... {tom.type == meowzedong.type}")
print(f"What is meowzedong.type?...{meowzedong.type}, then what is skitty?....{skitty.type}")

# Whatever the User types what ever it may be cat, Kat, Cat, Kitten
# we become less error prone when addressing name types

print("\nThere are 3 ways to to acess enumeration members")
print(f"{Species(1)}, {Species['cat']}, and {Species.cat}")
