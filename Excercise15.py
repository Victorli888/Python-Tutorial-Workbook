"""This is a reading excercise for Object-Oriented Vocabulary"""
import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, *** params.",
        "class %%% has-a __init__that takes self and *** params.",
    "class %%%(object: \n\tdef ***(self, @@@)":
        "class %%% has-a function"
