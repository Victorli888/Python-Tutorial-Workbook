# Create a mapping of state to abbreviation """ In a Dictionary, Name : Definition """
states = {  # Adding definitions to the States Dictionary
    'Oregon': "OR",  # Oregon is defined as OR in the State Dictionary
    'Florida': "FL",  # Florida is defined as FL in the State Dictionary
    'Califonia': "CA",  # ETC....
    'New York': "NY",
    'Michigan': "MI"
}

# Create a basic set of states and some cities in them
cities = {  # Adding definitions to the Cities Dictionary
    'CA': 'San Fransisco', # CA is defined as San Fransisco  in the Cities Dictionary
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities["NY"] = "New York City"  # the word NY is defined as New york City in the Cities Dictionary
cities['OR'] = "Portland"  # the word OR is defined as Portland in the Cities Dictionary

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])  # From the Cities Dictionary pull the Definition of NY
print("OR State has: ", cities['OR'])  # From the Cities Dictionary pull the definition of OR

# print some states
print('-' * 10)
print("Michigan's abbreviation is:", states["Michigan"])  # From the states dictionary pull the def. for Michigan
print("Florida's abbreviation is:", states['Florida'])  # From the states dictionary pull the def. for Florida

# do it by using state then cities dict
print('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

"""
From 32 to 34 - work inside to out
From the States dictionary pull the def. of Michigan... (MI) from the cities dictionary pull the def. of MI.
From the States Dictionary pull the def. of Florida... (FL) from the Cities Dictionary pull the def. of FL
"""

"""
list() simply creates a list 
items() will return the list with all the dictionary keys with values
"""

"""
For every x and y in States Dictionary  Oregon = x OR = y  ; state = x abbrev = y
"""
# print every state abbreviation
print(' :) ' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
"""
In short, For each item in the Cities Dictionary, abbrev = OR  city = Oregon 
do this for every item in the Cities Dictionary
"""
# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
"""
For each item in Dictionary States set variables state = Oregon abbrev = OR 
from the Cities Dictionary print the def. of abbrev (Which means: print def of OR )
"""
print('-' * 10)
# Safely get a abbreviation by state that might no be there
state = states.get('Texas') # From States Dictionary get Texas
"""
There is no Texas in the dictionary so state returns false
"""
if not state:  #  if state is false do the following
    print("Sorry, no Texas.")

"""
If I were to do 
if state:
    print("Sorry, no Texas")
then the logic for it would be if state is true do the following
"""

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

"""
From the Cities dictionary get the def of TX and set it equal to city, If TX isn't defined return Does not exist

As you can tell from the get() its a more intuitive version of pulling straight of a dictionary using cities[OR]

With get() you can pull from a definition from a dictionary and if that def returns NONE you can set it to return
an alternative, like "Does Not Exist"

"""
