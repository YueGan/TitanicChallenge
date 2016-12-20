""" 
selected train model
"""


import csv as csv
import numpy as np
import pandas as pd
#read train data and test data
train = pd.read_csv("../../data/train.csv")
test = pd.read_csv("../../data/train.csv")

# New Column 'Child', 1 if Child, 0 if not 
train["Child"] = 1
train.loc[train["Age"]>18,'Child'] = 0

# New Column 'gender', 1 if female, 0 if male
train["gender"] = 0
train.loc[train["Sex"]=="female",'gender'] = 1
train.loc[train["Sex"]=="male",'gender'] = 0

# Select model with only 1 and 0
del train['Age'],train['PassengerId'],train['SibSp'],train['Parch']
del train['Ticket'],train['Cabin'],train['Embarked'],train['Name'],train['Sex']

# Output to new data set
train.to_csv('../../data/Train_Set.csv')

# New Column 'Child', 1 if Child, 0 if not 
test["Child"] = 0
test.loc[test["Age"]>18,'Child'] =1

# New Column 'gender', 1 if female, 0 if male
test["gender"] = 0
test.loc[test["Sex"]=="female",'gender'] = 1
test.loc[test["Sex"]=="male",'gender'] = 0

del test['Age'],test['PassengerId'],test['SibSp'],test['Parch']
del test['Ticket'],test['Cabin'],test['Embarked'],test['Name'],test['Sex']
test = test.fillna(test.mean()) # Fill the empty slots

test.to_csv('../../data/Test_Set.csv')
	
