""" 
selected train model
"""


import csv as csv
import numpy as np
import pandas as pd
#read train data and test data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


train["Child"] = 0
train.loc[train["Age"]>18,'Child'] =1

train["gender"] = 0
train.loc[train["Sex"]=="female",'gender'] = 1
train.loc[train["Sex"]=="male",'gender'] = 0

del train['Age'],train['PassengerId'],train['SibSp'],train['Parch']

del train['Ticket'],train['Cabin'],train['Embarked'],train['Name'],train['Sex']


train.to_csv('Train_Set.csv')



test["Child"] = 0
test.loc[test["Age"]>18,'Child'] =1

test["gender"] = 0
test.loc[test["Sex"]=="female",'gender'] = 1
test.loc[test["Sex"]=="male",'gender'] = 0

del test['Age'],test['PassengerId'],test['SibSp'],test['Parch']

del test['Ticket'],test['Cabin'],test['Embarked'],test['Name'],test['Sex']
test = test.fillna(test.mean())
test.to_csv('Test_Set.csv')
	
