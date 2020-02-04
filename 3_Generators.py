# Iterators: an Object that allows one to transverse a container (list). Iterators gives access  to data
# elements in that container but doesn't perform an iteration. Three parts [iterable, iterator, iteration]

# 3.1. Iterable [iterable provides an Iterator]
# An iterable is any object in Python which has an __iter__ or a __getitem__ method defined which returns
# an iterator or can take indexes (You can read more about them here). In short an iterable is any object
# which can provide us with an iterator. So what is an iterator? [iterable provides an Iterator]

# 3.2. Iterator [anything with __next__]
# An iterator is any object in Python which has a next (Python2) or __next__ method defined. That’s it.
# That’s an iterator. Now let’s understand iteration.

# 3.3. Iteration [Using a loop]
# In simple words it is the process of taking an item from something e.g a list. When we use a loop to
# loop over something it is called iteration. It is the name given to the process itself. Now as we
# have a basic understanding of these terms let’s understand generators.

# 3.4 Generators [Iterators that only iterate once]
print("Example 1: Generate 0, 2, 4, 6, 8")

def generator_function():
    for i in range(5):
        math = i + i
        yield math


for item in generator_function():
    print(item)

print("\nPrint Fibonacci's Numbers")


def fibon1(n):  # this uses much less memory because because yield doesn't store the entire sequence into memory
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibon2(n):  # this method takes up a lot of memory
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


for x in fibon1(5):
    print(x)

print("\nExample 3: using the Next()")
# this allows access to the next element of a sequence, essentially allows you to run one iteration at a time.

def generator_function3():
    for i in range(3):
        yield i

gen = generator_function3()
print(next(gen))
print("pause")
print(next(gen))
print("pause")
print(next(gen))
print("If I do it one more time I fail")

print("\nExample 4: using iter()")
# strings are iterable but are not an iterator, using iter() we can make it an iterator
my_string = "This is a String"
my_iter = iter(my_string)
print(next(my_iter))
# print(next(my_string))  # this fails, outputs: TypeError: 'str' object is not an iterator
