import requests,csv
from covid_collect import Collect_Data

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    "X-RapidAPI-Key": "90165b2056msh5218e1ec6e762c2p1b30b0jsn0b7be9272e36",
    "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
}

covid_data_list = []
def get_data_from_api():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Successful request
        data = response.json()
        # print(data)
        
        for item in data['countries_stat']:
            covid_data = Collect_Data(item['country_name'], item['cases'], item['deaths'], item['region'], item['total_recovered'], item['new_deaths'], item['new_cases'], item['serious_critical'], item['active_cases'], item['total_cases_per_1m_population'])
            covid_data_list.append(covid_data)

    else:
        # Request failed
        print("Request failed with status code: ", response.status_code)
    
    return covid_data_list


def display_data(covid_data_list):
     for covid_data in covid_data_list:
            print(covid_data)


def save_data_to_csv(covid_data_list):
    if len(covid_data_list) > 0:
        with open("api_covid_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Country Name", "Cases", "Deaths", "Region", "Total Recovered", "New Deaths", "New Cases", "Serious/Critical", "Active Cases", "Total Cases per 1M Population"])
            for covid_data in covid_data_list:
                writer.writerow([covid_data.country_name, covid_data.cases, covid_data.deaths, covid_data.region, covid_data.total_recovered, covid_data.new_deaths, covid_data.new_cases, covid_data.serious_critical, covid_data.active_cases, covid_data.total_cases_per_1m_population])
                print("Data successfully written to file.")
    else:
        print("Data not found. Please fetch data from API first.")
