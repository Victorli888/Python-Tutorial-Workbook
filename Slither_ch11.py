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


shop_stock()
