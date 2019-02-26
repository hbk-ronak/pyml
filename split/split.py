import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split(X,y, stratify = True, size = 0.25):
    """
    The function takes two inputs the X or the independent variable and
    y or the dependent variable
    User can choose to use stratified split or unstratified split
    The module will break the data into two parts train and test based on the size user defined
    """
    logs = ""
    if stratify:
        x_train, x_test, y_train, y_test = train_test_split(X,y, stratify = y, test_size = size, random_state = 1)
        logs += "The ratio of classes in the whole data is %f and the ratio of classes in training data is %f \n" %(float(y.sum())/len(y),float(y_train.sum())/len(y_train))
    else:
        x_train, x_test, y_train, y_test = train_test_split(X,y, test_size = size, random_state = 1)
        logs += "The ratio of classes in the whole data is %f and the ratio of classes in training data is %f \n" %(float(y.sum())/len(y),float(y_train.sum())/len(y_train))
    logs += "training set has %i rows and validation set has %i rows" %(x_train.shape[0],x_test.shape[0])
    print(logs)
    return x_train, x_test, y_train, y_test