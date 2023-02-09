""" This module represents  Covid_19 data about a particular district """

class District:
    
    def __init__(self, district_name, num_of_confirmed_cases, num_of_hospitalizations, num_of_deaths):
        self.district_name = district_name
        self.num_of_confirmed_cases = num_of_confirmed_cases
        self.num_of_hospitalizations = num_of_hospitalizations
        self.num_of_deaths = num_of_deaths


    
    def __repr__(self):
        data = [self.district_name, self.num_of_confirmed_cases, self.num_of_hospitalizations, self.num_of_deaths]
        return str(data)
    

    # def __iter__(self):
    #     return iter()