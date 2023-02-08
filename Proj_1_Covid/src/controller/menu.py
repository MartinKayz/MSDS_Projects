import sys

sys.path.append("../model/")
sys.path.append("../view/")


from Covid_19 import COVID19Uganda
from district import District
from visuals import Visuals

def main():
    covid_data = COVID19Uganda()

    choices = {
        '1': covid_data.add_district,
        '2': covid_data.retrieve_district_cases,
        '3': covid_data.retrieve_total_cases,
        '4': covid_data.retrieve_average_cases,
        '5': covid_data.visualize_data,
        '6': covid_data.load_data_from_file,
        '7': covid_data.save_data_to_file,
        'Q': quit
    }

    while True:
        print("\nCOVID-19 Data Analysis for Uganda\n")
        print("1. Add district")
        print("2. Retrieve district data")
        print("3. Retrieve total data")
        print("4. Retrieve average data")
        print("5. Visualize data")
        print("6. Load data from file")
        print("7. Save data to file")
        print("Q. Quit\n")

        choice = input("Enter choice: ").upper()

        if choice in choices:
            if choice == '1':
                district_name = input("Enter district name: ")
                num_of_confirmed_cases = int(input("Enter number of confirmed cases: "))
                num_of_hospitalizations = int(input("Enter number of hospitalizations: "))
                num_of_deaths = int(input("Enter number of deaths: "))
                district = District(district_name,num_of_confirmed_cases,num_of_hospitalizations ,num_of_deaths)
                choices[choice](district)
            elif choice == '2':
                district_name = input("Enter district name: ")
                district_data = choices[choice](district_name)
                if district_data:
                    print("District: ", district_data.name)
                    print("Confirmed Cases: ", district_data.num_of_comfirmed_cases)
                    print("Hospitalizations: ", district_data.num_of_hospitalizations)
                    print("Deaths: ", district_data.num_of_deaths)
                else:
                    print("District not found.")
            elif choice in ['3', '4']:
                data = choices[choice]()
                print(f"{'Total' if choice == '3' else 'Average'} Confirmed Cases: ", data[0])
                print(f"{'Total' if choice == '3' else 'Average'} Hospitalizations: ", data[1])
                print(f"{'Total' if choice == '3' else 'Average'} Deaths: ", data[2])
            else:
                choices[choice]()
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()

