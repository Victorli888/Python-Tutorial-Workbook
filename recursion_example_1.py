# recursion is the process of defining something in terms of its self. (two parallel mirrors)

# example1 of a recursive function to find the factorial of a number.
print("example 1: Calculate the Factorial")

def calc_factorial(x):
    """
    This is a recursive function that finds the factorial of an integer
    :param x:
    :return:
    """

    if x == 1:
        return 1  # Base case: 1! = 1

    else:
        return (x * calc_factorial(x-1))  # recursive case: n! = n * (n-1)!

num_a = 5

print(f"the factorial of {num_a} is {calc_factorial(num_a)}")

print("Example 2: Delivering Presents")
# Santa needs to deliver presents to 8 Houses if he does it himself it would look like this
houses = []

for j in range (1, 9):
    home = (f"House {j}")
    houses.append(home)

def deliver_iteratively():
    for house in houses:
        print("Santa Delivering presents to", house)

deliver_iteratively()
print("\nThis time we'll do it with the help of elves")
# Elves responisble for >1 houses are managers if they're = 1 then they are a worker

def deliver_recursively(houses):
    '''
    Without the use of a for loop we can deliver presents to each house by spliting up the houses up until
    each elf has one house.
    :param houses:
    :return:
    '''
    if len(houses) == 1:  # This is the case where Worker elf will make deliveries
        house = houses[0]
        print("elf is delivering presents to", house)

    else:
        mid = len(houses) // 2  # in the case that there is more than one house and a manager is involved
        first_half = houses[:mid]
        second_half = houses[mid:]

        # The manager will divide the number of houses and half and assign to more elves
        # This will continue into there is only one house to one elf

        deliver_recursively(first_half)
        deliver_recursively(second_half)

deliver_recursively(houses)

print("\nExample 3: recursive addition")
# In this example we want to keep picking apples untill we have 9 apples in the basket
def recursive_sum(number):
    '''
    Basically how to count 1+1+1+1 in the sense of recursive
    :param number:
    :return:
    '''
    if number == 9:
        print("The basket has 9 apples")
    elif number > 9:
        print("We have too many apples")
    else:
        print(f'We currently have {number} of apples, I\'m going to pick one')
        number += 1
        print("We now have", number, "apples")
        recursive_sum(number)

recursive_sum(1)

print("\nExample 4: List Recursion")

def list_sum_recursion(input_list):
    if input_list == []:  # this is the base case
        return 0

    else:  # Recursive Case ( We made a smaller version of it self with recursion)
        head = input_list[0]
        cut_list = input_list[1:]  # Cuts from the 1st Cardinal (Counting) position and beyond
        return head + list_sum_recursion(cut_list)  # "Return the head of the list, and cut it down again"


list = [5, 2, 3, 2, 1, 3]
new_list = list[3:]  # This should return [2, 1, 3]
new_list2 = list[5:]  # This would return [3]
print(new_list)
print(new_list2)
print("Now lets move onto the recursive example")
print(f"If I added all these numbers {list} they would add up to {list_sum_recursion(list)}")

print("\nExample 5: Fibonacci's numbers Feat lru_cache")
from functools import lru_cache

@lru_cache(maxsize=None)
# lru_cache is a decorator that caches results, This helps with the unnecessary re-computation of f(n) by checking the
# value before trying to compute it.

def fibonacci_recursive(n):
    print(f"Calculating f({n}) ", end=",")
    #  Base Case
    if n==0:
        return 0
    elif n==1:
        return 1

    # Recursive Case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
# fibonacci_recursive(n-2) causes the program to repeat But I don't have the definte answer to why.
fibonacci_recursive(5)