#---------------------------------------------------------------------#
#Program Name: modelling.py
#Description: Apply different models to predict the value
#---------------------------------------------------------------------#

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model

import pandas as pd
import os

def model_random_forests(x_train,y_train, x_test,y_test ):
    print("\n\n Modelling with Random Forests")
    print("#---------------------------------------------------------------------------#")
    rf = RandomForestRegressor()
    print('Now Training the model...')
    rf.fit(x_train, y_train)
    print('Now Predicting the accuracy for train dataset')
    print('Accuracy Score for Train dataset: %.2f' % rf.score(x_train, y_train))
    print('Now Predicting the accuracy for test dataset')
    print('Accuracy Score for Test dataset: %.2f' % rf.score(x_test, y_test))

    output_file = 'predictions'+'/'+'RF_Actual_Predicted_output.csv'
    if os.path.exists(output_file):
        os.remove(output_file)

    print("Predicting the values and writing the Actual and Predicted values to the file ",output_file )
    predicted_values = rf.predict(x_test)
    df = pd.DataFrame({'Actual_Values': y_test, 'Predicted_Values':predicted_values })
    print("Printing output to the csv file")
    df.to_csv(output_file)
    print("------------Random Forests Modelling Ended---------------------")


def model_linear_regression(x_train, y_train, x_test, y_test):
    print("\n\n Modelling with Linear Regression")
    print("#---------------------------------------------------------------------------#")
    regression_model = linear_model.LinearRegression()
    print('Now Training the model...')
    regression_model.fit(x_train, y_train)
    print("Intercepts:", regression_model.intercept_)# Check trained model y-intercept
    print("Coefficients:",regression_model.coef_) # Check trained model coefficients
    print('Now Predicting the accuracy for train dataset')
    print('Accuracy Score for Train dataset: %.2f' % regression_model.score(x_train, y_train))
    print('Now Predicting the accuracy for test dataset')
    print('Accuracy Score for Test dataset: %.2f' % regression_model.score(x_test, y_test))

    output_file = 'predictions' + '/' + 'LR_Actual_Predicted_output.csv'
    if os.path.exists(output_file):
        os.remove(output_file)
    print("Predicting the values and writing the Actual and Predicted values to the file ",output_file )
    predicted_values = regression_model.predict(x_test)
    df = pd.DataFrame({'Actual_Values': y_test, 'Predicted_Values':predicted_values })
    print("Printing output to the csv file")
    df.to_csv(output_file)
    print("------------Linear Regression Modelling Ended---------------------")



