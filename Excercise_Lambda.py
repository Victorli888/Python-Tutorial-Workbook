# In a layman's terms the lambda function works similarly to a f(x)
# in a math expression. Take from below for example.


# Normally you could create a defined function:
def remainder(num):
    return num % 2
print(remainder(5))
# you could also right this as
remainder1 = lambda num: num % 2
print(remainder1(5))
# read as f(x) = x % 2
# print f(5) = 5 % 2
# f(5) = 1

# we can also do this for multiplication
product = lambda x, y : x * y
print(product(5,2))

# read as: set product to f(x,y) = x * y
# print the value of f(5,2) = 5 * 2, output = 10


numlist = [2, 3, 14, 53, 2, 4, 6, 7, 4, 6]
# create a list of numbers and from find the remainder divisible by 2

maplist = list(map(lambda num: num > 7, numlist))
print(maplist)
# read as: return a mutable list and map f(num) = num > 7 for each item in numlist
# output = False or True depending on whether or not num is greater than 7

filterlist = list(filter(lambda num: num > 7, numlist))
print(filterlist)
# read as: return a mutable list and filter numbers if f(x) = x > 7 for each item in numlist
# output: Numbers that are not greater than 7 will be popped from numlist

filterlist2 = list(filter(lambda num : num % 2, numlist))
print(filterlist2)
# read as: return a mutable list and filter all numbers based on...
# f(x) = x modulo 2 from each item in numlist
# output: any number from numlist which has a remainder from dividing 2 will be added to the new list

maplist2 = list(map(lambda num: num % 2, numlist))
print(maplist2)
# read as: create a mutable list and map each number with modulo 2 in numlist.
# output: each item in num list will run modulo 2 and be added to the new list
