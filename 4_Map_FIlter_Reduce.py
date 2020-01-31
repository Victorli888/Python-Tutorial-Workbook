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

class Example2():
    def __init__(self, x):
        self.x = x

    def mult(self):
        return self.x*self.x


    def divide(self):
        return self.x/self.x

    def add(self, x):
        return self.x+self.x

    def sub(self, x):
        return self.x-self.x


values = list(range(1, 11))
functions = (Example2.mult(x), Example2.divide(x), Example2.add(x), Example2.sub(x))
