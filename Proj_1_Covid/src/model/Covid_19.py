""" This module represents the COVID-19 data for all districts in Uganda"""
import sys,csv

sys.path.append("../model/")
from district import District
import pandas as pd


class COVID19Uganda:
    def _init_(self):
        self.districts = []

    def add_district(self, district):
        """This method adds a new district to the data set"""
        self.districts.append(district)
        with open("district_data.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([district.name, district.confirmed_cases, district.hospitalizations, district.deaths])

    def get_district_info(self, name):
        """
        This method retrieves the number of confirmed cases, hospitalizations, and
        deaths for a specific district
        """
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == name:
                    return District(row[0], int(row[1]), int(row[2]), int(row[3]))
            return None

    def get_total_cases(self):
        """
        This method retrieves the total number of confirmed cases, hospitalizations,
        and deaths for all districts
        """
        total_cases = 0
        total_hospitalizations = 0
        total_deaths = 0
        with open("district_data.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)  # skip the header row
            if header != ["District Name", "Confirmed Cases", "Hospitalizations", "Deaths"]:
                raise ValueError("The header in the csv file is invalid")
            for row in reader:
                total_cases += int(row[1])
                total_hospitalizations += int(row[2])
                total_deaths += int(row[3])
        return total_cases, total_hospitalizations, total_deaths

    def get_total_hospitalizations(self):
        total = 0
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total += int(row[2])
        return total

    def get_total_deaths(self):
        total = 0
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total += int(row[3])
        return total

    def get_average_cases(self):
        """
        This method retrieves the average number of confirmed cases, hospitalizations,
        and deaths for all districts
        """
        total = 0
        count = 0
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total += int(row[1])
                count += 1
        return total / count if count != 0 else 0

    def get_average_hospitalizations(self):
        total = 0
        count = 0
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total += int(row[2])
                count += 1
        return total / count if count != 0 else 0

    def get_average_deaths(self):
        total = 0
        count = 0
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total += int(row[3])
                count += 1
        return total / count if count != 0 else 0

    def read_districts_from_csv(self):
        with open("district_data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                district = District(row[0], int(row[1]), int(row[2]), int(row[3]))
                self.districts.append(district)



if __name__ == "__main__":
    print("I am being run directly as a Covid_19 module...")
