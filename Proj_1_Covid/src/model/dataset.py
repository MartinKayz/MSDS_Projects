""" This module is responsible for creating the data set for the collected data """
import csv 
from district import District
from Covid_19 import add_district

class DataSet:

    def __init__(self):
        print("Making a data set for our program...")

    
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
    print("I am being run as a module")