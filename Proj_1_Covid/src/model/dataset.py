""" This module is responsible for creating the data set for the collected data """
import csv 
from district import District
from Covid_19 import add_district
import pandas as pd

# # Create an empty DataFrame

# data = {}
# df = pd.DataFrame(columns=['district_name','num_of_confirmed_cases', 'num_of_hospitalizations', 'num_of_deaths' ])
# data['district_name'] = district_name
# data['num_of_confirmed_cases'] = num_of_confirmed_cases
# data['num_of_hospitalizations'] = num_of_hospitalizations
# data['num_of_deaths'] = num_of_deaths


# df = df.append(data, ignore_index=True)
# print(df)


    
def construct_data_set(self, file_name):
    with open(file_name) as data_set:
        reader = csv.reader(data_set)
        for row in reader:
            district_name, confirmed_cases, hospitalizations, deaths = row
            confirmed_cases = int(confirmed_cases)
            hospitalizations = int(hospitalizations)
            deaths = int(deaths)
            district = District(district_name,confirmed_cases,hospitalizations, deaths)
            self.add_district(district)


if __name__ == "__main__":
    print("I am being run as a module to create a data set ")