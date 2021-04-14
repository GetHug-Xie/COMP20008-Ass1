## Part B Task 1
import re
import pandas as pd
import os

b1_column = ["filename", "documentID"]
b1_df = pd.DataFrame(columns = b1_column)

# access the folder where the cricket data is stored
cricket_loc = os.chdir("/home/jovyan/Assignment 1/cricket")

file_name = []
for file in os.listdir(cricket_loc):
    # a condition to select files in the correct format
    if file.endswith("txt"):
        file_name.append(file)
        
pattern = r"[A-Z]{4}\-[0-9]{3}[A-Z]{0,1}"

for file in file_name:
    f = open(file, "r")
    text = f.read()
    
    # search for the potential pattern hidden in each text
    result = re.search(pattern, text).group()
    
    # similar to part a, transform the list to a series then append it to the dataframe
    listSeries = pd.Series([file, result], index = b1_column)
    b1_df = b1_df.append(listSeries, ignore_index = True)
    
b1_df.to_csv("partb1.csv", index = False)