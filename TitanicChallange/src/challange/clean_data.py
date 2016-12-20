
"""script to clean the test,training data"""
import pandas as pd
import numpy as npy
import csv as csv
import matplotlib.pyplot as plt
import re
from sklearn. ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt

# Load the train and test datasets to creat    e two DataFrames
train_url = "../../data/train.csv"
train = pd.read_csv(train_url)

test_url = "../../data/test.csv"
test = pd.read_csv(test_url)

#fill the missing data in Embarked with the most occured value
train["Embarked"]=train["Embarked"].fillna("S")

c=0
for i in [train, test]:
    # Unrelevant fields are dropped, also cabin has too many null values
    i = i.drop(['PassengerId','Ticket', 'Cabin', 'Name'], axis=1)
    
    # Add in age with mean value
    
    mean1 = npy.mean(i["Age"])
    x1 = npy.array(i["Age"])
    x1[npy.isnan(x1)] = mean1
    i["Age"] = x1
    

    #set female to 1, male to 0
    i.loc[i["Sex"]=="female",'Sex'] = 1
    i.loc[i["Sex"]=="male",'Sex'] = 0
    

    # Make Sibling and Parch into boolean parameter 'Family'
    i["Family"] = int(0)
    # Set 1 in Family to person that has sibling
    row_index = i["SibSp"] >= 1
    i.loc[row_index, 'Family'] = 1
    # Set 1 in Family to person that has Parch (can duplicate with sibling)
    row_index = i["Parch"] >= 1
    i.loc[row_index, 'Family'] = 1
    # Drop the former two parameter since we have new
    i = i.drop(["SibSp", "Parch"], axis=1)
    

    # Add mean fare to the missing value
    i["Fare"]=i["Fare"].fillna(i["Fare"].mean())
    
   
    
    #split age into several classes
    i.loc[i["Age"]<=18,'Age'] = 1
    i.loc[i["Age"]>18,'Age'] = 2
    
    #split Fare into several classes
    i.loc[i["Fare"]<=20,'Fare'] = 1
    i.loc[i["Fare"]>20,'Fare'] = 2
    
    
    i.loc[i["Embarked"]=="S",'Embarked'] = 1
    i.loc[i["Embarked"]=="Q",'Embarked'] = 2
    i.loc[i["Embarked"]=="C",'Embarked'] = 3
    
    #preview of the cleaned data
    print(i.head())
    if c == 0:
        i.to_csv("train_data.csv",index=False)
        c+=1
    else:
        i.to_csv("test_data.csv", index=False) 

 
    

