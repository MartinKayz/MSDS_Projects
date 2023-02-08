""" This Module is reponsible for showing the visualizations of the data """
import sys

sys.path.append("../model/")

import district

class Visuals:

    def __init__(self):
        print("Initializing the visualizations of our data...")

    
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