#---------------------------------------------------------------------#
#Program Name: read_data.py
#Description: Read the data from the file in to dataframe
#---------------------------------------------------------------------#

import pandas as pd
def read_data(filename):
    data = pd.read_csv(filename, encoding='cp1252')
    return data