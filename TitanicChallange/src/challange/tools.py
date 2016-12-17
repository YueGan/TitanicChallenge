'''
Dimension .shape
print(train.head().shape)
(5, 10)
'''

'''
Describe the data
print(train.head().describe())

       PassengerId  Survived    Pclass       Age     SibSp  Parch       Fare
count     5.000000  5.000000  5.000000   5.00000  5.000000    5.0   5.000000
mean      3.000000  0.600000  2.200000  31.20000  0.600000    0.0  29.521660
std       1.581139  0.547723  1.095445   6.83374  0.547723    0.0  30.510029
min       1.000000  0.000000  1.000000  22.00000  0.000000    0.0   7.250000
25%       2.000000  0.000000  1.000000  26.00000  0.000000    0.0   7.925000
50%       3.000000  1.000000  3.000000  35.00000  1.000000    0.0   8.050000
75%       4.000000  1.000000  3.000000  35.00000  1.000000    0.0  53.100000
max       5.000000  1.000000  3.000000  38.00000  1.000000    0.0  71.283300

'''

'''
# absolute numbers
train["Survived"].value_counts()

# percentages
train["Survived"].value_counts(normalize = True)

train["Survived"][train["Sex"] == 'male'].value_counts()
train["Survived"][train["Sex"] == 'female'].value_counts()



'''

'''
# Create the column Child and assign to 'NaN'
train["Child"] = float('NaN')

# Assign 1 to passengers under 18, 0 to those 18 or older. Print the new column.


train["Child"][train["Age"] < 18] = 1
train["Child"][train["Age"] >= 18] = 0
print(train["Child"])

# Print normalized Survival Rates for passengers under 18
print(train["Survived"][train["Child"] == 1].value_counts(normalize = True))

# Print normalized Survival Rates for passengers 18 or older
print(train["Survived"][train["Child"] == 0].value_counts(normalize = True))

'''




