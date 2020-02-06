from functools import reduce
# map applies a function to all items in an input-list
# map(function to apply, [list of inputs])
print("Example 1: Map() Square the number")
items = [1, 2, 3, 4, 5]


def square(items):
    squared_nums = []
    for i in items:
        squared_nums.append(i**2)
    return squared_nums


def map_square(items):
    squared = list(map(lambda x: x**2, items))
    return squared


print(f"Using a for loop method we get: {square(items)}")
print(f"This time using Map() method we get: {map_square(items)}")

print("\nExample 2: A lot of Math home work")
# in this example you need to multiply, divide, add, and subtract all the numbers from 1 to 10.
# 1*1, 1/1, 1-1, 1+1 etc...


class Math:
    def mult(x):
        return x*x

    def divide(x):
        return x//x

    def add(x):
        return x+x

    def sub(x):
        return x-x


values = list(range(1, 11))
functions = (Math.mult, Math.divide, Math.add, Math.sub)

for i in values:
    solution = list(map(lambda x: x(i), functions))
    print(f"for {i} the math solutions are: {solution}")

# 4.2 Filter
# Filter creates a list of elements for which a function returns TRUE.
print("\nExample 3: Using filter()")
number_list = list(range(-5, 5))
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(f"From the range these numbers are less than 0: {less_than_zero}")


print("\nExample 4 From Example 2, I don't like the 0 at the end of each solution... Remove it")

for i in values:
    solution = list(map(lambda x: x(i), functions))
    filter_zero = list(filter(lambda x: x > 0, solution))
    print(f"for {i} the new math solutions are: {filter_zero}")

# 4.3 Reduce
# Performing computation on a list and returning the result
print("\nExample 5: Compute the product for a list of integers")
product = 1
list1 = list(range(1, 5))
for num in list1:
    product = product * num
print(f"the product of {list1} = {product}")

print("\nExample 6: This time using the reduce() method")
# using the reduce() we can do the same thing
product5 = reduce((lambda x5, y5: x5 * y5), list1)
print(f"the product of {list1} is {product5}")

print("\nExample 7 Sum up all the problems in your Math Homework")
for i in values:
    solution = list(map(lambda x: x(i), functions))
    filter_zero = list(filter(lambda x: x > 0, solution))
    final_sum = reduce((lambda x6, y6: x6 + y6), filter_zero)
    print(f"For {filter_zero}, The final sum is: {final_sum}")
# SUMMARY:
# map() applies a function to items in an input list
# filter() If the item passes (true) KEEP IT, and if it fails (false) item is "filtered"
# reduce() applies a function to items in an input list, BUT ONLY RETURNS THE RESULT
