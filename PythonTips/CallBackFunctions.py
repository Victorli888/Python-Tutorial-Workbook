"""
Call back functions is a function that is passed into another function, to be called back later
Functions that accept other functions as parameters are known as higher order functions
"""


def main(quote, callback):  # we have 2 parameters (string, callback function) ( This is a Higher order function)
    myQuote = ("Like I always say " + quote)
    callback(myQuote)


def printQuote(quote):  # This is our call back function
    print(quote)


main("Not even close baby.", printQuote)


"""
How it interprets:
1. quote = "Not even close baby.", callback = printQuote
2. myQuote = Like I always say Not even close baby
3. callback(myQuote)
4. printQuote(myQuote)
5. print(myQuote)
>>> Like I always say Not even close baby 
"""

"""
When do we practically use Call Back Functions?
Typically when we want our program to act in a SYNCHRONOUS manner, meaning we want our operations to start only after 
the preceding ones have completed.

For example, requesting data from other sources like an external API we don't always know when our data will be served
back. In these instances we want to wait for a response but we don't want our entire application to grind to a halt while
data is being fetched.
"""