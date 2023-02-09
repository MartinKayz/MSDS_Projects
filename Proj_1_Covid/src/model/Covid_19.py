""" This module represents the COVID-19 data for all districts in Uganda"""
import sys,csv

sys.path.append("../model/")
from district import District
import pandas as pd

class COVID19Uganda:
    # district_data = District(district_name="Mukono", num_of_confirmed_cases=0, num_of_hospitalizations=0, num_of_deaths=0)
    
    def __init__(self):
        print("Initializing the data")
        # self.districts = []
        


    def add_district(self, district_name, num_of_confirmed_cases, num_of_hospitalizations, num_of_deaths):
        """This method adds a new district to the data set"""
        # self.districts.append(district_name)
        district_data = District(district_name,num_of_confirmed_cases, num_of_hospitalizations, num_of_deaths)
        
        # data_df = {}
        # for attr in ['district_name', 'num_of_confirmed_cases', 'num_of_hospitalizations', 'num_of_deaths']:
        #     data_df[attr] = getattr(district_data, attr)
        # print(data_df)

        # with open('covid.csv', 'a', newline='') as file:
        #     writer = csv.DictWriter(file, fieldnames=['district_name', 'num_of_confirmed_cases', 'num_of_hospitalizations', 'num_of_deaths'])
        #     writer.writeheader()
        #     for row in zip(data_df.values()):
        #         writer.writerow(dict(zip(data_df.keys(), row)))
        
        
        
        

    
    def retrieve_district_cases(self, district_name):
        """
        This method retrieves the number of confirmed cases, hospitalizations, and
        deaths for a specific district
        """
        for district in self.districts:
            if district.district_name == district_name:
                return district
        return None
        

    def retrieve_total_cases(self, confirmed_cases_total, hospitalizations_total, deaths_total):
        """
        This method retrieves the total number of confirmed cases, hospitalizations,
        and deaths for all districts
        """
        confirmed_cases_total = 0
        hospitalizations_total = 0
        deaths_total = 0
        for district in self.districts:
            confirmed_cases_total += district.num_of_comfirmed_cases
            hospitalizations_total += district.num_of_hospitalizations
            deaths_total += district.num_of_deaths
        return confirmed_cases_total, hospitalizations_total, deaths_total

    def retrieve_average_cases(self, confirmed_cases, hospitalizations, deaths):
        """
        This method retrieves the average number of confirmed cases, hospitalizations,
        and deaths for all districts
        """
        confirmed_cases_total, hospitalizations_total, deaths_total = self.retrieve_total_cases()
        return confirmed_cases_total/len(self.districts), hospitalizations_total/len(self.districts), deaths_total/len(self.districts)


    def visualize_data(self):
        """ This method visualizes our data from the data set """
        confirmed_cases = [district.confirmed_cases for district in self.districts]
        hospitalizations = [district.hospitalizations for district in self.districts]
        deaths = [district.deaths for district in self.districts]

        district_names = [district.district_name for district in self.districts]

        fig, ax = plt.subplots()
        ax.bar(district_names, confirmed_cases, label="Confirmed Cases")
        ax.bar(district_names, hospitalizations, label="Hospitalizations")
        ax.bar(district_names, deaths, label="Deaths")

        ax.legend()
        plt.show()



if __name__ == "__main__":
    print("I am being run directly as a Covid_19 module...")
