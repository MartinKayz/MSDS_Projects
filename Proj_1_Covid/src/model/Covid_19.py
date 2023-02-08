""" This module represents the COVID-19 data for all districts in Uganda"""

class COVID19Uganda:
    def __init__(self):
        print("Initializing the data")
        self.districts = []


    def add_district(self, district_name):
        """This method adds a new district to the data set"""
        self.districts.append(district_name)

    
    def retrieve_district_cases(self, district_name):
        """
        This method retrieves the number of confirmed cases, hospitalizations, and
        deaths for a specific district
        """
        for district in self.districts:
            if district.name == district_name:
                return district
        return None
        

    def retrieve_total_cases(self, confirmed_cases, hospitalizations, deaths):
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

        