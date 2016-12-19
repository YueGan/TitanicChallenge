# Import the Pandas library

import pandas as pd

# Load the train and test datasets to creat    e two DataFrames
train_url = "../../data/train.csv"
train = pd.read_csv(train_url)

test_url = "../../data/test.csv"
test = pd.read_csv(test_url)

#Print the `head` of the train and test dataframes
print(train)
print(test)