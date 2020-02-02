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
    print(f"for {i} the math solutions are : {solution}")
