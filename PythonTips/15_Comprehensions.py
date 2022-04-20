# Comprehensions are a feature in Python that allow sequences to be built from other sequences.
# Types of comprehensions include:
# list comprehensions
# dictionary comprehensions XXXXXX Not used often comeback to this topic
# set comprehensions
# generator comprehensions

print("Example 1: List Comprehensions")
# We use this to provide a short and concise way to create lists.

print("Blueprint: variable = [out_exp for out_exp in input_list if out_exp == 2]\n")

# Using List comprehension we get....
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# But we can do this using a for loop like this....
list_1 = []
for i in range(30):
    if i % 3 == 0:
        list_1.append(i)
print(list_1)

# with a single line of code you can now do the exact same thing.
print("\nPart 2 Find the squared values for 2")
# Using list comprehension we get...
squared_2 = [x**2 for x in range(10)]
print(squared_2)
# With the typical for-loop method we get...
squared = []
for i in range(10):
    squared.append(i**2)
print(squared)

print("Example 2: dict comprehensions\n\n\n")
burger_menu = {'Burger': 9.99, 'fries': 2.00, 'Shake': 1.99, 'Soda': .99}
print("..... Come back to this topic ")

print("Example 3: generator comprehensions")
# These are similar to list comprehensions. To be more memory efficient they don't allocate memory for
# the whole list but instead generates one item at a time

multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)  # outputs <generator object <genexpr> at 0x10480a950>

for x in multiples_gen:
    print(x)
# As you can see it generates the values one and a time.

multiples_gen = (i for i in range(30) if i % 3 == 0)
print("\nLets convert this back into a list of items")
gen_list = []
for x in multiples_gen:
    gen_list.append(x)

print(gen_list)


# Please note that running a for loop on multiples_gen causes the variable to change. So in order to
# reset it you need to create that generator comprehension once more


