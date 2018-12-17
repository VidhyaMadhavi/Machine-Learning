#---------------------------------------------------------------------#
#Program Name: feature_engineering
#Description: Selects the important features that can be used for modelling
#---------------------------------------------------------------------#
from sklearn import preprocessing

from eda import heatmap

def convert_string_to_numbers(data):
    str_cols = list(data.select_dtypes(include=['object']).columns)
    print("List of columns:")
    print(str_cols)
    for col in str_cols:
        newcolname = col+'_int'
        str_int = preprocessing.LabelEncoder()
        data[newcolname] = str_int.fit_transform(data[col])

    print(data.head(2))
    return data

def feature_engineering(data):
    print("\n\nFeature Engineering")
    print("#-----------------------------------------------------------#")
    print(data.head(2))
    print("#--------Converting the String data to numbers by Label Encoder------------#")
    updated_data = convert_string_to_numbers(data)
    heatmap(updated_data)
    return updated_data


