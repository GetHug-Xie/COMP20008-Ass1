import pandas as pd
import argparse

covid19_data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
# locate the months and years from date
covid19_data["month"] = [date[5:7] for date in covid19_data["date"].values]
covid19_data["year"] = [date[:4] for date in covid19_data["date"].values]

data_2020 = covid19_data[covid19_data["year"] == '2020']

# store the locations and months temporarily in lists to read through later
location_list = list(set(data_2020["location"]))
month_list = list(set(data_2020["month"]))

df_column = ["location", "month", "total_cases","new_cases", "total_deaths", "new_deaths"]
part_a_df = pd.DataFrame(columns = df_column)

# go through every country and month
for location in location_list:
    # initialise the smount then count the total cases/deaths in each country
    total_cases = 0
    total_deaths = 0
    
    for month in month_list:
        # create an empty list to store all data required
        emptylist = [location, month]
        # use the temp data to fill the empty list
        tempdata = data_2020[data_2020["location"] == location].where(data_2020["month"] == month)
        
        total_cases = total_cases + tempdata["new_cases"].sum()
        emptylist.append(total_cases)
        emptylist.append(tempdata["new_cases"].sum())
        
        total_deaths = total_deaths + tempdata["new_deaths"].sum()
        emptylist.append(total_deaths)
        emptylist.append(tempdata["new_deaths"].sum())
        
        # transform the filled list to a series as list cannot be appenened to a dataframe
        list_series = pd.Series(emptylist, index = df_column)
        part_a_df = part_a_df.append(list_series, ignore_index = True)

        
part_a_df.insert(2, "case_fatality_rate", part_a_df["new_deaths"] / part_a_df["new_cases"])
# sort by location then month
part_a_df.sort_values(by=['location', 'month'])
print(part_a_df.head())
part_a_df.to_csv("owid-covid-data-2020-monthly.csv", index=False)