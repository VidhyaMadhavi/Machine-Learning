#---------------------------------------------------------------------#
#Program Name: prepare_data.py
#Description: Fill the Null Values
#---------------------------------------------------------------------#
from sklearn.model_selection import  train_test_split

def prepare_data(data, predicted_col):

    print("\n\nPrepare the data for modelling. Dividing the data in to train and test")
    print("#---------------------------------------------------------------------------#")
    Y = data[predicted_col]
    X = data.drop([predicted_col], axis='columns', inplace=False)
    str_cols = list(data.select_dtypes(include=['object']).columns)
    X = data.drop(str_cols, axis='columns', inplace=False)
    print(data.head(2))

    # Percent of the X array to use as training set. This implies that the rest will be test set
    test_size = .33

    # Split into train and validation
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=3)

    print ('Shape of Train Input Data:', x_train.shape)
    print('Shape of Test Input Data:', x_test.shape)
    print('Shape of Train Output Data:', y_train.shape)
    print('Shape of Test Output Data:', y_test.shape)

    return ([x_train, x_test, y_train, y_test])
