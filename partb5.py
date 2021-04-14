## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
import math
from IPython.display import display









# import the tools to handle the keywords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

# import the two functions all_alpha(word) and preprocessing(text) from partb2
def all_alpha(word):
    result = "".join([char for char in word if char.isalpha()])
    if result != "":
        return result

def preprocessing(text):
    pre_text = " ".join([all_alpha(word) for word in text.split() if all_alpha(word)])
    return pre_text.lower()



os.chdir("/home/jovyan/Assignment 1/cricket")
b4_df = pd.read_csv("partb1.csv")

# a function that transform words in the whole text to normal form
def text_stem(text):
    words = word_tokenize(text)
    return (" ".join([PorterStemmer().stem(word) for word in words]))



doc_ID = []
temp_scores = []
open_times = len(b4_df["filename"])
for i in range(open_times):
    readfile = open(b4_df["filename"][i], "r")
    text = preprocessing(readfile.read())
    text = text_stem(text)
    
    # same logic in partb3
    if (1<=len(sys.argv[1:])<=5):
        keywords = sys.argv[1:]
    else:
        print("Please enter 1 to 5 keywords and try again.")
        break
    
    # transform each keyword to normal form, prepare for further comparison
    for keyword in keywords:
        keywords = [PorterStemmer().stem(keyword)]   
    
    for keyword in keywords:
        if not re.search(r"\b" + keyword.lower() + r"\b", text):
            # all 3 should be satisfied
            break
            
        if keyword == keywords[-1]:
            # if all keywords are matched then print the ID
            doc_ID.append(b4_df["documentID"][i])
            break
            
            
            
            
#mycol = ["documentID", "score"]
#b5_df = pd.DataFrame(columns = mycol)
d = {'documentID':doc_ID, 'score':temp_scores}
df = pd.DataFrame(d)
display(df)
#doc_tfidf = tfidf.toarray()

from numpy import dot
from numpy.linalg import norm
def cosine_sim(v1, v2):
    return dot(v1, v2)/(norm(v1)*norm(v2))