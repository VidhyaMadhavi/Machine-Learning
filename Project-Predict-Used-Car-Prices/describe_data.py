#---------------------------------------------------------------------#
#Program Name: describe_data.py
#Description: To find out
# Shape of the data : Number of columns, rows
# Data types of the data
# Data Central Tendency values
#---------------------------------------------------------------------#

def describe_data(data):
    print("\n\n Print first few records of the Data:")
    print("#-----------------------------------------------------------#")
    print(data.head(2))

    print ("\n\n Shape of the Dataset:")
    print("#-----------------------------------------------------------#")
    print (data.shape)

    print("\n\n Datatypes of the Data:")
    print("#-----------------------------------------------------------#")
    print(data.info())

    print("\n\n Data Central Tendency Values:")
    print("#-----------------------------------------------------------#")
    print(data.describe())


def display_null_counts(data):
    print ("\n\n Null Values in the Dataset:")
    print("#-----------------------------------------------------------#")
    print(data.isnull().sum())