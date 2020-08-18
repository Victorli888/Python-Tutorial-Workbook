"""
Memoization ensures that a function doesn't run the same inputs more than once by keeping a record of the results
for the given inputs (Usually in a dictionary)


Take for example a simple recursive function!
"""


def recursive_fib(n):
    if n < 0:
        raise IndexError(
            "index was negative"
            "No such thing as negative index in this series"
        )
    elif n in [0, 1]:
        # Base case
        return n

    print("computing fib(%i)" % n)
    return recursive_fib(n - 1) + recursive_fib(n - 2)


class Fibber:

    def __init__(self):
        self.memo = {}

    def fib(self, n):

        if n < 0:
            raise IndexError(
                "index was negative"
                "No such thing as negative index in this series"
            )

        # Base cases
        if n in [0, 1]:
            return n

        # See if we've already calculated this
        if n in self.memo:
            print(f"grabbing from memo[{n}]")
            return self.memo[n]

        print(f"computing fib({n})")
        result = self.fib(n - 1) + self.fib(n - 2)

        # Memorize
        self.memo[n] = result
    
        return result


print(Fibber().fib(4))
