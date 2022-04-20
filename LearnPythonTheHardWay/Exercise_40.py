class Song(object):  # Classes are like Modules and Modules are like dictionaries

    def __init__(self, lyrics):
        self.lyrics = lyrics

    """
In this example your creating a "dictionary function" that will call back to whatever variable you set 
it to. For example, the "self" function below is a usable variable to call back to.
When you call on Song(Object = the portion you want represented in the code)

the "instaniate" operation is like calling a function but Python coordinates a sequence of events
for you behind the scenes. __init__ creates a variable called "self" and you can set it to values like
you would for a dictionary
"""
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
"""
Line 15: Create a user defined function defined as sing_me_a_song
line 16 & 17: for each line of definition lyrics in module self.lyrics print that line
"""

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here"])

""" The "Song" portion of the code references back to the class you made"""

bulls_on_parade = Song(["They rally around tha family",
                          "With Pockets full of shells"])

"""sing_me_a_song()  will call back on that user defined function"""

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
