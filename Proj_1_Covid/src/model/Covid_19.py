""" This module represents the COVID-19 data for all districts in Uganda"""
import sys,csv,os

sys.path.append("../model/")
from district import District
import pandas as pd
import matplotlib.pyplot as plt


class COVID19Uganda:
    def __init__(self):
        self.data = pd.read_csv("../controller/covid.csv")
        self.districts = []

    def add_district(self):
        """This method adds a new district to the data set"""
        """This method adds a new district to the data set"""
        district_name = input("Enter the name of the district: ")
        confirmed_cases = input("Enter the number of confirmed cases: ")
        hospitalizations = input("Enter the number of hospitalizations: ")
        deaths = input("Enter the number of deaths: ")
        district = District(district_name, confirmed_cases, hospitalizations, deaths)
        self.districts.append(district)

        with open("covid.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            header = ["Name", "Confirmed Cases", "Hospitalizations", "Deaths"]
            try:
                with open("covid.csv") as f:
                    # Read the first line to check if it's the header
                    first_line = f.readline().strip().split(",")
                    if first_line == header:
                        # If it's the header, skip it
                        writer.writerow([district.district_name, district.num_of_confirmed_cases, district.num_of_hospitalizations, district.num_of_deaths])
                    else:
                        # If it's not the header, write the header and the data
                        writer.writerow(header)
                        writer.writerow([district.district_name, district.num_of_confirmed_cases, district.num_of_hospitalizations, district.num_of_deaths])
            except FileNotFoundError:
                # If the file doesn't exist, write the header and the data
                writer.writerow(header)
                writer.writerow([district.name, district.confirmed_cases, district.hospitalizations, district.deaths])

        
    def get_district_info(self, district_name):
        """
        This method retrieves the number of confirmed cases, hospitalizations, and
        deaths for a specific district
        """
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                if row[0] == district_name:
                    confirmed_cases = row[1]
                    hospitalizations = row[2]
                    deaths = row[3]
                    return (confirmed_cases, hospitalizations, deaths)
        return None

    def get_total_cases(self):
        """
        This method retrieves the total number of confirmed cases, hospitalizations,
        and deaths for all districts
        """
        total_cases = 0
        total_hospitalizations = 0
        total_deaths = 0
        with open("../controller/covid.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)  # skip the header row
            for row in reader:
                total_cases += int(row[1])
                total_hospitalizations += int(row[2])
                total_deaths += int(row[3])
        return total_cases, total_hospitalizations, total_deaths

    def get_total_hospitalizations(self):
        total = 0
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                total += int(row[2])
        return total

    def get_total_deaths(self):
        total = 0
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                total += int(row[3])
        return total

    def get_average_data(self):
        """This method retrieves the average number of confirmed cases, hospitalizations, and deaths for all districts"""
        total_confirmed_cases = 0
        total_hospitalizations = 0
        total_deaths = 0
        district_count = 0

        with open("../controller/covid.csv") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                total_confirmed_cases += int(row[1])
                total_hospitalizations += int(row[2])
                total_deaths += int(row[3])
                district_count += 1

        return (total_confirmed_cases/district_count, total_hospitalizations/district_count, total_deaths/district_count)




    def get_average_hospitalizations(self):
        total = 0
        count = 0
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                total += int(row[2])
                count += 1
        return total / count if count != 0 else 0

    def get_average_deaths(self):
        total = 0
        count = 0
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                total += int(row[3])
                count += 1
        return total / count if count != 0 else 0

    def read_districts_from_csv(self):
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                district = District(row[0], int(row[1]), int(row[2]), int(row[3]))
                self.districts.append(district)
            return iter(self.districts)

    def generate_bar_graph(self):
        plt.bar(self.data['District_Name'], self.data['Confirmed Cases'], color='red', label='Confirmed Cases')
        plt.bar(self.data['District_Name'], self.data['Hospitalizations'], color='blue', label='Hospitalizations')
        plt.bar(self.data['District_Name'], self.data['Deaths'], color='green', label='Deaths')
        plt.xlabel('Districts')
        plt.ylabel('Cases/Hospitalizations/Deaths')
        plt.legend()

        if not os.path.exists('../view/visualizations'):
            os.makedirs('visualizations')
        plt.savefig('visualizations/bar_graph.png')
        plt.show()
        
    def generate_line_graph(self):
        with open("../controller/covid.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Skip header row
            district_data = {row[0]: {"Confirmed Cases": [], "Hospitalizations": [], "Deaths": []} for row in reader}

        # Extract data for each district
        for row in reader:
            district = row[0]
            district_data[district]["Confirmed Cases"].append(int(row[1]))
            district_data[district]["Hospitalizations"].append(int(row[2]))
            district_data[district]["Deaths"].append(int(row[3]))

        # Generate line charts for each district
        for district, data in district_data.items():
            fig, ax = plt.subplots()
            ax.plot(data["Confirmed Cases"], label="Confirmed Cases")
            ax.plot(data["Hospitalizations"], label="Hospitalizations")
            ax.plot(data["Deaths"], label="Deaths")
            ax.legend()
            ax.set_xlabel("Time")
            ax.set_ylabel("Number of Cases")
            ax.set_title(f"COVID-19 Data for {district}")
            if not os.path.exists('../view/visualizations'):
                os.makedirs('visualizations')
            plt.savefig(f"visualizations/ {district}.png") 
            plt.show()  # Save the figure to a file
            plt.close()
            


if __name__ == "__main__":
    print("I am being run directly as a Covid_19 module...")
