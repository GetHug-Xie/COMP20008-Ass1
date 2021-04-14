import pandas as pd
import argparse
import matplotlib.pyplot as plt
import math

covid19_data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
covid19_data["month"] = [date[5:7] for date in covid19_data["date"].values]
covid19_data["year"] = [date[:4] for date in covid19_data["date"].values]
data_2020 = covid19_data[covid19_data["year"] == '2020']
location_list = list(set(data_2020["location"]))
month_list = list(set(data_2020["month"]))
df_column = ["location", "month", "total_cases","new_cases", "total_deaths", "new_deaths"]
part_a_df = pd.DataFrame(columns = df_column)

for location in location_list:
    total_cases = 0
    total_deaths = 0
    for month in month_list:
        emptylist = [location, month]
        tempdata = data_2020[data_2020["location"] == location].where(data_2020["month"] == month)

        total_cases = total_cases + tempdata["new_cases"].sum()
        emptylist.append(total_cases)
        emptylist.append(tempdata["new_cases"].sum())
        
        total_deaths = total_deaths + tempdata["new_deaths"].sum()
        emptylist.append(total_deaths)
        emptylist.append(tempdata["new_deaths"].sum())
        
        list_series = pd.Series(emptylist, index = df_column)
        part_a_df = part_a_df.append(list_series, ignore_index = True)

part_a_df.insert(2, "case_fatality_rate", part_a_df["new_deaths"] / part_a_df["new_cases"])



# codes from parta1.py from this line above
####################################################################################################

groups = part_a_df.groupby("location")

# the graph of scatter-a
plt.figure(figsize=(15,15))
for name, group in groups:
    # count the total new_cases in 2020
    x = sum(group["new_cases"])
    # for some reasons some values are negative, ignore them
    if sum(group["new_cases"]) <= 0:
        y = 0
    # just calculate the normal data
    else:
        y = sum(group["new_deaths"]) / sum(group["new_cases"])
    plt.plot(x, y, marker='*', linestyle='', label=name)

plt.xlabel('confirmed new cases', fontsize=10)
plt.ylabel('case fatality rate', fontsize=10)
plt.title('Scatter-a')
# plot the legend outside the graph as it involves too many countries
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('scatter-a.png')
plt.show()



# the graph of scatter-b
plt.figure(figsize=(15,15))
for name, group in groups:
    x = sum(group["new_cases"])
    # skip the 0 values as log0 is undefined in math
    if (x > 0):
        log_x = math.log(x)
    if sum(group["new_cases"]) <= 0:
        y = 0
    else:
        y = sum(group["new_deaths"]) / sum(group["new_cases"])
    plt.plot(log_x, y, marker='^', linestyle='', label=name)

plt.xlabel('confirmed new cases', fontsize=10)
plt.ylabel('case fatality rate', fontsize=10)
plt.title('Scatter-b')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('scatter-b.png')
plt.show()