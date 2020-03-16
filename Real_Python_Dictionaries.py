# This is another review of Python dictionaries
print("Typically you'd write Python dictionaries in this format")
Dict_name = {
    'key' : 'value',
    'key1' : 'value1',
    'etc' : 'so on and so forth'
}
print(Dict_name)

print("\n\nYou could just as well use the dict() method")
Dict_name1 = dict([
    ('key', 'value'),
    ('key1', 'value1'),
    ('key2', 'value2')
])
print(Dict_name1)

print("\n\nAs long as the key values are simple strings they can be specified as keyword arguments")
Tools = dict(
    Axe='cut',
    Sword='kill',
    Shovel='dig',
)
print(Tools)

# How to access dictonary elements? Blueprint: Dict_name['key']
print(f"I'll {Tools['Axe']} and {Tools['Sword']} this man. I'll hide the body in the hole i'll {Tools['Shovel']} up")
# add new entries by assigning a new key and value:
print("\n\nlets add a new item to our dictionary")
Tools['Phaser'] = 'stun'
Tools['Delete'] = 'this'
print(Tools)
print("\nlet's delete a dictionary entry")
del Tools['Delete']
print(Tools)

print("\n\n\nBuilding Dictionaries Incrementally.")
on_the_fly_Dict = {}

# from here just add key - value
on_the_fly_Dict['family'] = 'Dad', 'Mom', 'Victor'
on_the_fly_Dict['pets'] = 'Chickens'
on_the_fly_Dict['cars'] = 'Accord DX', 'Accord Sport', 'Izuzu Trooper'

print(on_the_fly_Dict)

# retrieving sublist or sub-dictionary requires an additional index
print(on_the_fly_Dict['family'][-1])  # Victor
print(on_the_fly_Dict['cars'][0]) # Victor's Car

# You can use Operators and Built-in-Functions in
print('garden' not in on_the_fly_Dict)  # True
print('kitchen' in on_the_fly_Dict)  # False
print('cars' in on_the_fly_Dict)  # True

# you can call on len() to find the length of a dictionary

print(f"\n\nThere is {len(Tools)} items in the Tools dictionary")

# These are some Built in Dictionary methods:
# d.clear() - clears a dictionary

# d.get(<key>[, <default>]) - returns the value for a key if it exists in the dictionary
#   - d.get method returns the key without checking whether or not it exits
#   - If there is no key found then it will return NONE

# d.items() - Returns a list of Key-value pairs in a dictionary
print("\n\nExample for d.items()")
# say I want to get the Accord Sport from my on_the_fly_dictionary, I would do something like this
print("from on_the_fly_Dict Find me the Accord sport")
x =list(on_the_fly_Dict.items())[2][1][1]
# [3rd definition] [Key or Values] [2nd Index]
# [Cars: Types] [Values] [Accord Sport]
print(x)

# d.keys() - Returns a list of all the keys in the dictionary
# d.values() - Returns all the Values in the dictionary
# d.pop(<key>[, <default>]) - removes a key from a dictionary, if it is present, and returns its value
#   - If the value doesn't exists when d.pop() is called then it will return KeyError exception

# d.popitem() - Removes a key-value pair form a dictionary.
#   - If the dictionary is empty then a KeyError exception will occur
# d.update(<obj>) - Merges dictionary with another dictionary or with an iterable of key-value pairs.
#   -If the key isn't present in d, the key-value pair from <obj> is added to d
#   -If the key exists then the corresponding value in d for that key is updated with the value from <obj>

