import sys

sys.path.append("../model/")
sys.path.append("../view/")

from Covid_19 import COVID19Uganda
from district import District

covid = COVID19Uganda()

while True:
    print("Enter 1 to add a district, 2 to retrieve district information, 3 to retrieve total statistics, 4 to retrieve average statistics, or Q to exit.")
    choice = int(input("Enter your choice: "))

    if choice == "Q":
        break
    elif choice == 1:
        name = input("Enter district name: ")
        confirmed_cases = int(input("Enter number of confirmed cases: "))
        hospitalizations = int(input("Enter number of hospitalizations: "))
        deaths = int(input("Enter number of deaths: "))

        district = District(name, confirmed_cases, hospitalizations, deaths)
        covid.add_district(district)
    elif choice == 2:
        name = input("Enter district name: ")
        print(covid.get_district_info(name))
    elif choice == 3:
        print("Total cases:", covid.get_total_cases())
        print("Total hospitalizations:", covid.get_total_hospitalizations())
        print("Total deaths:", covid.get_total_deaths())
    elif choice == 4:
        print("Average cases:", covid.get_average_cases())
        print("Average hospitalizations:", covid.get_average_hospitalizations())
        print("Average deaths:", covid.get_average_deaths())
    else:
        print("Invalid choice.")
