"""
Question 1: Read a file that contains a shop's item stock. create a program that parses the file and builds a
dictionary. Then output the available stock in alphabet order.
"""

import sys
from string import punctuation as punc


def shop_stock():

    inventory = {}

    filename = sys.argv[1]

    with open(filename, "r") as f:
        #  Read input data line by line
        for line in f.readlines():
            tokens = line.strip().split()

            # Each line is now a list called Tokens e.g ['Energy', 'Drinks', '8']

            # Last element in the list is the value, every thing else is the key
            stock = tokens[-1]
            product_name = " ".join(tokens[:-1])  # Everything behind the last element

            inventory[product_name] = stock

    # Find the longest key for formatting
    longest_key = 0
    for product in inventory.keys():
        if len(product) > longest_key:
            longest_key = len(product)

    # Format the output with sorted keys
    for (product, stock) in sorted(inventory.items()):
        print("{:>{}s} : {}".format(product, longest_key, stock))


# shop_stock()


"""
Question 2: Write a program that reads a txt file of CONTACT DETAILS, each CONTACT will have: NAME, NUMBER, & EMAIL
Your dictionary should map from the name ( Key: NAME Value: NUMBER & EMAIL )
INPUT: should be a single NAME
OUTPUT: should be NUMBER & EMAIL
"""


def contact_search():
    # create a dictionary
    contacts = {}

    # Open system file

    filename = sys.argv[1]

    # Read system file
    with open(filename, "r") as f:
        # Read file line by line
        for line in f.readlines():  # for file named f read line by line and set to variable "line"
            tokens = line.strip().split()  # for each line create a list of items separated by the spaces in between

            # Designate each list item as a working variable
            name = tokens[0]
            email = tokens[1]
            phone = tokens[2]

            # Append dictionary items so that name is the KEY and email & phone is the VALUE
            contacts[name] = {"phone": phone, "email": email}

            # User input, and search for name from dictionary
            user_search = input("Please enter a name to search: ")

            while user_search:  # Run this loop as long as there is an input
                if user_search in contacts:
                    print("Name: " + user_search)
                    print("Email: " + contacts[user_search]["email"])
                    print("Phone: " + contacts[user_search]["phone"])

                else:
                    print("No such contact found. Please try again...")

                user_search = input()


# contact_search()

"""
Question 3: Create a program that counts and outputs how many times a word appears in a text.

* Punctuation Matters
* Should not be Case-sensitive

"""


def word_counter():

    # Select file input
    filename = sys.argv[1]

    # Create Dictionary
    word_count = {}

    # read and strip
    with open(filename, "r") as f:
        full_txt = f.read().strip()

    # Change all letters to lower-case to allow case sensitivity
    full_txt = full_txt.lower()

    # split text to words
    words = full_txt.split()

    # Conditions
    # Remove Punctiation from words
    for word in words:
        if word[0] in punc:
            word = word.replace(word[0], "")
        elif word[-1] in punc:
            word = word.replace(word[-1], "")
        # Add items to word count dictionary or add to the count if it exits prior
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    # Show the word count
    for word, count in word_count.items():
        print(word + " : " + str(count))


word_counter()
