# Part B Task 2
import re
import os
import sys

# access the path to the cricket data
os.chdir("/home/jovyan/Assignment 1/cricket")
filename = "001.txt"
readfile = open(filename, "r")
content = readfile.read()

# a function that removes all non-alphabetic characters in a word
def all_alpha(word):
    result = "".join([char for char in word if char.isalpha()])
    # stop when the current word ends
    if result != "":
        return result

# a function that deal with three preprocessing steps
def preprocessing(text):
    # leave only one whitespace character between each alphabetic word
    pre_text = " ".join([all_alpha(word) for word in text.split() if all_alpha(word)])
    # change all uppercase characters to lower case
    return pre_text.lower()

print(preprocessing(content))