""" This module is an endpoint to collect data from the web about Covid 19 """

class Collect_Data:
    country_name: str
    cases: int
    deaths: int
    region: str
    total_recovered: int
    new_deaths: int
    new_cases: int
    serious_critical: int
    active_cases:int 
    total_cases_per_1m_population: int


    def __init__(self, country_name, cases, deaths, region, total_recovered, new_deaths, new_cases, serious_critial, active_cases, total_cases_per_1m_population):
        # print("Initializing our object")
        self.country_name = country_name
        self.cases = cases
        self.deaths = deaths
        self.region = region
        self.total_recovered = total_recovered
        self.new_deaths = new_deaths
        self.new_cases = new_cases
        self.serious_critical = serious_critial
        self.active_cases = active_cases
        self.total_cases_per_1m_population = total_cases_per_1m_population

    def __repr__(self):
        return f"{self.country_name} | Cases: {self.cases} | Deaths: {self.deaths} | Region: {self.region} | Total Recovered: {self.total_recovered} | New Deaths: {self.new_deaths} | New Cases: {self.new_cases} | Serious/Critical: {self.serious_critical} | Active Cases: {self.active_cases} | Total Cases per 1M Population: {self.total_cases_per_1m_population}"

    
    def get_country_name(self):
        return self.country_name
    
    def set_country_name(self, country_name):
        self.country_name = country_name
        
    def get_cases(self):
        return self.cases
    
    def set_cases(self, cases):
        self.cases = cases
        
    def get_deaths(self):
        return self.deaths
    
    def set_deaths(self, deaths):
        self.deaths = deaths
        
    def get_region(self):
        return self.region
    
    def set_region(self, region):
        self.region = region
        
    def get_total_recovered(self):
        return self.total_recovered
    
    def set_total_recovered(self, total_recovered):
        self.total_recovered = total_recovered
        
    def get_new_deaths(self):
        return self.new_deaths
    
    def set_new_deaths(self, new_deaths):
        self.new_deaths = new_deaths
        
    def get_new_cases(self):
        return self.new_cases
    
    def set_new_cases(self, new_cases):
        self.new_cases = new_cases
        
    def get_serious_critical(self):
        return self.serious_critical
    
    def set_serious_critical(self, serious_critical):
        self.serious_critical = serious_critical
        
    def get_active_cases(self):
        return self.active_cases
    
    def set_active_cases(self, active_cases):
        self.active_cases = active_cases
        
    def get_total_cases_per_1m_population(self):
        return self.total_cases_per_1m_population
    
    def set_total_cases_per_1m_population(self, total_cases_per_1m_population):
        self.total_cases_per_1m_population = total_cases_per_1m_population


