#---------------------------------------------------------------------#
#Program Name: fill_null_values.py
#Description: Fill the Null Values
#---------------------------------------------------------------------#

def fill_null_values(data, col_name, value):
    print("Filling Null Values for ",col_name)
    print("#-----------------------------------------------------------#")
    data[col_name].fillna(value, inplace= True)