print("Example 1: The Mighty Return")
# what return does is it simply, assigns the value to the variable which is calling that function "result"
# ******** assigns it to the variable that is calling the function ***********

def add(value1, value2):
    return value1 + value2


value1 = 3
value2 = 5
result = add(value1, value2)
print(f"{value1} + {value2} = {result}")

print("Example 2: Use the Global Variable")
# by using the global we can access result_2 outside of the function

def add_2(value1, value2):
    global result_2
    result_2 = value1 + value2


result_2 = add(value1, value2)  # we can use it like return but assigning it to a variable is not necessary
print(f"{value1} + {value2} = {result_2}")

print("\nExample 3: Another example with Global")
# USING GLOBAL VARIABLES ARE RISKY, its smart to keep code encapsulated so that it doesn't affect other lines of code
def add_3(value1, value2):
    global result_3
    result_3 = value1 + value2


add_3(3, 5)
print(f"{value1} + {value2} = {result_3}")

print("\nExample 4: Multiple return values")  # This method is NOT a good idea
def pokemon():
    global name4
    global level4
    name4 = "Chikorita"
    level4 = 5

pokemon()
print(f"A Level {level4} {name4} appeared!")

print("\nThis time lets use return to call on multiple return values")
def pikachu():
    name5 = "Pikachu"
    level5 = 17
    return (name5, level5)

pikachu_name, pikachu_level = pikachu()  # There is intent when creating these variables so its less risky
print(f"A level {pikachu_level} {pikachu_name} appeared!")

# wow very much good encapsulation
print("\nThis is another way we could do this is this..")
def cyndiquil():
    name = "cyndiquil"
    level = 22
    return (name, level)

cyndiquil_info = cyndiquil()
print(f"A level {cyndiquil_info[0]} {cyndiquil_info[1]} appeared!")

print("\nExample 5: Using namedtuple")
from collections import namedtuple


from collections import namedtuple
def suicune():
    Pokemon = namedtuple('Pokemon', 'name level')  # Assign the the Pesudo Object, Assign the Arguments to that object
    return Pokemon(name="Suicune", level=50)  #

# Use as namedtuple   namedtuple(type_name, field names)
s = suicune()
print(s, type(s)) # This outputs: Person(name='Suicune', level=31) <class '__main__.Pokemon'>
print(f"A wild level {s.level} {s.name} appeared")

# Use as plain tuple
s = suicune()
print(f"A wild level {s[1]} {s[0]} appeared")

# Unpack it immediatly
name, level = suicune()
print(f"A wild level {level} {name} appeared")

print("For the funnies lets do this for all the Legendary Pokemon")

def raikou():
    Pokemon = namedtuple('Pokemon', 'name level')
    return Pokemon(name="Raikou", level=50)

def enti():
    Pokemon = namedtuple("Pokemon", "name level")
    return Pokemon(name="Enti", level=50)

namedt

print(f"A level {raikou().level} {raikou().name} appeared.")
print(f'A level {enti().level} {enti().name} appeared.')