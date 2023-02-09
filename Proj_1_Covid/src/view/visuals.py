""" This Module is reponsible for showing the visualizations of the data """
import sys

sys.path.append("../model/")

from Covid_19 import COVID19Uganda
import pandas as pd
import matplotlib.pyplot as plt

covid = COVID19Uganda()
covid.read_districts_from_csv()

# Create a pandas DataFrame from the districts data
# Create a pandas DataFrame from the districts data
data = {"District": [d.name for d in covid.districts],
        "Cases": [d.cases for d in covid.districts],
        "Hospitalizations": [d.hospitalizations for d in covid.districts],
        "Deaths": [d.deaths for d in covid.districts]}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

    
    