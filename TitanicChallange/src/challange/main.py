# Import the Pandas library

import pandas as pd
import numpy as npy

# Load the train and test datasets to creat    e two DataFrames
train_url = "../../data/train.csv"
train = pd.read_csv(train_url)

test_url = "../../data/test.csv"
test = pd.read_csv(test_url)

#print("#########Train Info#########")
#train.info()
#print("\n#########Test Info#########")
#test.info()

# Non-Quantitative fields are dropped, also cabin has too many null values
train = train.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
test = test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)


# Add in age with mean value

meanTrain = npy.mean(train["Age"])
x1 = npy.array(train["Age"])
x1[npy.isnan(x1)] = meanTrain
train["Age"] = x1

meanTest = npy.mean(test["Age"])
x2 = npy.array(test["Age"])
x2[npy.isnan(x2)] = meanTest
test["Age"] = x2


# Make Sibling and Parch into boolean parameter 'Family'
train["Family"] = int(0)
# Set 1 in Family to person that has sibling
row_index = train["SibSp"] >= 1
train.loc[row_index, 'Family'] = 1
# Set 1 in Family to person that has Parch (can duplicate with sibling)
row_index = train["Parch"] >= 1
train.loc[row_index, 'Family'] = 1
# Drop the former two parameter since we have new
train = train.drop(["SibSp", "Parch"], axis=1)

# Make Sibling and Parch into boolean parameter 'Family'
test["Family"] = int(0)
# Set 1 in Family to person that has sibling
row_index = test["SibSp"] >= 1
test.loc[row_index, 'Family'] = 1
# Set 1 in Family to person that has Parch (can duplicate with sibling)
row_index = test["Parch"] >= 1
test.loc[row_index, 'Family'] = 1
# Drop the former two parameter since we have new
test = test.drop(["SibSp", "Parch"], axis=1)

# Add mean fare to the missing value in test
meanTest = npy.mean(test["Fare"])
x = npy.array(test["Fare"])
x[npy.isnan(x)] = meanTest
test["Fare"] = x

# Apparently S is the majority of Embarked, so we fill the missing value in 
# print(sum(train["Embarked"] == 'S'))
train['Embarked'] = train['Embarked'].fillna("S")




