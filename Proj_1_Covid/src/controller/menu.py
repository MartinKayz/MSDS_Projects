import sys, csv

sys.path.append("../model/")
sys.path.append("../view/")

from Covid_19 import COVID19Uganda
from district import District

covid = COVID19Uganda()

while True:
    print("Enter\n 1 to add a district,\n 2 to retrieve district information,\n 3 to retrieve total statistics,\n 4 to retrieve average statistics,\n or Q to exit.")
    choice = input("Enter your choice: ")

    if choice == "Q" or 'q':
        break
    elif choice == '1':
        covid.add_district()
    elif choice == '2':
        name = input("Enter district name: ")
        print(covid.get_district_info(name))
    elif choice == '3':
        print("Total cases:", covid.get_total_cases())
        print("Total hospitalizations:", covid.get_total_hospitalizations())
        print("Total deaths:", covid.get_total_deaths())
    elif choice == '4':
        print("Average cases:", covid.get_average_data())
        print("Average hospitalizations:", covid.get_average_hospitalizations())
        print("Average deaths:", covid.get_average_deaths())
    else:
        print("Invalid choice.")
