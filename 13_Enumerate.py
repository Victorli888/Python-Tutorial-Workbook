# Enumerate is a built in function that we can use to loop over something and have an automatic counter

print("Example 1: enumerate()")
def example_1(some_list):
    for counter, value in enumerate(some_list, 1):
        print(counter, value)

guest_list = ["Yash", "Austin", "Peter", "Brandon", "Jason", "Victor"]

print(f"These are the people on your guest list: {guest_list}\n")
print(f"your Enumerated list looks like this:")
example_1(guest_list)

print("\n\n\nExample 2: Create Tuples")
def example_2(some_list):
    counter_list = list(enumerate(some_list, 1))
    print(counter_list)


print(f"These are the people on your guest list: {guest_list}")
print(f"You're tuple will look like this")
example_2(guest_list)
