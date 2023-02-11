""" This Module is reponsible for showing the visualizations of the data """
import sys

sys.path.append("../model/")

from Covid_19 import COVID19Uganda
import pandas as pd
import matplotlib.pyplot as plt

covid = COVID19Uganda()

covid.generate_bar_graph()
# covid.generate_line_graph() fix the IO error
    
    