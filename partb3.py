## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os

# path to the files and partb1.csv
os.chdir("/home/jovyan/Assignment 1/cricket")
b3_df = pd.read_csv("partb1.csv")

# import the two functions all_alpha(word) and preprocessing(text) from partb2
def all_alpha(word):
    result = "".join([char for char in word if char.isalpha()])
    if result != "":
        return result

def preprocessing(text):
    pre_text = " ".join([all_alpha(word) for word in text.split() if all_alpha(word)])
    return pre_text.lower()



open_times = len(b3_df["filename"])
# read through each file and search for keywords
for i in range(open_times):
    readfile = open(b3_df["filename"][i], "r")
    # perform the preprocessing in Task 2
    text = preprocessing(readfile.read())
    
    # at position 0, the first word is partb3.py
    # between 1 and 5 keywords will be entered
    if (1<=len(sys.argv[1:])<=5):
        keywords = sys.argv[1:]
    else:
        print("Please enter 1 to 5 keywords and try again.")
        break
        
    for keyword in keywords:
        # text is already in lower case, lower the keywords for comparison
        if not re.search(r"\b" + keyword.lower() + r"\b", text):
            # break and move to the next file if keyword is not found
            break
        
        # if current word is the last one then all keywords are matched
        if keyword == keywords[-1]:
            # if all keywords are matched then print the ID
            print(b3_df["documentID"][i])
            break