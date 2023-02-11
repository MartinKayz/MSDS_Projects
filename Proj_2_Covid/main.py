import csv
import requests
from api_call import get_data_from_api, covid_data_list, display_data, save_data_to_csv

def main():
    while True:
        print("\nMain Menu")
        print("1. Get data from API")
        print("2. Display data")
        print("3. Write data to file")
        print("Q. Quit")
        choice = input("Enter your choice: ").strip().upper()
        if choice == "Q" or choice == "QUIT":
            break
        elif choice == "1":
            get_data_from_api()
        elif choice == "2":
            covid_data_list = get_data_from_api()
            if len(covid_data_list) > 0:
                display_data(covid_data_list)
            else:
                print("Data not found. Please fetch data from API first.")
        elif choice == "3":
            covid_data_list = get_data_from_api()
            save_data_to_csv(covid_data_list)
        else:
            print("Invalid option")


main()